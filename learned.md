

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

    ** *varmap=newol.Map({***

** *controls:ol.control.defaults().extend([newol.control.ScaleLine()]),***

** *interactions:ol.interaction.defaults({***

** *altShiftDragRotate:false,***

** *dragPan:false,***

** *rotate:false,***

** *doubleClickZoom:false***

** *}).extend([newol.interaction.DragPan({***

** *kinetic:null***

** *})]),***

** *target:'olmap',***

** *view:newol.View({***

***minZoom:13,***

** *
    maxZoom:21, // set zoom here* **

** *extent:ol.proj.transformExtent([85.28712272644042, 27.725009654030885, 85.30171394348145, 27.705092489448575], 'EPSG:4326', 'EPSG:3857') // add coordintates using the coordinate information tool***

** *})***

** *});***

---
