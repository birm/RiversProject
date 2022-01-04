import {Component, Input, OnInit } from '@angular/core';
import {ObservationService} from '../observation.service'

@Component({
  selector: 'app-line-chart',
  templateUrl: './line-chart.component.html',
  styleUrls: ['./line-chart.component.css']
})
export class LineChartComponent implements OnInit {

  @Input() site = "-1";
  @Input() field = "unkown";

  public chartData : any[] = []

  constructor(private observationService: ObservationService) { }

  getChartData(){
    this.chartData = this.observationService.getObservationsBySiteAndType(parseInt(this.site), this.field);
    console.log(this)
  }

  ngOnInit(): void {
    this.getChartData();
  }

}
