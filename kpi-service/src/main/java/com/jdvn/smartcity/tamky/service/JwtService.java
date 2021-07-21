package com.jdvn.smartcity.tamky.service;

import java.net.URL;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.stereotype.Service;

import com.auth0.jwk.Jwk;
import com.auth0.jwk.UrlJwkProvider;

@Service
public class JwtService {

    @Value("${spring.security.oauth2.client.provider.keycloak.jwk-set-uri}")
    private String jwksUrl;

    @Value("${spring.security.oauth2.client.provider.keycloak.certs-id}")
    private String certsId;

    @Cacheable(value = "jwkCache")
    public Jwk getJwk() throws Exception {
        return new UrlJwkProvider(new URL(jwksUrl)).get(certsId);
    }
}