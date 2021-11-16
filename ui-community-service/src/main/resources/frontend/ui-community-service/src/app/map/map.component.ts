import { Component, AfterViewInit } from '@angular/core';
import * as L from 'leaflet';
import { environment } from '../../environments/environment';
import { HttpClient } from "@angular/common/http";
import { geoJSON } from 'leaflet';


@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements AfterViewInit {

  private map: L.Map;

  private initMap(): void {

    const mbAttr = 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>'
    const mbUrl = 'https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoidGhhaWh2IiwiYSI6ImNrdmt0N2V5MTBldWUybm81cmlibGVod3UifQ.yan_bLwJOLo2jvieMzMpQQ';

    const watercolor = L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.png', {
      subdomains: 'abcd',
      maxZoom: 18,
      minZoom: 3,
      attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    });
    const grayscale = L.tileLayer(mbUrl, { id: 'mapbox/light-v9', tileSize: 512, zoomOffset: -1, attribution: mbAttr });
    const streets = L.tileLayer(mbUrl, { id: 'mapbox/streets-v11', tileSize: 512, zoomOffset: -1, attribution: mbAttr });
    const baseLayers = {
      'WaterColor': watercolor,
      "Grayscale": grayscale,
      "Streets": streets
    };

    var arenas = L.layerGroup();
    var states = L.layerGroup();

    const overlays = {
      "Arenas": arenas,
      "States": states
    };
    this.map = L.map('map', {
      center: [38.89304, -77.03699],
      zoom: 13,
      layers: [grayscale]
    });
    L.control.layers(baseLayers, overlays).addTo(this.map);

    // Arenas
    let arena_url = environment.apiUrlBase + '/geo-api/v0.1/arena/';

    this.httpClient.get<any>(arena_url).subscribe(
      data => {
        console.log(data);
        L.geoJSON(data, {

          onEachFeature: function (feature, layer) {
            layer.bindPopup(feature.properties.name).addTo(arenas)
          }
        }).addTo(this.map);
      },
      err => {
        console.log(err);
      });

    // Arenas
    let district_url = environment.apiUrlBase + '/geo-api/v0.1/state/16/';

    this.httpClient.get<any>(district_url).subscribe(
      data => {
        console.log(data);
        var myStyle = {
          "color": "#ff7800",
          "weight": 5,
          "opacity": 0.65
        };
        L.geoJSON(data, {
          style: myStyle,
          onEachFeature: function (feature, layer) {
            layer.bindPopup(feature.properties.name).addTo(states)
          }
        }).addTo(this.map);
      },
      err => {
        console.log(err);
      });



  }
  constructor(private httpClient: HttpClient) { }
  ngAfterViewInit(): void {
    this.initMap();
  }

}
