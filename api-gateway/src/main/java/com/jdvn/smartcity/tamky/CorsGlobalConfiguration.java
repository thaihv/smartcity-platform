package com.jdvn.smartcity.tamky;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.reactive.config.CorsRegistry;
import org.springframework.web.reactive.config.EnableWebFlux;
import org.springframework.web.reactive.config.WebFluxConfigurer;

@Configuration
@EnableWebFlux
public class CorsGlobalConfiguration implements WebFluxConfigurer {

    @Override
    public void addCorsMappings(CorsRegistry corsRegistry) {
        corsRegistry.addMapping("/**")
          .allowedOrigins("http://localhost:4200")
          .allowedMethods("HEAD","GET", "POST", "PUT", "DELETE", "PATCH","OPTIONS")
          .maxAge(3600);
    }
}