import {Component, Input, OnInit } from '@angular/core';
import {SiteService} from '../site.service';
import {Site} from '../site';
import { Observable, of } from 'rxjs';

@Component({
  selector: 'app-grid',
  templateUrl: './grid.component.html',
  styleUrls: ['./grid.component.css']
})
export class GridComponent implements OnInit {
  public sites: Site[] = [];
  getSites(): void {
    this.siteService.getSites().subscribe(
      sites => {
        this.sites = sites
      });
  }

  constructor(private siteService: SiteService) { }

  ngOnInit(): void {
    this.getSites();
  }

}
