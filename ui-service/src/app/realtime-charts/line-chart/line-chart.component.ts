import { Component, OnInit } from '@angular/core';
import { ChartDataSets, ChartType, ChartOptions } from 'chart.js';
import { Color, Label } from 'ng2-charts';
import {Router} from "@angular/router";
import {NgxSpinnerService} from "ngx-spinner";
import {KeycloakService} from 'keycloak-angular';
import {TemperaturePoint} from "../temperature-point";
import {RealtimeService} from "../realtime.service";
@Component({
  selector: 'app-line-chart',
  templateUrl: './line-chart.component.html',
  styleUrls: ['./line-chart.component.css']
})
export class LineChartComponent implements OnInit {

  lineChartData: ChartDataSets[] = [
    { data: [85, 72, 78, 75, 77, 75], label: 'Temperature Variation' },
  ];

  lineChartLabels: Label[] = ['January', 'February', 'March', 'April', 'May', 'June'];

  lineChartOptions = {
    responsive: true,
  };

  lineChartColors: Color[] = [
    {
      borderColor: 'black',
      backgroundColor: 'rgba(255,255,0,0.28)',
    },
  ];

  lineChartLegend = true;
  lineChartPlugins = [];
  lineChartType: ChartType = 'line';
  X: Array<string> = [];
  Y: Array<number> = [];
  
//  temperatures: Array<TemperaturePoint>;
  temperatures: TemperaturePoint[] =[];
  constructor(private realtimeService:RealtimeService,
    private keycloakService:KeycloakService,
    private ngxSpinnerService:NgxSpinnerService,
    private router:Router){ }  
  ngOnInit()
  {
    this.getTemperatures();
  }
  private getTemperatures()
  {
    this.ngxSpinnerService.show();
    this.realtimeService.getTemperatures('http://localhost:8091/realtime/temperatures?startTime=1563142100&endTime=1631469392').subscribe(
      data=>
      {

        for(var key in data) {
          var value = data[key];
          if (key == 'data')
            this.temperatures.push(value);
        }        

        console.log(this.temperatures);
        const object = Object.assign({}, ...this.temperatures);  

        for (let i = 0; i < Object.keys(object).length; i++) {     
          this.X.push(new Date(object[i]['unixTimestamp']*1000).toLocaleString());
          //var fToC = (object[i]['temperatureInFahrenheit'] - 32) * 5 / 9;
          this.Y.push(object[i]['temperatureInFahrenheit']);
        }

        this.lineChartLabels = this.X;
        this.lineChartData = [
          { data: this.Y, label: 'Temperature Variation' },
        ];
        this.ngxSpinnerService.hide();
      },
      error1 =>
      {
        this.ngxSpinnerService.hide();
      }
    );
  }    


}
