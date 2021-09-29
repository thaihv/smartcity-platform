package com.jdvn.smartcity.tamky.uicommunityservice;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@EnableDiscoveryClient
@SpringBootApplication
@RestController
public class UiCommunityServiceApplication {

	@RequestMapping("/test")
	public String greet() {
		return "Welcome!";
	}
	public static void main(String[] args) {
		SpringApplication.run(UiCommunityServiceApplication.class, args);
	}

}
