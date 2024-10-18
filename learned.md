if u want to show on map from datatable : add in the fetch function
e.g :  $content.='<a title="Map" href="'.action("MapsController@index", ['layer'=>'buildings', 'field'=>'bin', 'val'=>$model->bin]) .'" class="btn btn-info btn-xs">`<i class="fa fa-map-marker"><i>``</a>` ';
  and getMapextent -> layer name if in base there will be difference if the geom is in point or polygon in MAPCONTROLLER
