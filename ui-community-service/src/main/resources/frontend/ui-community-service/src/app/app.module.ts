import {HTTP_INTERCEPTORS, HttpClientModule} from "@angular/common/http";
import {APP_INITIALIZER, NgModule} from "@angular/core";
import {ReactiveFormsModule} from "@angular/forms";
import {BrowserModule} from "@angular/platform-browser";
import {BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {NgxSpinnerModule} from "ngx-spinner";

import {TokenInterceptor} from './interceptors/token-interceptor';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { KeycloakAngularModule, KeycloakService } from 'keycloak-angular';
import { KpiListComponent } from './kpi-list/kpi-list.component';
import { KpiViewComponent } from './kpi-view/kpi-view.component';
import { UserProfileComponent } from './user-profile/user-profile.component';
import { ChartsModule } from 'ng2-charts';
import { RealtimeChartsComponent } from './realtime-charts/realtime-charts.component';
import { BarChartComponent } from './realtime-charts/bar-chart/bar-chart.component';
import { BubbleChartComponent } from './realtime-charts/bubble-chart/bubble-chart.component';
import { DoughnutChartComponent } from './realtime-charts/doughnut-chart/doughnut-chart.component';
import { LineChartComponent } from './realtime-charts/line-chart/line-chart.component';
import { PieChartComponent } from './realtime-charts/pie-chart/pie-chart.component';
import { RadarChartComponent } from './realtime-charts/radar-chart/radar-chart.component';
import { HomeComponent } from './home/home.component';

function initializeKeycloak(keycloak: KeycloakService) {
  return () =>
    keycloak.init({
      config: {
        url: 'http://tamky.xyz:8080/auth',
        realm: 'Smartcity',
        clientId: 'ui-community-service',
      },
      initOptions: {
       onLoad: 'check-sso',
       //silentCheckSsoRedirectUri: window.location.origin + '/assets/silent-check-sso.html',
        // onLoad: 'login-required',
       checkLoginIframe: false
      },
    });
}
@NgModule({
  declarations: [
    AppComponent,
    KpiListComponent,
    KpiViewComponent,
    UserProfileComponent,
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
    KeycloakAngularModule,
    ChartsModule
  ],
  providers: [
    {
      provide: APP_INITIALIZER,
      useFactory: initializeKeycloak,
      multi: true,
      deps: [KeycloakService],
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
