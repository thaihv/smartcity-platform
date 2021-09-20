import { Component, OnInit } from '@angular/core';
import { KeycloakService } from 'keycloak-angular';
import { KeycloakProfile } from 'keycloak-js';

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent implements OnInit {

  public userProfile: KeycloakProfile | null = null;
  constructor(private readonly keycloak: KeycloakService) { }
  public async ngOnInit() {
      this.userProfile = await this.keycloak.loadUserProfile();
  }

}
