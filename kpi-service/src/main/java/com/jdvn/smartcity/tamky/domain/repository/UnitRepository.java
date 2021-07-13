package com.jdvn.smartcity.tamky.domain.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

import com.jdvn.smartcity.tamky.domain.model.Unit;

@RepositoryRestResource
public interface UnitRepository extends JpaRepository<Unit, Long> {
}