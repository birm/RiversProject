import {Component, Input, OnInit } from '@angular/core';
import {ObservationService} from '../observation.service';
import { ChartDataset, ChartOptions } from 'chart.js';
import 'chartjs-adapter-moment';

@Component({
  selector: 'app-line-chart',
  templateUrl: './line-chart.component.html',
  styleUrls: ['./line-chart.component.css']
})
export class LineChartComponent implements OnInit {

  @Input() site = "-1";
  @Input() field = "unkown";

  public lineChartLabels : any[] = [];
  public chartData : any[] = [];
  public canvas: any;
  public chartConfig : (ChartOptions & { annotation?: any }) = {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      xAxes: {
        type: 'timeseries'
      }
    }
  }

  constructor(private observationService: ObservationService) { }

  getChartData(){
    this.observationService.getObvservationsBySite(this.site).subscribe(z=>{
      this.chartData = z.map(i=>{ return {x:i.datetime, y:i[this.field as keyof typeof i]}});
      this.lineChartLabels = z.map(i=>i.datetime);
    });
  }

  ngOnInit(): void {
    this.getChartData();
  }

}
