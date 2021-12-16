import {Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-line-chart',
  templateUrl: './line-chart.component.html',
  styleUrls: ['./line-chart.component.css']
})
export class LineChartComponent implements OnInit {

  @Input() data = [];
  @Input() name = "unkown";

  constructor() { }

  ngOnInit(): void {
  }

}
