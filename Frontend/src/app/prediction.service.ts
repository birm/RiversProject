import { Injectable } from '@angular/core';
import { Prediction } from './prediction';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class PredictionService {

  constructor(private http: HttpClient) { }
  public predictionsUrl = "/api/predictions"
  private defaultData = [{id:1, site:"-1", gageHeight:19, datetime:"01/01/2022 00:01:00"}]

  private handleError<T>(result?: T){
    return (error: any): Observable<T> => {
      console.error(error);
      return of(result as T);
    }
  }

  getPredictions(): Observable<Prediction[]>{
    return this.http.get<Prediction[]>(this.predictionsUrl).pipe(
      catchError(this.handleError<Prediction[]>(this.defaultData))
    );
  }

  getPredictionsBySite(site: string): Observable<Prediction[]>{
    return this.http.get<Prediction[]>(this.predictionsUrl + "/from?site=" + site).pipe(
      catchError(this.handleError<Prediction[]>(this.defaultData))
    );
  }
}
