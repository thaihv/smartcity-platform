import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Arena} from "./arena";

@Injectable({
  providedIn: 'root'
})
export class GeoService {

  constructor(private httpClient:HttpClient) { }
  
  getArenas(url:string)
  {
    return this.httpClient.get<any>(url);
  }
  getDistricts(url:string)
  {
    return this.httpClient.get<any>(url);
  }
  createArena(url: string, arena: Arena)
  {
    return this.httpClient.post<any>(url, arena);
  }  
}
