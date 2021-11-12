package us.rbirm.rivers;

import javax.persistence.Entity;
import javax.persistence.Table;
import javax.persistence.Id;

@Entity
@Table(name = "site")
public class Site {
  @Id
  private String site;
  private String name;
  private Float latitude;
  private Float longitude;

  @Override
  public String toString() {
    return String.format("Site[site=%s, name='%s']", site, name);
  }

  public String getSite(){
    return site;
  }
  public String getName(){
    return name;
  }
  public Float getLatitude(){
    return latitude;
  }
  public Float getLongitude(){
    return longitude;
  }
}
