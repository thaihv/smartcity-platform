package com.jdvn.smartcity.tamky.domain.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.NonNull;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "kpi")
public class Kpi {

	public Kpi(String name) {
		this.name = name;
	}

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;

	@NonNull
	private String name; // Descriptive human readable name of the KPI

	private String code; // Identifier in a human readable form

	private int frequencyInDays; // How often the KPI is calculated in days

	@NonNull
	private Long kpiTypeID;

	@NonNull
	private int unitID; // Reference to the unit of the measurements of the KPI e.g. KWh/m²

	@NonNull
	private String structuralElement; // The structural element that the KPI is calculated for Building, District,...

}