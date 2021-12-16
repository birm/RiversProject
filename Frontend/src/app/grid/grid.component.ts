import {Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-grid',
  templateUrl: './grid.component.html',
  styleUrls: ['./grid.component.css']
})
export class GridComponent implements OnInit {

  @Input() sites = [{"name":"North Peachtree", "prediction":14.5},{"name":"South Peachtree", "prediction":1.2}];

  constructor() { }

  ngOnInit(): void {
  }

}
