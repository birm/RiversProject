package us.rbirm.rivers;

import javax.persistence.Entity;
import javax.persistence.Table;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import java.util.Date;

@Entity
@Table(name = "observation")
public class Observation {
  @Id
  @GeneratedValue(strategy=GenerationType.AUTO)
  private Long id;
  private String site_no;
  private Date Datetime;
  private Float Temperature;
  private Float Precipitation;
  private Float Discharge;
  private Float GageHeight;
  private Float Conductance;
  private Float DO;
  private Float pH;
  private Float Turbidity;

  @Override
  public String toString() {
    return String.format("Observation for[site_no=%s]", site_no);
  }

  public String getSiteNo(){
    return site_no;
  }
  public Long getId(){
    return id;
  }
  public Date getDatetime(){
    return Datetime;
  }
  public Float getTemperature(){
    return Temperature;
  }
  public Float getPrecipitation(){
    return Precipitation;
  }
  public Float getDischarge(){
    return Discharge;
  }
  public Float getGageHeight(){
    return GageHeight;
  }
  public Float getConductance(){
    return Conductance;
  }
  public Float getDO(){
    return DO;
  }
  public Float getpH(){
    return pH;
  }
  public Float getTurbidity(){
    return Turbidity;
  }
}
