package com.jdvn.smartcity.tamky.api;

import java.util.Arrays;
import java.util.List;

import javax.annotation.security.RolesAllowed;

import org.keycloak.adapters.springsecurity.token.KeycloakAuthenticationToken;
import org.keycloak.representations.AccessToken;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.hateoas.CollectionModel;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.oauth2.jwt.Jwt;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.jdvn.smartcity.tamky.domain.model.Kpi;
import com.jdvn.smartcity.tamky.domain.model.Unit;
import com.jdvn.smartcity.tamky.domain.repository.KpiRepository;
import com.jdvn.smartcity.tamky.domain.repository.UnitRepository;


@RestController
public class KpiController {

	@Autowired
	private KpiRepository kpiRepository;

	@Autowired
	private UnitRepository unitRepository;

	private final static Logger log = LoggerFactory.getLogger(KpiController.class);

	@GetMapping("/")
	@RolesAllowed("USER")
	@ResponseBody
	public String Greetings(@AuthenticationPrincipal Jwt jwt) {
		log.info("Get Principal");
//        KeycloakAuthenticationToken keycloakAuthenticationToken = (KeycloakAuthenticationToken) principal;
//        AccessToken accessToken = keycloakAuthenticationToken.getAccount().getKeycloakSecurityContext().getToken();
//        model.addAttribute("username", accessToken.getGivenName());		
		return String.format("Hello");
	}

	@GetMapping("/kpi-all")
//	@RolesAllowed("user")
	@ResponseBody
	public CollectionModel<Kpi> getAllKpis() {
		List<Kpi> kpis = kpiRepository.findAll();
		CollectionModel<Kpi> result = CollectionModel.of(kpis);
		return result;
	}
	@RolesAllowed("USER")
	@GetMapping("/kpi-all/{kpiId}")
	public CollectionModel<Kpi> getKpiById(@PathVariable Long kpiId) {

		CollectionModel<Kpi> result = CollectionModel.of(Arrays.asList(kpiRepository.findById(kpiId).get()));
		return result;
	}

	@RolesAllowed("ADMIN")
	@GetMapping("/unit-all")
	public CollectionModel<Unit> getKpiUnits() {
		List<Unit> units = unitRepository.findAll();
		CollectionModel<Unit> result = CollectionModel.of(units);
		return result;
	}
	@RolesAllowed("ADMIN")
	@GetMapping("/unit-all/{unitId}")
	public CollectionModel<Unit> getUnitByUnitId(@PathVariable Long unitId) {
		Unit unit = unitRepository.findById(unitId).get();
		CollectionModel<Unit> result = CollectionModel.of(Arrays.asList(unit));
		return result;
	}
}
