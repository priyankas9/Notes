
---

## How GeoJSON data flows into an OpenLayers map

### 1. The file format itself

A GeoJSON file is just JSON with a specific shape:

json

```json
{
"type":"FeatureCollection",
"features":[
{
"type":"Feature",
"geometry":{"type":"Polygon","coordinates":[[[84.1,28.3], ...]]},
"properties":{"name":"Kathmandu","population":1000000}
}
]
}
```

The coordinates are in **longitude/latitude (EPSG:4326)** but OL's map canvas uses **Web Mercator (EPSG:3857)** — meters, not degrees. That's why every fetch in your code does `featureProjection:"EPSG:3857"` during parsing, which reprojects on the fly.

---

### 2. The fetch → parse → render pipeline

```
Network (fetch)
    ↓
Raw JSON blob (text)
    ↓
ol/format/GeoJSON or TopoJSON  ←── reprojects coords 4326 → 3857
    ↓
ol/Feature[]  (each has a Geometry + properties Map)
    ↓
VectorSource.addFeatures()  ←── spatial index built here (R-tree)
    ↓
VectorLayer  ←── reads from source, applies Style per feature
    ↓
Canvas 2D renderer  ←── draws polygons/lines/points each frame
```

Each step matters:

**`fetch(url)`** — just an HTTP GET. The browser caches it like any asset. If the file is 10MB, the whole 10MB arrives before anything renders — this is the main pain point.

**`new GeoJSON().readFeatures(data, options)`** — walks every feature, converts coordinate arrays from `[lon, lat]` pairs into OL's internal `[x_meters, y_meters]` format using the `proj4` library under the hood.

**`VectorSource`** — stores features in an **R-tree** (spatial index). This means when OL asks "which features are visible in this viewport extent?", it's an O(log n) lookup, not scanning every feature.

**`VectorLayer`** — on every map render frame, asks the source for features in the current view extent, then calls your `style` function for each one to get stroke/fill/etc, then draws to canvas.

---

### 3. Why TopoJSON is different

Your districts and provinces use TopoJSON not GeoJSON. The key difference:

```
GeoJSON:   each polygon stores its own coordinates (shared borders duplicated)
TopoJSON:  stores "arcs" (line segments) once, polygons reference arc IDs
```

A shared border between two districts is stored **once** in TopoJSON instead of twice. This typically cuts file size by 40-80% for administrative boundary data. OL's `ol/format/TopoJSON` reassembles the arcs back into polygons during `readFeatures()`.

---

### 4. What the R-tree spatial index actually does

When you zoom into Kathmandu district, OL calls internally:

ts

```ts
source.getFeaturesInExtent([minX, minY, maxX, maxY])
```

The R-tree returns only features whose bounding boxes overlap that extent. For a ward layer with 6,000+ features, this means OL might only style/draw ~50 of them even though all 6,000 are loaded in memory. That's why panning is fast even with large datasets loaded — the bottleneck is the initial fetch and parse, not rendering.

---

### 5. The style function call chain

For every visible feature, every frame:

ts

```ts
// Your static style object (fast — same object reused):
const districtStyle =newStyle({ stroke:newStroke({...}), fill:newFill({...})})

// Dynamic style function (called per-feature, per-frame — keep it cheap):
style:(feature, resolution)=>{
const name = feature.get("name")
return name ==="Kathmandu"? highlightStyle : normalStyle
}
```

The resolution argument (meters per pixel at current zoom) lets you hide labels at low zoom, change stroke width, etc. This is how most map apps do zoom-dependent styling.

---

### 6. The specific flow in your code

ts

```ts
// 1. Lazy load — only fetch when layer is toggled on
useEffect(()=>{
if(!isOn.district|| src.getFeatures().length>0)return// ← guard: fetch once

fetchJson(DISTRICT_URL)// 2. HTTP GET
.then(data =>newTopoJSON().readFeatures(data,{
      featureProjection:"EPSG:3857",// 3. reproject during parse
      dataProjection:"EPSG:4326",
}))
.then(features => src.addFeatures(features))// 4. into R-tree
},[isOn.district])
```

The `src.getFeatures().length > 0` guard is important — without it, toggling the layer off and on would re-fetch the file every time.

---

### 7. Common performance traps

| Problem                                          | Symptom                     | Fix                                                       |
| ------------------------------------------------ | --------------------------- | --------------------------------------------------------- |
| Large GeoJSON (>2MB)                             | Long freeze on first toggle | Simplify geometry with `mapshaper`, or use vector tiles |
| Style function creates `new Style()`every call | Janky pan/zoom              | Cache style objects outside the function                  |
| All features loaded at all zooms                 | Slow on ward/village level  | Set `minZoom`/`maxZoom`on the layer                   |
| No loading indicator                             | UI appears frozen           | Your `setInfo("Loading...")`pattern is exactly right    |

---

The vector tile approach solves the biggest one (large file size + full download) by slicing the data spatially and only sending what the viewport needs — which is why it's worth doing for production.
