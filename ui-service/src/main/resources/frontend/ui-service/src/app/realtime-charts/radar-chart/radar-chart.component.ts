import { Component, OnInit } from '@angular/core';
import { ChartDataSets, ChartType, RadialChartOptions } from 'chart.js';
import { Label } from 'ng2-charts';

@Component({
  selector: 'app-radar-chart',
  templateUrl: './radar-chart.component.html',
  styleUrls: ['./radar-chart.component.css']
})
export class RadarChartComponent {

  public radarChartOptions: RadialChartOptions = {
    responsive: true,
  };
  public radarChartLabels: Label[] = ['Delivered energy', 'ICT tools satisfaction', 'CO2 emissions',
    'Number of households', 'Investment', 'Vehicle fuel efficiency', 'Citizen information satisfaction'];

  public radarChartData: ChartDataSets[] = [
    { data: [0, 1, 2, 3, 4, 5, 6], label: 'Key Performance Indicator Analysis' }
  ];
  public radarChartType: ChartType = 'radar';

}
