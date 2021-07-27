package com.jdvn.smartcity.tamky.domain.model;

import java.io.Serializable;

import javax.persistence.Column;
import javax.persistence.Embeddable;

import lombok.AllArgsConstructor;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Embeddable
@EqualsAndHashCode
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class CategoryKpiKey implements Serializable {

	@Column(name = "kpi_id")
	Long kpiId;

	@Column(name = "category_id")
	Long categoryId;

}