import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {TemperaturePoint} from "./temperature-point";

@Injectable({
  providedIn: 'root'
})
export class RealtimeService {
  constructor(private httpClient:HttpClient) { }

  getTemperatures(url:string)
  {
    return this.httpClient.get<TemperaturePoint[]>(url);
  }
}
