package com.jdvn.smartcity.tamky.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import com.jdvn.smartcity.tamky.service.LoggedInUserService;

/**
 * Provides application related beans.
 */
@Configuration
public class AppConfig {

    /**
     * For assignment purpose, getLoggedInDeviceId() returns fixed device id.
     * In production, we will have security configured, there will be one-to-one relation between
     * logged in user and user/device Id
     */
    @Bean
    public LoggedInUserService loggedInUserService() {
        return () -> "e01a7bc8-ee40-48ba-80ee-f8acbaba5f14";
    }
}
