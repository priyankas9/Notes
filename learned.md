



---

**map display from datatable**

---

if u want to show on map from datatable : add in the fetch function

e.g :  $content.='<a title="Map" href="'.action("MapsController@index", ['layer'=>'buildings', 'field'=>'bin', 'val'=>$model->bin]) .'" class="btn btn-info btn-xs">`<i class="fa fa-map-marker"><i>``</a>` ';
  and getMapextent -> layer name if in base there will be difference if the geom is in point or polygon in MAPCONTROLLER

---

**SHOW LAYER**

---

- if you want to show a filter the just add layer name in showLayer('layer name');

---

**Map zoom in initila load**

---

- if you want to zoom then work here

 functionzoomToCity() {

    map.getView().setCenter(ol.proj.transform([85.29197216033933, 27.715958575192687], 'EPSG:4326', 'EPSG:3857')); //just add the long and lat

    map.getView().setZoom(16); // You can adjust the zoom level if needed

    }
