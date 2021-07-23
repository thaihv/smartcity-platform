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
@Table(name = "categorykpi")
public class CategoryKpi {

	@EmbeddedId
	CategoryKpiKey id;

	@ManyToOne
	@MapsId("categoryId")
	@JoinColumn(name = "category_id")
	Category category;

	@ManyToOne
	@MapsId("kpiId")
	@JoinColumn(name = "kpi_id")
	Kpi kpi;

}