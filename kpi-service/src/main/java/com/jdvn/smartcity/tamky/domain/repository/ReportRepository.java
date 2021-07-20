package com.jdvn.smartcity.tamky.domain.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

import com.jdvn.smartcity.tamky.domain.model.Report;

@RepositoryRestResource
public interface ReportRepository extends JpaRepository<Report, Long> {
}