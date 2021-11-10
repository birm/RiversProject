package us.rbirm.rivers;

import javax.persistence.Entity;
import javax.persistence.Table;
import javax.persistence.Id;

@Entity
@Table(name = "site")
public class Site {
  @Id
  private String site_no;
  private String name;
  private Float latitude;
  private Float longitude;

  @Override
  public String toString() {
    return String.format("Site[site_no=%s, name='%s']", site_no, name);
  }

  public String getSiteNo(){
    return site_no;
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
