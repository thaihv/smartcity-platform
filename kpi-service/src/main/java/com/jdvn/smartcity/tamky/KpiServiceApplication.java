package com.jdvn.smartcity.tamky;

import java.util.stream.Stream;

import org.springframework.boot.ApplicationRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.context.annotation.Bean;

import com.jdvn.smartcity.tamky.domain.model.Kpi;
import com.jdvn.smartcity.tamky.domain.model.Unit;
import com.jdvn.smartcity.tamky.domain.repository.KpiRepository;
import com.jdvn.smartcity.tamky.domain.repository.UnitRepository;

@EnableDiscoveryClient
@SpringBootApplication
public class KpiServiceApplication {

	public static void main(String[] args) {
		SpringApplication.run(KpiServiceApplication.class, args);
	}


	@Bean
	ApplicationRunner init(KpiRepository repository, UnitRepository unitRepository) {

		Unit unit = new Unit("Degree Celsius", "ºC");
		unitRepository.saveAndFlush(unit);
		unit = new Unit("Watt hour", "Wh");
		unitRepository.saveAndFlush(unit);		
		unit = new Unit("Watt", "W");
		unitRepository.saveAndFlush(unit);	
		
		return args -> {

			Stream.of("Air Quality", "Water and Sanitation", "Energy", "Housing", "Food Security", "Buildings",
					"Employment", "Electricity Supply", "Drainage", "ICT Infrastructure").forEach(name -> {

						Kpi kpi = new Kpi();
						kpi.setName(name);
						kpi.setCode("L1");
						kpi.setFrequencyInDays(3);
						kpi.setStructuralElement("District");
						kpi.setUnit(unitRepository.findAll().get(0));
						repository.saveAndFlush(kpi);
					});
			repository.findAll().forEach(System.out::println);
		};
	}

}
