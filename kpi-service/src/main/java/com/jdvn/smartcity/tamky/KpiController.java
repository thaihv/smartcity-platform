package com.jdvn.smartcity.tamky;

import java.security.Principal;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/kpi")
public class KpiController {

	private final static Logger log = LoggerFactory.getLogger(KpiController.class);

	@GetMapping("/hello")
	public String Greetings(Principal principal) {
		String username = principal.getName();
		log.info("Get Principal");
		return "Hello, " + username;
	}

	@GetMapping("all-kpis")
	public String allKpis() {
		return "All KPIs is here";
	}

	@GetMapping("good-kpis")
	public String goodKpis() {
		return "All good KPIs is here";
	}
}
