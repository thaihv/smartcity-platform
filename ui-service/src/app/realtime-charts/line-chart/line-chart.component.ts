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

  temperatures: Array<TemperaturePoint>;
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
    this.realtimeService.getTemperatures('http://localhost:8091/realtime/temperatures?startTime=1563142100&endTime=1631439989').subscribe(
      data=>
      {
        this.temperatures=data;
        console.log('data as : ' + data);
        console.log(this.temperatures);
        this.ngxSpinnerService.hide();
      },
      error1 =>
      {
        this.ngxSpinnerService.hide();
      }
    );
  }    
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

}
