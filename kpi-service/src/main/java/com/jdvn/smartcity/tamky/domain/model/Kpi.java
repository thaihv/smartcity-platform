package com.jdvn.smartcity.tamky.domain.model;

import java.util.Collection;
import java.util.Set;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.OneToMany;
import javax.persistence.Table;

import com.fasterxml.jackson.annotation.JsonBackReference;
import com.fasterxml.jackson.annotation.JsonIgnore;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.NonNull;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "kpi") // This table stores the general information for each KPI
public class Kpi {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;

	private String code; // Identifier in a human readable form

	@NonNull
	private String name; // Descriptive human readable name of the KPI

	private int frequencyInDays; // How often the KPI is calculated in days

	private String description;

	@ManyToOne
	@JoinColumn(name = "unitId")
	@JsonBackReference
	private Unit unit; // Reference to the unit of the measurements of the KPI e.g. KWh/m²

	@Column(name = "structural_element", length = 40, columnDefinition = "varchar(40) default 'District'") // Building,
																											// District,...
	private String structuralElement; // The structural element that the KPI is calculated for

	@OneToMany(fetch = FetchType.EAGER, mappedBy = "kpi", cascade = CascadeType.ALL)
	@JsonIgnore
	private Collection<Measure> measures;

	@OneToMany(mappedBy = "kpi",cascade = CascadeType.ALL)
	@JsonIgnore
	Set<CategoryKpi> belongCategory;

	@OneToMany(fetch = FetchType.EAGER, mappedBy = "kpi", cascade = CascadeType.ALL)
	@JsonIgnore
	Set<ReportKpi> belongReport;

}