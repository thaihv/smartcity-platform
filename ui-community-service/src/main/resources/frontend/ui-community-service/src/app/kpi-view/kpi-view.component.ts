import { Component, OnInit } from '@angular/core';
import {FormBuilder} from "@angular/forms";
import {ActivatedRoute} from "@angular/router";
import {NgxSpinnerService} from "ngx-spinner";
import {Kpi} from "src/app/kpi-list/kpi";
import {KpiService} from "src/app/kpi-list/kpi.service";
import { environment } from '../../environments/environment';

@Component({
  selector: 'app-kpi-view',
  templateUrl: './kpi-view.component.html',
  styleUrls: ['./kpi-view.component.css']
})
export class KpiViewComponent implements OnInit {

  kpi: Kpi;
  editMode: boolean=false;

  kpiForm = this.formBuilder.group({
    id: [{disabled: true}],
    code: [''],
    name: [''],
    frequencyInDays: [''],
    description: ['']
  });


  constructor(private kpiService:KpiService,
              private formBuilder:FormBuilder,
              private activatedRoute:ActivatedRoute,
              private ngxSpinnerService:NgxSpinnerService)
  { }

  ngOnInit()
  {
    this.getKpiDetails();
  }

  private getKpiDetails()
  {
    let id=this.activatedRoute.snapshot.params.id;

    this.ngxSpinnerService.show();
    this.kpiService.getKpiById(environment.apiUrlBase + '/kpi/find/'+id).subscribe(
      data=>
      {
        this.kpi=data;
        this.kpiForm.patchValue(
          {
            id: data.id,
            code: data.code,
            name: data.name,
            frequencyInDays: data.frequencyInDays,
            description: data.description
          });
        this.ngxSpinnerService.hide();
        this.activatedRoute.snapshot.params.editMode=='true'?this.editMode=true:this.editMode=false;
      },
      error1 =>
      {
        this.ngxSpinnerService.hide();
      }
    );
  }

  editKpi()
  {
    this.editMode=true;
  }

  updateKpi()
  {
    this.ngxSpinnerService.show();

    console.info(this.kpiForm.value);
    let kpi=this.kpiForm.value;

    this.kpiService.updateKpi(environment.apiUrlBase + '/kpi/update', kpi).subscribe(
      data=>
      {
        this.kpi=data;
        this.kpiForm.patchValue(
          {
            id: data.id,
            code: data.code,
            name: data.name,
            frequencyInDays: data.frequencyInDays,
            description: data.description
          });
        this.editMode=false;

        this.ngxSpinnerService.hide();
      },
      error1 =>
      {
        this.ngxSpinnerService.hide();
      }
    );

  }

  cancelUpdate()
  {
    this.editMode=false;
  }
}
