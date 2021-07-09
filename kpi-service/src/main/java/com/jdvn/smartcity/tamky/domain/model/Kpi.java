package com.jdvn.smartcity.tamky.domain.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.NonNull;

@Data
@NoArgsConstructor
@Entity
@Table(name = "Kpi")
public class Kpi {

	public Kpi(String name) {
		this.name = name;
	}

	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
	private Long kpiID;

	@NonNull
	private String name; // Descriptive human readable name of the KPI

	@NonNull
	private String code; // Identifier of the KPI outside the system, in a human readable form

	private int frequencyInDays; // How often the KPI is calculated in days

	@NonNull
	private Long kpiTypeID;

	@NonNull
	private int unitID; // Reference to the unit of the measurements of the KPI e.g. KWh/m²

	@NonNull
	private String structuralElement; // The structural element that the KPI is calculated for Building, District,...

}