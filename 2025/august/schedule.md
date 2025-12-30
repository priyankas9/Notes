
 public function setPriority($id)

    {

    if(empty($id))

    {

    $containments=Containment::whereNULL('deleted_at')->get();

    }

    else

    {

    $containments=Containment::find($id);

    }

    $updates= [];

    foreach ($containmentsas$containment) {

    $constructionDate=Carbon::parse($containment->construction_date);

    $lastEmptiedDate=$containment->last_emptied_date?Carbon::parse($containment->last_emptied_date) :null;

    // storing values already in db for comparison and update

    $old_priority=$containment->priority;

    $oldfstp_distance=$containment->fstp_distance;

    $oldfstp_id=$containment->closest_fstp_id;

    $now=Carbon::now();

    // Determine priority

    // if containment has not been emptied

    if (is_null($lastEmptiedDate)) {

    // if we dont have containment construction date, we assume highest priority

    if (is_null($constructionDate)) {

    $containment->priority=1;

    }

    else

    {

    // if construction date present, we use same logic as emptying date

    $yearsSinceConstruction=$constructionDate->diffInYears($now);

    if ($yearsSinceConstruction>3) {

    $containment->priority=1;

    } elseif ($yearsSinceConstruction>1  &&$yearsSinceConstruction<=3) {

    $containment->priority=2;

    } else {

    $containment->priority=3;

    }

    }

    } else {

    // priority logic according to last emptied

    $yearsSinceLastEmptied=$lastEmptiedDate->diffInYears($now);

    if ($yearsSinceLastEmptied>3) {

    $containment->priority=1;

    } elseif ($yearsSinceLastEmptied>1&&$yearsSinceLastEmptied<=3) {

    $containment->priority=2;

    } else {

    $containment->priority=3;

    }

    }

    // Fetch all FSTPs with specified conditions

    $treatment_plant_types= ['FSTP', 'Co-Treatment Plant'];

    // Reverse map text values to IDs

    $typeIds=array_keys(array_filter(TreatmentPlantType::toEnumArray(),function($label)use($treatment_plant_types){

    returnin_array($label,$treatment_plant_types);

    }));

    $fstps=TreatmentPlant::whereIn('type', $typeIds)

    ->where('status', true)

    ->get();

    if ($fstps->count() ==0) {

    returnresponse()->json(['status' => 'error', 'message' => 'No FSTP or Co-Treatment Plants registered. Please register treatment plant and try again.']);

    }

    elseif ($fstps->count() ==1) {

    $fstp=$fstps->first();

    $distanceResult=DB::selectOne("

    SELECT ROUND(ST_Distance(

    ST_Transform(c.geom, 32646),

    ST_Transform(f.geom, 32646)

    )::numeric , 6) AS distance

    FROM fsm.containments c, fsm.treatment_plants f

    WHERE c.id = ? AND f.id = ?

    ", [$containment->id, $fstp->id]);

    $containment->fstp_distance=$distanceResult->distance;

    $containment->closest_fstp_id=$fstp->id;

    } else {

    $distances= [];

    foreach ($fstpsas$fstp) {

    $distanceResult=DB::selectOne("

    SELECT ROUND(ST_Distance(

    ST_Transform(c.geom, 32646),

    ST_Transform(f.geom, 32646)

    )::numeric , 6) AS distance

    FROM fsm.containments c, fsm.treatment_plants f

    WHERE c.id = ? AND f.id = ?

    ", [$containment->id, $fstp->id]);

    $distances[$fstp->id] =$distanceResult->distance;

    }

    if (!empty($distances)) {

    // if multiple FSTP, select the fstp closest

    $containment->fstp_distance=min($distances);

    $containment->closest_fstp_id=array_search($containment->fstp_distance,$distances);

    } else {

    $containment->fstp_distance=null;

    $containment->closest_fstp_id=null;

    }

    }

    if ($oldfstp_distance!=$containment->fstp_distance||$oldfstp_id!=$containment->closest_fstp_id||$old_priority!=$containment->priority) {

    $updates[] = [

    'id' => $containment->id,

    'fstp_distance' =>  $containment->fstp_distance,

    'closest_fstp_id' => $containment->closest_fstp_id,

    'priority' =>  $containment->priority

    ];

    }

    }

    if (!empty($updates)) {

    foreach (array_chunk($updates,500) as$chunk) {

    foreach ($chunkas$update) {

    Containment::where('id', $update['id'])->update([

    'priority' => $update['priority'],

    'fstp_distance' => $update['fstp_distance'],

    'closest_fstp_id' => $update['closest_fstp_id']

    ]);

    }

    }

    }

    }
