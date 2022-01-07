import { Injectable } from '@angular/core';
import {Observation} from './observation';

@Injectable({
  providedIn: 'root'
})
export class ObservationService {
  constructor() { }

  getObvservations(): Observation[]{
    return [{id:1, site:1, gage_height:14, datetime:"01/01/2022 00:01:00"}];
  }

  getObvservationsBySite(site: number): Observation[]{
    return [{id:1, site:site, gage_height:14, datetime:"01/01/2022 00:01:00"}, {id:1, site:site, gage_height:15, datetime:"01/01/2022 00:02:00"}, {id:1, site:site, gage_height:13, datetime:"01/01/2022 00:03:00"}];
  }

  getObservationsBySiteAndType(site: number, field: string): any[]{
    let res: any[] = [];
    for (let i of this.getObvservationsBySite(site)){
      if (i[field as keyof typeof i]){
        res.push({x:i.datetime, y:i[field as keyof typeof i]})
      }
    }
    return res;
  }
}
