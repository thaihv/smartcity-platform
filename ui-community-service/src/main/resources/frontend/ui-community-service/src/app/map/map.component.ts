import { Component, AfterViewInit } from '@angular/core';
import { FormBuilder, Validators } from "@angular/forms";
import * as L from 'leaflet';
import { environment } from '../../environments/environment';
import { Arena } from "./arena";
import { GeoService } from "./geo.service";
import { NgxSpinnerService } from "ngx-spinner";
import { FileSaverService } from 'ngx-filesaver';
import { HttpEvent, HttpEventType } from '@angular/common/http';


@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements AfterViewInit {

  private map: L.Map;
  arenas: Arena[] = [];
  isValidated = false;
  convertDone = false;
  progress: number = 0;
  fileDownload = '';
  arenaForm = this.formBuilder.group({
    id: [''],
    name: ['']
  });
  convertForm = this.formBuilder.group({
    srcfile: [''],
    format: ['geojson']
  });
  longitude = -77.03699;
  latitude = 38.89304;
  name = 'New Arena';
  constructor(private geoService: GeoService, private _FileSaverService: FileSaverService, private ngxSpinnerService: NgxSpinnerService, private formBuilder: FormBuilder) { }
  private addArenasToMap(controlLayers: L.Control.Layers) {
    this.ngxSpinnerService.show();
    this.geoService.getArenas(environment.apiUrlBase + '/geo-api/v0.1/arena/').subscribe(
      data => {
        for (var key in data) {
          var value = data[key];
          if (key == 'features') {
            value.forEach((element: { [x: string]: any; }) => {
              var properties = element['properties'];
              var geometry = element['geometry'];
              const arena: Arena = {
                id: 0,
                name: '',
                longitude: 0,
                latitude: 0
              };
              arena.id = properties['id']
              arena.name = properties['name'];
              arena.longitude = geometry['coordinates'][0];
              arena.latitude = geometry['coordinates'][1];
              this.arenas.push(arena);
            });
          }
        }
        var geojsonLayer = L.geoJSON(data, {
          onEachFeature: function (feature, layer) {
            layer.bindPopup(feature.properties.name)
          }
        }).addTo(this.map);
        controlLayers.addOverlay(geojsonLayer, 'Arenas');
        this.ngxSpinnerService.hide();
      },
      error1 => {
        this.ngxSpinnerService.hide();
        console.log(error1);
      }
    );
  }

  private addDistrictsToMap(controlLayers: L.Control.Layers) {
    this.ngxSpinnerService.show();
    this.geoService.getDistricts(environment.apiUrlBase + '/geo-api/v0.1/district/5/').subscribe(
      data => {
        var myLineStyle = {
          "color": "#ff7800",
          "weight": 5,
          "opacity": 0.65
        };
        var geojsonLayer = L.geoJSON(data, {
          style: myLineStyle,
          onEachFeature: function (feature, layer) {
            layer.bindPopup(feature.properties.name)
          }
        }).addTo(this.map);
        controlLayers.addOverlay(geojsonLayer, 'Districts');
        this.ngxSpinnerService.hide();
      },
      error1 => {
        this.ngxSpinnerService.hide();
        console.log(error1);
      }
    );
  }

  get areaName() {
    return this.arenaForm.get('name');
  }

  onChangeEvent(event: any) {
    this.areaName?.setValue(event.target.value, {
      onlySelf: true
    })
    this.name = this.arenaForm.get('name')?.value
  }
  onSubmit() {
    this.isValidated = true;
    if (!this.arenaForm.valid) {

    }
    else {
      for (var i = 0; i < this.arenas.length; i++) {
        var obj = this.arenas[i];
        var id = this.arenaForm.value['id'];
        if (id == obj.id) {
          this.map.panTo(new L.LatLng(obj.latitude, obj.longitude));
          break;
        }
      }

    }

  }
  addNewLocation() {

    this.ngxSpinnerService.show();
    let arena = new Arena();
    arena.name = this.name;
    arena.latitude = this.latitude;
    arena.longitude = this.longitude;
    this.geoService.createArena(environment.apiUrlBase + '/geo-api/v0.1/arena/add/', arena).subscribe(
      data => {
        this.ngxSpinnerService.hide();
      },
      error1 => {
        this.ngxSpinnerService.hide();
      }
    );

  }
  deleteLocation() {
    this.ngxSpinnerService.show();
    var id = this.arenaForm.value['id'];
    for (var i = 0; i < this.arenas.length; i++) {
      var obj = this.arenas[i];
      if (id == obj.id) {
        this.map.panTo(new L.LatLng(obj.latitude, obj.longitude));
        break;
      }
    }
    this.geoService.deleteArena(environment.apiUrlBase + '/geo-api/v0.1/arena/delete/' + id + '/').subscribe(
      data => {
        window.location.reload();
        this.ngxSpinnerService.hide();
      },
      error1 => {
        this.ngxSpinnerService.hide();
      }
    );
  }
  get srcFile() {
    return this.convertForm.get('srcfile');
  }
  uploadFile(event: any) {
    const file = event.target.files[0];
    this.convertForm.patchValue({
      srcfile: file
    });
    this.convertForm.get('srcfile')?.updateValueAndValidity()

  }
  covertToFile() {
    this.ngxSpinnerService.show();
    const formData = new FormData();
    formData.append('file', this.convertForm.value['srcfile']);
    formData.append('format', this.convertForm.value['format']);
    this.geoService.convertToFile(environment.apiUrlBase + '/geo-api/v0.1/util/convertofile/', formData).subscribe(
      (event: HttpEvent<any>) => {
        switch (event.type) {
          case HttpEventType.Sent:
            console.log('Request has been made!');
            break;
          case HttpEventType.ResponseHeader:
            console.log('Response header has been received!');
            break;
          case HttpEventType.UploadProgress:
            var eventTotal = event.total ? event.total : 0;
            this.progress = Math.round(event.loaded / eventTotal * 100);
            console.log(event.total);
            console.log(event.loaded);
            console.log('Uploaded! ${this.progress}%');
            break;
          case HttpEventType.Response:
            console.log('Image Upload Successfully!', event.body);
            this.convertDone = true
            this.fileDownload = event.body['filename']
            setTimeout(() => {
              this.progress = 0;
            }, 1500);

        }
      }
    );

  }
  download() {
    this.ngxSpinnerService.show();
    this.geoService.downloadFile(environment.apiUrlBase + '/geo-api/v0.1/util/return-files/' + this.fileDownload + '/').subscribe(
      data => {
        let filename = this.fileDownload
        const blob = new Blob([data], { type: 'application/zip' });
        this._FileSaverService.save(data, filename)
        this.ngxSpinnerService.hide();
        this.convertDone = false
      },
      error1 => {
        console.log(error1)
        this.ngxSpinnerService.hide();

      }
    );
  }
  private initMap() {

    const iconRetinaUrl = './assets/marker-icon-2x.png';
    const iconUrl = './assets/marker-icon.png';
    const shadowUrl = './assets/marker-shadow.png';
    const iconDefault = L.icon({
      iconRetinaUrl,
      iconUrl,
      shadowUrl,
      iconSize: [25, 41],
      iconAnchor: [12, 41],
      popupAnchor: [1, -34],
      tooltipAnchor: [16, -28],
      shadowSize: [41, 41]
    });
    L.Marker.prototype.options.icon = iconDefault;

    const mbAttr = 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>'
    const mbUrl = 'https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoidGhhaWh2IiwiYSI6ImNrdmt0N2V5MTBldWUybm81cmlibGVod3UifQ.yan_bLwJOLo2jvieMzMpQQ';

    const watercolor = L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.png', {
      subdomains: 'abcd',
      maxZoom: 18,
      minZoom: 3,
      attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    });
    const satellite = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', { maxZoom: 19 });
    const grayscale = L.tileLayer(mbUrl, { id: 'mapbox/light-v9', tileSize: 512, zoomOffset: -1, attribution: mbAttr });
    const streets = L.tileLayer(mbUrl, { id: 'mapbox/streets-v11', tileSize: 512, zoomOffset: -1, attribution: mbAttr });
    const baseLayers = {
      'WaterColor': watercolor,
      'Satellite': satellite,
      "Grayscale": grayscale,
      "Streets": streets
    };

    this.map = L.map('map', {
      center: [this.latitude, this.longitude],
      zoom: 13,
      layers: [watercolor]
    });
    var controlLayers = L.control.layers(baseLayers).addTo(this.map);
    this.addArenasToMap(controlLayers);
    this.addDistrictsToMap(controlLayers);

    var popup = L.popup();
    this.map.on('click', <LeafletMouseEvent>(e: { latlng: { lat: any; lng: any; }; }) => {
      console.log(e.latlng.lat);
      console.log(e.latlng.lng);
      this.longitude = e.latlng.lng
      this.latitude = e.latlng.lat
      popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng.toString())
        .openOn(this.map);
    });
  }



  ngAfterViewInit(): void {
    this.initMap();
  }

}
