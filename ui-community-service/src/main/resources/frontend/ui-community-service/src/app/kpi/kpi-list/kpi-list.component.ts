import { Component, OnInit } from '@angular/core';
import {Router} from "@angular/router";
import {NgxSpinnerService} from "ngx-spinner";
import {KeycloakService} from 'keycloak-angular';
import {Kpi} from "./kpi";
import {KpiService} from "./kpi.service";
import { environment } from '../../../environments/environment';

@Component({
  selector: 'app-kpi-list',
  templateUrl: './kpi-list.component.html',
  styleUrls: ['./kpi-list.component.css']
})
export class KpiListComponent implements OnInit {

  kpis: Array<Kpi>;

  constructor(private kpiService:KpiService,
              private keycloakService:KeycloakService,
              private ngxSpinnerService:NgxSpinnerService,
              private router:Router)
  { }

  ngOnInit()
  {
    this.getKpis();
  }

  private getKpis()
  {
    this.ngxSpinnerService.show();
    this.kpiService.getKpis(environment.apiUrlBase + '/kpi/list').subscribe(
      data=>
      {
        this.kpis=data;
        this.ngxSpinnerService.hide();
      },
      error1 =>
      {
        this.ngxSpinnerService.hide();
        console.log(error1);
      }
    );
  }


  logout()
  {
    this.keycloakService.logout();
  }

  createKpi()
  {
    this.ngxSpinnerService.show();
    let kpi=new Kpi();
    kpi.id=1001;
    kpi.code='T0';
    kpi.description='For a Test';
    kpi.frequencyInDays=30;
    kpi.name='Test';

    this.kpiService.createKpi(environment.apiUrlBase + '/kpi/create',kpi).subscribe(
      data=>
      {
        this.kpis=data;
        this.ngxSpinnerService.hide();
      },
      error1 =>
      {
        this.ngxSpinnerService.hide();
      }
    );
  }

  deleteKpi(id: number)
  {
    this.kpiService.deleteKpi(environment.apiUrlBase + '/kpi/delete/'+id).subscribe(
      data=>
      {
        this.getKpis();
      },
      error1 =>
      {
        this.ngxSpinnerService.hide();
      }
    );
  }

  editKpi(id: number)
  {
    this.router.navigate(["/kpis/" + id, { editMode: true }
    ]);
  }

}
