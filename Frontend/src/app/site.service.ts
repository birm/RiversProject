import { Injectable } from '@angular/core';
import {Site} from './site';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class SiteService {

  constructor(private http: HttpClient) { }
  public sitesUrl = "/api/sites/";
  private defaultData = [{"name":"North Peachtree", "latitude":45.0, "longitude": 41, site:"1"},{"name":"South Peachtree", "latitude":44.0, longitude:41, site:"2"}];

  private handleError<T>(result?: T){
    return (error: any): Observable<T> => {
      console.error(error);
      return of(result as T);
    }
  }

  getSites(): Observable<Site[]>{
    return this.http.get<Site[]>(this.sitesUrl).pipe(
      catchError(this.handleError<Site[]>(this.defaultData))
    );
  }

}
