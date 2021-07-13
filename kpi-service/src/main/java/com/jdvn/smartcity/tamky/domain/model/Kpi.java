package com.jdvn.smartcity.tamky.domain.model;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.NoArgsConstructor;
import lombok.NonNull;
import lombok.ToString;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "kpi") // This table stores the general information for each KPI
public class Kpi {

//	public Kpi(String name, Unit unit) {
//		this.name = name;
//		this.unit = unit;
//	}

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;

	@NonNull
	private String name; // Descriptive human readable name of the KPI

	private String code; // Identifier in a human readable form

	private int frequencyInDays; // How often the KPI is calculated in days

	@ManyToOne
	@JoinColumn(name = "unitId")
	@EqualsAndHashCode.Exclude
	@ToString.Exclude
	private Unit unit; // Reference to the unit of the measurements of the KPI e.g. KWh/m²

	@Column(name = "structuralElement", length = 40, columnDefinition = "varchar(40) default 'District'") // Building, District,...
	private String structuralElement; // The structural element that the KPI is calculated for

}