package us.rbirm.rivers;

import javax.persistence.Entity;
import javax.persistence.Table;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import java.util.Date;

@Entity
@Table(name = "prediction")
public class Prediction {
  @Id
  @GeneratedValue(strategy=GenerationType.AUTO)
  private Long id;
  private String site;
  private String type;
  private Float value;
  private Date datetime;

  @Override
  public String toString() {
    return String.format("Prediction[site=%s, type='%s']", site, type);
  }

  public Long getId(){
    return id;
  }
  public String getSite(){
    return site;
  }
  public String getType(){
    return type;
  }
  public Float getValue(){
    return value;
  }
  public Date getDatetime(){
    return datetime;
  }
}
