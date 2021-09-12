package com.jdvn.smartcity.tamky.api;

import java.util.List;
import java.util.Optional;

import javax.annotation.security.RolesAllowed;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.jdvn.smartcity.tamky.domain.model.Kpi;
import com.jdvn.smartcity.tamky.domain.model.Unit;
import com.jdvn.smartcity.tamky.domain.repository.KpiRepository;
import com.jdvn.smartcity.tamky.domain.repository.UnitRepository;

@RestController
@CrossOrigin
public class KpiController {

	@Autowired
	private KpiRepository kpiRepository;

	@Autowired
	private UnitRepository unitRepository;

	private final static Logger log = LoggerFactory.getLogger(KpiController.class);

	@GetMapping("/")
	@RolesAllowed({ "ADMIN", "USER" })
	public String Greetings() {
		log.info("Get Principal");
		return "Hello";
	}

	@RolesAllowed({ "ADMIN", "USER" })
	@GetMapping(path = "/list", produces = MediaType.APPLICATION_JSON_VALUE)
	@ResponseBody
	public List<Kpi> getAllKpis() {
		return kpiRepository.findAll();
	}

	@RolesAllowed({ "ADMIN", "USER" })
	@GetMapping("/find/{id}")
	public Optional<Kpi> findKpiById(@PathVariable Long id) {
		return kpiRepository.findById(id);
	}

	@RolesAllowed({ "ADMIN" })
	@PostMapping("/update")
	public Kpi update(@RequestBody Kpi kpi) {
		return kpiRepository.saveAndFlush(kpi);
	}

	@RolesAllowed({ "ADMIN" })
	@PostMapping("/create")
	public List<Kpi> create(@RequestBody Kpi kpi) {
		kpiRepository.saveAndFlush(kpi);
		return kpiRepository.findAll();
	}

	@RolesAllowed({ "ADMIN" })
	@DeleteMapping("/delete/{id}")
	public void delete(@PathVariable Long id) {
		kpiRepository.deleteById(id);
	}

	@RolesAllowed({ "ADMIN", "USER" })
	@GetMapping("/unit/list")
	public List<Unit> getKpiUnits() {
		return unitRepository.findAll();
	}

	@RolesAllowed({ "ADMIN", "USER" })
	@GetMapping("/unit/find/{id}")
	public Optional<Unit> getUnitByUnitId(@PathVariable Long id) {
		return unitRepository.findById(id);
	}
}
