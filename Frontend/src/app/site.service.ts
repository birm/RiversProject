import { Injectable } from '@angular/core';
import {Site} from './site';

@Injectable({
  providedIn: 'root'
})
export class SiteService {

  constructor() { }

  getSites(): Site[]{
    return [{"name":"North Peachtree", "latitude":45.0, "longitude": 41, site:1},{"name":"South Peachtree", "latitude":44.0, longitude:41, site:2}];
  }

}
