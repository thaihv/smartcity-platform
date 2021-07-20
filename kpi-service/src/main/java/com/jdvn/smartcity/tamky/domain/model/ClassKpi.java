package com.jdvn.smartcity.tamky.domain.model;

import javax.persistence.EmbeddedId;
import javax.persistence.Entity;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.MapsId;
import javax.persistence.Table;

import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@Entity
@Table(name = "classkpi")
public class ClassKpi {

	@EmbeddedId
	ClassKpiKey id;

	@ManyToOne
	@MapsId("classificationId")
	@JoinColumn(name = "classification_id")
	Classification classification;

	@ManyToOne
	@MapsId("kpiId")
	@JoinColumn(name = "kpi_id")
	Kpi kpi;

}