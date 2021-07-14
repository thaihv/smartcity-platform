package com.jdvn.smartcity.tamky.domain.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

import com.jdvn.smartcity.tamky.domain.model.Measure;

@RepositoryRestResource
public interface MeasureRepository extends JpaRepository<Measure, Long> {
}