import {Component, Input, OnInit } from '@angular/core';

import {ObservationService} from '../observation.service';
import {Observation} from '../observation'

@Component({
  selector: 'app-site',
  templateUrl: './site.component.html',
  styleUrls: ['./site.component.css'],
})
export class SiteComponent implements OnInit {

  public chartTypes = ["gage_height", "precipitation", "turbidity"];

  @Input() site = {"name":"Uninitailized", "latitude":-1, "longitude": -1, "site": "-1"}

  public observations: Observation[] = [];
  public chartData = {};

  constructor(private observationService: ObservationService) {
  }
  getObvservations(){
    this.observationService.getObvservationsBySite(this.site.site).subscribe(
      observations => {
        this.observations = observations
      });
  }

  ngOnInit(): void {
    this.getObvservations();
  }

}
