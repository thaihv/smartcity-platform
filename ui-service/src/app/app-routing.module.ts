import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {KpiListComponent} from "./kpi-list/kpi-list.component";
import {KpiViewComponent} from "./kpi-view/kpi-view.component";
const routes: Routes = [
  {
    path: 'kpi/list',
    component: KpiListComponent
  },  
  {
    path: 'kpi/:id',
    component: KpiViewComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
