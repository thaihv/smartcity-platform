import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {KpiListComponent} from "./kpi-list/kpi-list.component";
import {KpiViewComponent} from "./kpi-view/kpi-view.component";
import {UserProfileComponent} from "./user-profile/user-profile.component";
import { LineChartComponent } from './realtime-charts/line-chart/line-chart.component';
import { BarChartComponent } from './realtime-charts/bar-chart/bar-chart.component';
import { DoughnutChartComponent } from './realtime-charts/doughnut-chart/doughnut-chart.component';
import { RadarChartComponent } from './realtime-charts/radar-chart/radar-chart.component';
import { PieChartComponent } from './realtime-charts/pie-chart/pie-chart.component';
import { BubbleChartComponent } from './realtime-charts/bubble-chart/bubble-chart.component';
import { RealtimeChartsComponent } from './realtime-charts/realtime-charts.component';

const routes: Routes = [
  { path: '', pathMatch: 'full', redirectTo: '/' },
  { path: 'kpi/list', component: KpiListComponent},  
  { path: 'kpi/:id', component: KpiViewComponent},
  { path: 'userinfo', component: UserProfileComponent},
  { path: 'charts', component: RealtimeChartsComponent,
    children:[
      {path: '', pathMatch: 'full', redirectTo: 'line-chart'},
      { path: 'line-chart', component: LineChartComponent },
      { path: 'bar-chart', component: BarChartComponent },
      { path: 'doughnut-chart', component: DoughnutChartComponent },
      { path: 'radar-chart', component: RadarChartComponent },
      { path: 'pie-chart', component: PieChartComponent },
      { path: 'bubble-chart', component: BubbleChartComponent }
  ]}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
