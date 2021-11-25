import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from "@angular/common/http";
import { Arena } from "./arena";
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class GeoService {

  constructor(private httpClient: HttpClient) { }

  getArenas(url: string) {
    return this.httpClient.get<any>(url);
  }
  getDistricts(url: string) {
    return this.httpClient.get<any>(url);
  }
  createArena(url: string, arena: Arena) {
    return this.httpClient.post<any>(url, arena);
  }
  deleteArena(url: string) {
    return this.httpClient.delete(url);
  }
  convertToFile(url: string, formData: FormData): Observable<any> {
    return this.httpClient.post(url, formData, {
      reportProgress: true,
      observe: 'events'
    }).pipe(
      catchError(this.errorMgmt)
    )
  }
  downloadFile(url: string) {
    return this.httpClient.get(url, { responseType: 'blob' });
  }

  errorMgmt(error: HttpErrorResponse) {
    let errorMessage = '';
    if (error.error instanceof ErrorEvent) {
      // Get client-side error
      errorMessage = error.error.message;
    } else {
      // Get server-side error
      errorMessage = `Error Code: ${error.status}\nMessage: ${error.message}`;
      console.log(error);
    }
    console.log(errorMessage);
    return throwError(errorMessage);
  }

}
