package com.jdvn.smartcity.tamky.domain.model;

import javax.persistence.EmbeddedId;
import javax.persistence.Entity;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.MapsId;
import javax.persistence.Table;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter 
@Setter
@NoArgsConstructor
@Entity
@Table(name = "report_kpi")
public class ReportKpi {

	@EmbeddedId
	ReportKpiKey id;

	@ManyToOne
	@MapsId("reportId")
	@JoinColumn(name = "report_id")
	Report report;

	@ManyToOne
	@MapsId("kpiId")
	@JoinColumn(name = "kpi_id")
	Kpi kpi;

}