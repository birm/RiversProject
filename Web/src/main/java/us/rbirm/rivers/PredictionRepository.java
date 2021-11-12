package us.rbirm.rivers;

import java.util.List;
import org.springframework.data.repository.CrudRepository;

public interface PredictionRepository extends CrudRepository<Prediction, String>{
  List<Prediction> findAll();
  List<Prediction> findBySite(String site);
}
