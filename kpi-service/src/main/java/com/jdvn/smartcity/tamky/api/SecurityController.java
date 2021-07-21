package com.jdvn.smartcity.tamky.api;

import java.security.interfaces.RSAPublicKey;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.auth0.jwk.Jwk;
import com.auth0.jwt.JWT;
import com.auth0.jwt.algorithms.Algorithm;
import com.auth0.jwt.interfaces.DecodedJWT;
import com.jdvn.smartcity.tamky.service.JwtService;
import com.jdvn.smartcity.tamky.service.KeycloakRestService;

@RestController
public class SecurityController {

    private Logger logger = LoggerFactory.getLogger(SecurityController.class);

    @Autowired
    private KeycloakRestService restService;

    @Autowired
    private JwtService jwtService;

    @SuppressWarnings({ "rawtypes", "unchecked", "serial" })
	@GetMapping("/user")
    public HashMap user(@RequestHeader("Authorization") String authHeader) {
        try {
            List<String> roles = restService.getRoles(authHeader);
            if(!roles.contains("user"))
                throw new Exception("not a user role");
            return new HashMap (){{
                put("role", "user");
            }};
        } catch (Exception e) {
            logger.error("exception : {} ", e.getMessage());
            return new HashMap (){{
                put("status", "forbidden");
            }};
        }
    }

    @GetMapping("/admin")
    public HashMap isAdminRole(@RequestHeader("Authorization") String authHeader) {
        try {
            DecodedJWT jwt = JWT.decode(authHeader.replace("Bearer", "").trim());

            // check JWT is valid
            Jwk jwk = jwtService.getJwk();
            Algorithm algorithm = Algorithm.RSA256((RSAPublicKey) jwk.getPublicKey(), null);

            algorithm.verify(jwt);

            // check JWT role is correct
            List<String> roles = ((List)jwt.getClaim("realm_access").asMap().get("roles"));
            if(!roles.contains("admin"))
                throw new Exception("not a admin role");

            // check JWT is still active
            Date expiryDate = jwt.getExpiresAt();
            if(expiryDate.before(new Date()))
                throw new Exception("token is expired");

            // all validation passed
            return new HashMap() {{
                put("role", "admin");
            }};
        } catch (Exception e) {
            logger.error("exception : {} ", e.getMessage());
            return new HashMap() {{
                put("status", "forbidden");
            }};
        }
    }

    @GetMapping("/valid")
    public HashMap tokenIsValid(@RequestHeader("Authorization") String authHeader) {
        try {
            restService.checkValidity(authHeader);
            return new HashMap (){{
                put("is_valid", "true");
            }};
        } catch (Exception e) {
            logger.error("token is not valid, exception : {} ", e.getMessage());
            return new HashMap (){{
                put("is_valid", "false");
            }};
        }
    }
    @GetMapping("/userinfo")
    public String getUserInfo(@RequestHeader("Authorization") String authHeader) {
    	return restService.getUserInfo(authHeader);
    }
    @PostMapping(value = "/login", produces = MediaType.APPLICATION_JSON_VALUE)
    public String login(String username, String password) {
        return restService.login(username, password);
    }

    @PostMapping(value = "/logout", produces = MediaType.APPLICATION_JSON_VALUE)
    public Map logout(@RequestParam(value = "refresh_token", name = "refresh_token") String refreshToken) {
        try {
            restService.logout(refreshToken);
            return new HashMap (){{
                put("logout", "true");
            }};
        } catch (Exception e) {
            logger.error("unable to logout, exception : {} ", e.getMessage());
            return new HashMap (){{
                put("logout", "false");
            }};
        }
    }
}