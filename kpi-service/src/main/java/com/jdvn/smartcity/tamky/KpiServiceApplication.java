package com.jdvn.smartcity.tamky;

import java.util.stream.Stream;

import org.springframework.boot.ApplicationRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

import com.jdvn.smartcity.tamky.domain.model.Kpi;
import com.jdvn.smartcity.tamky.domain.repository.KpiRepository;

@EnableDiscoveryClient
@SpringBootApplication
public class KpiServiceApplication {

	public static void main(String[] args) {
		SpringApplication.run(KpiServiceApplication.class, args);
	}

	@Configuration
	static class OktaOAuth2WebSecurityConfigurerAdapter extends WebSecurityConfigurerAdapter {

		@Override
		protected void configure(HttpSecurity http) throws Exception {
			// @formatter:off
			http.authorizeRequests().anyRequest().authenticated().and().oauth2ResourceServer().jwt();
			// @formatter:on
		}
	}

	@Bean
	ApplicationRunner init(KpiRepository repository) {
		return args -> {
			Stream.of("Air Quality", "Water and Sanitation", "Energy", "Housing", "Food Security", "Buildings",
					"Employment", "Electricity Supply", "Drainage", "ICT Infrastructure").forEach(name -> {
						repository.save(new Kpi(name));
					});
			repository.findAll().forEach(System.out::println);
		};
	}
}
