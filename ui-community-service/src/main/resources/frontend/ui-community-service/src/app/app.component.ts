import { Component, OnInit } from '@angular/core';
import { Cookie } from 'ng2-cookies';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'Tamky Smart City Platform';
  public redirectUri = 'http://localhost:8080/community/';
  constructor() { }

  public async ngOnInit() {

  }

  public logout() {
    let logoutURL = "http://tamky.xyz:8080/auth/realms/Smartcity/protocol/openid-connect/logout?redirect_uri=" + this.redirectUri;
    window.location.href = logoutURL;
  }  
}
