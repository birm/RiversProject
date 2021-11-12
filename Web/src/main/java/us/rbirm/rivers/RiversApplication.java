package us.rbirm.rivers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@SpringBootApplication
@RestController
public class RiversApplication {
	@Autowired
	private SiteRepository siteRepository;
	@Autowired
	private ObservationRepository observationRepository;
	@Autowired
	private PredictionRepository predictionRepository;

	public static void main(String[] args) {
		SpringApplication.run(RiversApplication.class, args);
	}
	@GetMapping("/hello")
		public String hello(@RequestParam(value = "name", defaultValue = "World") String name) {
			return String.format("Hello %s!", name);
	}
	@GetMapping("/sites")
		public List < Site > getAllSites() {
			return siteRepository.findAll();
	}
	@GetMapping("/observations")
		public List < Observation > getAllObservations() {
			return observationRepository.findAll();
	}
	@GetMapping("/observations/from")
		public List < Observation > getSiteObservations(@RequestParam(value = "site") String site) {
			return observationRepository.findBySite(site);
	}
	@GetMapping("/predictions")
		public List < Prediction > getAllPredictions() {
			return predictionRepository.findAll();
	}
	@GetMapping("/predictions/from")
		public List < Prediction > getSitePredictions(@RequestParam(value = "site") String site) {
			return predictionRepository.findBySite(site);
	}



}
