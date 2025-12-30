// map.js
import Map from 'ol/Map';
import View from 'ol/View';
import TileLayer from 'ol/layer/Tile';
import VectorLayer from 'ol/layer/Vector';
import VectorSource from 'ol/source/Vector';
import OSM from 'ol/source/OSM';
import GeoJSON from 'ol/format/GeoJSON';
import { Fill, Stroke, Style , Text } from 'ol/style';
import { transformExtent, fromLonLat } from 'ol/proj';
import { all as loadingStrategyAll } from 'ol/loadingstrategy';

export function initMap() {
    const geoServerURL = import.meta.env.VITE_GEOSERVER_URL;
    const geoServerWorkspace = import.meta.env.VITE_GEOSERVER_WORKSPACE;
    const buildingsStyleFunction = (feature) => {
    const sd = feature.get('sd'); // assuming 'sd' is your field
    const bin = feature.get('bin'); // field used for label
        console.log( "SD:", sd, "Bin:", bin); // debug log
    return new Style({
        fill: new Fill({
            color: 'rgba(254, 191, 255, 0.4)' // #febfff with 0.4 opacity
        }),
        stroke: new Stroke({
            color: 'rgba(0, 0, 1, 0.4)', // #000001 with 0.4 opacity
            width: 0.01,
            lineJoin: 'bevel'
        }),
        text:  new Text({
            text: bin ? String(bin) : '',
            font: 'bold 12px Arial',
            fill: new Fill({ color: 'black' }),
            stroke: new Stroke({ color: 'white', width: 2 }), // halo effect
            offsetY: -10,
            textAlign: 'center',
            textBaseline: 'middle'
        })
    });
};
const roadAllStyleFunction = (feature) => {
    const roadCode = feature.get('road_code');

    return [
        // Outer stroke: black, width 7
        new Style({
            stroke: new Stroke({
                color: 'black',
                width: 7
            })
        }),

    // Inner stroke: firebrick (#B22222), width 5
        new Style({
            stroke: new Stroke({
                color: '#B22222',
                width: 5
            })
        }),

    // Label on line using road_code
        new Style({
            text: new Text({
                text: roadCode ? String(roadCode) : '',
                font: '14px Arial',
                fill: new Stroke({ color: 'black' }), // label color
                stroke: new Stroke({ color: '#ffffff', width: 3 }), // white halo
                placement: 'line',
                textAlign: 'center',
                textBaseline: 'middle',
                offsetY: 7,
                padding: [10, 10, 10, 10]
            })
        })
    ];
};
//console.log("GeoServer:", geoServerURL, geoServerWorkspace); // test

    const mLayer = {

    // wards_layer: { name: 'Communes / Sangkats' },
        buildings_layer: { name: 'Building Survey' },
        // citypolys_layer: { name: 'Building Footprints' },
        // roadAll_layer : {name: 'Roads'},
        road_layer: { name: 'Roads Survey' },
        // sewer_layer : {name : 'Sewer'}
        survey_grids: { name: 'Survey Grids' },
    };

    const overlayContainer = document.getElementById("overlay_checkbox_container");

    for (const key in mLayer) {
        const label = document.createElement("label");
        label.style.display = "block";

    const checkbox = document.createElement('input');
        checkbox.type = "checkbox";
        checkbox.id =`layer_${key}`;
        checkbox.dataset.layerKey = key;
        checkbox.checked = true;

    label.appendChild(checkbox);
        label.append(mLayer[key].name);
        overlayContainer.appendChild(label);
    }

    const baseLayer = new TileLayer({ source: new OSM() });

    const wardsLayer = new VectorLayer({
        source: new VectorSource({
            format: new GeoJSON(),
            url:`${geoServerURL}/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=${geoServerWorkspace}:communes_sangkats_layer&outputFormat=application/json`,
            strategy: loadingStrategyAll
        }),
        style: new Style({
            stroke: new Stroke({ color: 'red', width: 1.5 }),
            fill: new Fill({ color: 'rgba(255, 0, 0, 0.05)' })
        }),
        visible: true
    });
    const citypolysLayer = new VectorLayer({
        source: new VectorSource({
            format: new GeoJSON(),
            url: `${geoServerURL}/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=${geoServerWorkspace}:building_footprints&outputFormat=application/json`,
            strategy: loadingStrategyAll
        }),
        style: new Style({
            stroke: new Stroke({ color: 'black', width: 2 }),
            fill: new Fill({ color: 'rgba(0, 0, 235, 0.1)' })
        }),
        visible: true
    });
    const buildingsLayer = new VectorLayer({
    source: new VectorSource({
        format: new GeoJSON(),
        url: `${geoServerURL}/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=${geoServerWorkspace}:building_surveys_layer&outputFormat=application/json`,
        strategy: loadingStrategyAll
    }),
    style: buildingsStyleFunction,
    visible: true
    });
     const roadLayer = new VectorLayer({
        source: new VectorSource({
            format: new GeoJSON(),
            url: `${geoServerURL}/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=${geoServerWorkspace}:road_networks_layer&outputFormat=application/json`,
            strategy: loadingStrategyAll
        }),
        style: new Style({
            stroke: new Stroke({ color: 'black', width: 2 }),
            fill: new Fill({ color: 'rgba(0, 0, 235, 0.1)' })
        }),
        visible: true
        });
        const roadAllLayer = new VectorLayer({
        source: new VectorSource({
            format: new GeoJSON(),
            url: `${geoServerURL}/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=${geoServerWorkspace}:road_networks_layer&outputFormat=application/json`,
            strategy: loadingStrategyAll
        }),
        style: roadAllStyleFunction,
        visible: true
    });

    const sewerLayer = new VectorLayer({
        source: new VectorSource({
            format: new GeoJSON(),
            url:`${geoServerURL}/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=${geoServerWorkspace}:sewer_networks_all&outputFormat=application/json`,
            strategy: loadingStrategyAll
        }),
        style: new Style({
            stroke: new Stroke({ color: 'black', width: 2 }),
            fill: new Fill({ color: 'rgba(0, 0, 235, 0.1)' })
        }),
        visible: true

    });

    const SurveyGridLayer = new VectorLayer({
        source: new VectorSource({
            format: new GeoJSON(),
            url:`${geoServerURL}/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=${geoServerWorkspace}:survey_grids_layer&outputFormat=application/json`,
            strategy: loadingStrategyAll
        }),
        style: new Style({
            stroke: new Stroke({ color: 'black', width: 2 }),
            fill: new Fill({ color: 'rgba(0, 0, 235, 0.1)' })
        }),
        visible: true

    });
    const extent = transformExtent(
        [103.86335, 13.362, 103.88335, 13.382],
        'EPSG:4326',
        'EPSG:3857'
    );

    const map = new Map({
        target: 'map',
        layers: [baseLayer, citypolysLayer, roadLayer,roadAllLayer,sewerLayer,wardsLayer, buildingsLayer, SurveyGridLayer],
        view: new View({
            center: fromLonLat([103.8594, 13.3611]),
            zoom: 14,
            minZoom: 14,
            extent: extent
        })
    });

    document.getElementById('layer_citypolys_layer')?.addEventListener('change', (e) => {
        citypolysLayer.setVisible(e.target.checked);
    });

    document.getElementById('layer_wards_layer')?.addEventListener('change', (e) => {
        wardsLayer.setVisible(e.target.checked);
    });

    document.getElementById('layer_buildings_layer')?.addEventListener('change', (e) => {
        buildingsLayer.setVisible(e.target.checked);
    });
    document.getElementById('layer_road_layer')?.addEventListener('change', (e) => {
        roadLayer.setVisible(e.target.checked);
    });
     document.getElementById('layer_roadall_layer')?.addEventListener('change', (e) => {
        roadAllLayer.setVisible(e.target.checked);
    });
     document.getElementById('layer_sewer_layer')?.addEventListener('change', (e) => {
        sewerLayer.setVisible(e.target.checked);
    });

    document.getElementById('layer_survey_grids')?.addEventListener('change', (e) => {
        SurveyGridLayer.setVisible(e.target.checked);
    });
}
