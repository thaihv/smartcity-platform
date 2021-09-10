import {HTTP_INTERCEPTORS, HttpClientModule} from "@angular/common/http";
import {APP_INITIALIZER, NgModule} from "@angular/core";
import {ReactiveFormsModule} from "@angular/forms";
import {BrowserModule} from "@angular/platform-browser";
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {NgxSpinnerModule} from "ngx-spinner";

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { KeycloakAngularModule, KeycloakService } from 'keycloak-angular';
import { KpiListComponent } from './kpi-list/kpi-list.component';
import { KpiViewComponent } from './kpi-view/kpi-view.component';

function initializeKeycloak(keycloak: KeycloakService) {
  return () =>
    keycloak.init({
      config: {
        url: 'http://tamky.xyz:8080/auth',
        realm: 'Smartcity',
        clientId: 'ui-service',
      },
      initOptions: {
        onLoad: 'check-sso',
        silentCheckSsoRedirectUri: window.location.origin + '/assets/silent-check-sso.html',
      },
    });
}
@NgModule({
  declarations: [
    AppComponent,
    KpiListComponent,
    KpiViewComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    ReactiveFormsModule,
    AppRoutingModule,
    HttpClientModule,
    NgxSpinnerModule,
    KeycloakAngularModule
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
