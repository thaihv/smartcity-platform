import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Kpi} from "./kpi";
@Injectable({
  providedIn: 'root'
})
export class KpiService {

  constructor(private httpClient:HttpClient) { }

  getKpis(url:string)
  {
    return this.httpClient.get<Kpi[]>(url);
  }

  getKpiById(url:string)
  {
    return this.httpClient.get<Kpi>(url);
  }

  updateKpi(url: string, kpi: Kpi)
  {
    return this.httpClient.post<Kpi>(url,kpi);
  }

  createKpi(url: string, kpi: Kpi)
  {
    return this.httpClient.post<Kpi[]>(url, kpi);
  }

  deleteKpi(url: string)
  {
    return this.httpClient.delete(url);
  }
}
