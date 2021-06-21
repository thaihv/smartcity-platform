package com.jdvn.smartcity.tamky;

import com.netflix.hystrix.contrib.javanica.annotation.HystrixCommand;
import feign.RequestInterceptor;
import lombok.Data;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.web.servlet.FilterRegistrationBean;
import org.springframework.cloud.client.circuitbreaker.EnableCircuitBreaker;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.cloud.netflix.zuul.EnableZuulProxy;
import org.springframework.cloud.openfeign.EnableFeignClients;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.Ordered;
import org.springframework.hateoas.CollectionModel;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.oauth2.client.OAuth2AuthorizedClientService;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.cors.CorsConfiguration;
import org.springframework.web.cors.UrlBasedCorsConfigurationSource;
import org.springframework.web.filter.CorsFilter;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.stream.Collectors;

@EnableFeignClients
@EnableCircuitBreaker
@EnableDiscoveryClient
@EnableZuulProxy
@SpringBootApplication
public class ApiGatewayApplication {

    public static void main(String[] args) {
        SpringApplication.run(ApiGatewayApplication.class, args);
    }

    @Configuration
    static class OktaOAuth2WebSecurityConfigurerAdapter extends WebSecurityConfigurerAdapter {

        @Override
        protected void configure(HttpSecurity http) throws Exception {
            // @formatter:off
            http
                .authorizeRequests().anyRequest().authenticated()
                    .and()
                .oauth2Login()
                    .and()
                .oauth2ResourceServer().jwt();
            // @formatter:on
        }
    }

    @Bean
    public FilterRegistrationBean<CorsFilter> simpleCorsFilter() {
        UrlBasedCorsConfigurationSource source = new UrlBasedCorsConfigurationSource();
        CorsConfiguration config = new CorsConfiguration();
        config.setAllowCredentials(true);
        config.setAllowedOrigins(Collections.singletonList("*"));
        config.setAllowedMethods(Collections.singletonList("*"));
        config.setAllowedHeaders(Collections.singletonList("*"));
        source.registerCorsConfiguration("/**", config);
        FilterRegistrationBean<CorsFilter> bean = new FilterRegistrationBean<>(new CorsFilter(source));
        bean.setOrder(Ordered.HIGHEST_PRECEDENCE);
        return bean;
    }

    @Bean
    public RequestInterceptor getUserFeignClientInterceptor(OAuth2AuthorizedClientService clientService) {
        return new UserFeignClientInterceptor(clientService);
    }

    @Bean
    public AuthorizationHeaderFilter authHeaderFilter(OAuth2AuthorizedClientService clientService) {
        return new AuthorizationHeaderFilter(clientService);
    }
}

@Data
class Kpi {
    private String name;
}

@FeignClient("kpi-service")
interface KpiClient {

    @GetMapping("/kpis")
    @CrossOrigin
    CollectionModel<Kpi> readKpis();
}

@RestController
class StandardKpiController {

    private final KpiClient kpiClient;

    public StandardKpiController(KpiClient kpiClient) {
        this.kpiClient = kpiClient;
    }

    private Collection<Kpi> fallback() {
        return new ArrayList<>();
    }

    @GetMapping("/good-kpis")
    @CrossOrigin
    @HystrixCommand(fallbackMethod = "fallback")
    public Collection<Kpi> goodKpis() {
        return kpiClient.readKpis()
                .getContent()
                .stream()
                .filter(this::isGoodKpi)
                .collect(Collectors.toList());
    }

    private boolean isGoodKpi(Kpi kpi) {
        return !kpi.getName().equals("Air Quality") &&
                !kpi.getName().equals("Water and Sanitation") &&
                !kpi.getName().equals("Drainage") &&
                !kpi.getName().equals("Food Security");
    }
}
