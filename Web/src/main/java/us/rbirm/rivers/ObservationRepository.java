package us.rbirm.rivers;

import java.util.List;
import org.springframework.data.repository.CrudRepository;

public interface ObservationRepository extends CrudRepository<Observation, String>{
  List<Observation> findAll();
  List<Observation> findBySite(String site);
}
