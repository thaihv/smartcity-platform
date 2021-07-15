package com.jdvn.smartcity.tamky;

import java.security.Principal;
import java.util.Arrays;
import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.hateoas.CollectionModel;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.jdvn.smartcity.tamky.domain.model.Kpi;
import com.jdvn.smartcity.tamky.domain.model.Unit;
import com.jdvn.smartcity.tamky.domain.repository.KpiRepository;
import com.jdvn.smartcity.tamky.domain.repository.UnitRepository;

@RestController
@RequestMapping("/kpi")
public class KpiController {

	@Autowired
	private KpiRepository kpiRepository;

	@Autowired
	private UnitRepository unitRepository;

	private final static Logger log = LoggerFactory.getLogger(KpiController.class);

	@GetMapping("/hi")
	public String Greetings(Principal principal) {
		String username = principal.getName();
		log.info("Get Principal");
		return "Hello, " + username;
	}

	@GetMapping("/kpis")
	public CollectionModel<Kpi> getAllKpis() {
		List<Kpi> kpis = kpiRepository.findAll();
		CollectionModel<Kpi> result = CollectionModel.of(kpis);
		return result;
	}

	@GetMapping("/kpis/{kpiId}")
	public CollectionModel<Kpi> getKpiById(@PathVariable Long kpiId) {

		CollectionModel<Kpi> result = CollectionModel.of(Arrays.asList(kpiRepository.getOne(kpiId)));
		return result;
	}

	@GetMapping("/units")
	public CollectionModel<Unit> getKpiUnits() {
		List<Unit> units = unitRepository.findAll();
		CollectionModel<Unit> result = CollectionModel.of(units);
		return result;
	}

	@GetMapping("/units/{kpiId}")
	public CollectionModel<Unit> getUnitByKpiId(@PathVariable Long kpiId) {
		Kpi kpi = kpiRepository.getOne(kpiId);
		CollectionModel<Unit> result = CollectionModel.of(Arrays.asList(kpi.getUnit()));
		return result;
	}
}
