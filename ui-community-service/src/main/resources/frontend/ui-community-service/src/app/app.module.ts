import {HTTP_INTERCEPTORS, HttpClientModule} from "@angular/common/http";
import {NgModule} from "@angular/core";
import {ReactiveFormsModule} from "@angular/forms";
import {BrowserModule} from "@angular/platform-browser";
import {BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {NgxSpinnerModule} from "ngx-spinner";

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { KpiListComponent } from './kpi-list/kpi-list.component';
import { KpiViewComponent } from './kpi-view/kpi-view.component';
import { ChartsModule } from 'ng2-charts';
import { RealtimeChartsComponent } from './realtime-charts/realtime-charts.component';
import { BarChartComponent } from './realtime-charts/bar-chart/bar-chart.component';
import { BubbleChartComponent } from './realtime-charts/bubble-chart/bubble-chart.component';
import { DoughnutChartComponent } from './realtime-charts/doughnut-chart/doughnut-chart.component';
import { LineChartComponent } from './realtime-charts/line-chart/line-chart.component';
import { PieChartComponent } from './realtime-charts/pie-chart/pie-chart.component';
import { RadarChartComponent } from './realtime-charts/radar-chart/radar-chart.component';
import { HomeComponent } from './home/home.component';

@NgModule({
  declarations: [
    AppComponent,
    KpiListComponent,
    KpiViewComponent,
    RealtimeChartsComponent,
    BarChartComponent,
    BubbleChartComponent,
    DoughnutChartComponent,
    LineChartComponent,
    PieChartComponent,
    RadarChartComponent,
    HomeComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    ReactiveFormsModule,
    AppRoutingModule,
    HttpClientModule,
    NgxSpinnerModule,
    ChartsModule
  ],
  providers: [
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
