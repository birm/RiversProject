package us.rbirm.rivers;

import java.util.List;
import org.springframework.data.repository.CrudRepository;

public interface SiteRepository extends CrudRepository<Site, String>{
  Site findByName(String name);
  List<Site> findAll();
}
