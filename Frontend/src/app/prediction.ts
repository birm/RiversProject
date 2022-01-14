export class Prediction {
  id: number = -1;
  site: string = "-1";
  datetime: string = "1970-01-01 12:00:01";
  temperature?: number = -1;
  precipitation?: number = -1;
  discharge?: number = -1;
  gageHeight?: number = -1;
  conductance?: number = -1;
  dissolvedOxygen?: number = -1;
  pH?: number = -1;
  turbidity?: number = -1;
}
