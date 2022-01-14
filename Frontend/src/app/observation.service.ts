import { Injectable } from '@angular/core';
import {Observation} from './observation';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ObservationService {
  constructor(private http: HttpClient) { }
  public observationsUrl = "/api/observations"
  private defaultData = [{id:1, site:"-1", gageHeight:14, datetime:"01/01/2022 00:01:00"}, {id:1, site:"-1", gageHeight:15, datetime:"01/01/2022 00:02:00"}, {id:1, site:"-1", gageHeight:13, datetime:"01/01/2022 00:03:00"}]

  private handleError<T>(result?: T){
    return (error: any): Observable<T> => {
      console.error(error);
      return of(result as T);
    }
  }

  getObvservations(): Observable<Observation[]>{
    return this.http.get<Observation[]>(this.observationsUrl).pipe(
      catchError(this.handleError<Observation[]>(this.defaultData))
    );
  }

  getObvservationsBySite(site: string): Observable<Observation[]>{
    return this.http.get<Observation[]>(this.observationsUrl + "/from?site=" + site).pipe(
      catchError(this.handleError<Observation[]>(this.defaultData))
    );
  }
}
