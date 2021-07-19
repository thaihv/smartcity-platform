package com.jdvn.smartcity.tamky.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

@Configuration
public class OAuth2ResourceServerConfig extends WebSecurityConfigurerAdapter {

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
		        .csrf().disable()
		        .authorizeRequests()
                .anyRequest().authenticated()
                .and()
                .oauth2Login()
                .and()
                .oauth2ResourceServer()
                .jwt();
    }
}