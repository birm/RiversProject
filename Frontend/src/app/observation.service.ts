import { Injectable } from '@angular/core';
import {Observation} from './observation';

@Injectable({
  providedIn: 'root'
})
export class ObservationService {
  constructor() { }

  getObvservations(): Observation[]{
    return [{id:1, site:1, gage_height:14}];
  }

  getObvservationsBySite(site: number): Observation[]{
    return [{id:1, site:site, gage_height:14}, {id:1, site:site, gage_height:15}, {id:1, site:site, gage_height:13}];
  }

  getObservationsBySiteAndType(site: number, field: string): any[]{
    let res: any[] = [];
    for (let i of this.getObvservationsBySite(site)){
      console.log(i)
      res.push(i[field as keyof typeof i] || -1);
    }
    return res;
  }
}
