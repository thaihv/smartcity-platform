import {HttpClientModule, HTTP_INTERCEPTORS} from "@angular/common/http";
import {APP_INITIALIZER, NgModule} from "@angular/core";
import {ReactiveFormsModule} from "@angular/forms";
import {BrowserModule} from "@angular/platform-browser";
import {BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {NgxSpinnerModule} from "ngx-spinner";
import { FileSaverModule } from 'ngx-filesaver';

import { environment } from '../environments/environment';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { KeycloakAngularModule, KeycloakService } from 'keycloak-angular';
import { KpiListComponent } from './kpi/kpi-list/kpi-list.component';
import { KpiViewComponent } from './kpi/kpi-view/kpi-view.component';
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
import { MapComponent } from './map/map.component';
import { KpiComponent } from './kpi/kpi.component';
import { OngoingComponent } from './ongoing/ongoing.component';
import {TokenInterceptor} from './interceptors/token-interceptor';

function initializeKeycloak(keycloak: KeycloakService) {
  return () =>
    keycloak.init({
      config: {
        url: environment.keycloakUrlBase,
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
    HomeComponent,
    MapComponent,
    KpiComponent,
    OngoingComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    ReactiveFormsModule,
    FileSaverModule,
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
    },
    {
      provide: HTTP_INTERCEPTORS,
      useClass: TokenInterceptor,
      multi: true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
