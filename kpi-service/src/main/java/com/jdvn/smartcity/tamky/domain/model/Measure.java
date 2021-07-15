package com.jdvn.smartcity.tamky.domain.model;

import java.sql.Date;

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
@Table(name = "measure")
//This table contains main KPI data.It is loaded with aggregated data from the different verticals
public class Measure {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private int id;

	@ManyToOne
	@JoinColumn(name = "kpiId")
	@EqualsAndHashCode.Exclude
	@ToString.Exclude
	private Kpi kpi;

	@NonNull
	private Date startDate;

	@NonNull
	private Date endDate;

	// The results of the aggregated data calculated from the StartDate to the
	// EndDate, or the specific value of the KPI in that period of time
	private float value;

	// The estimated value this measure should have, according to some simulations
	private float referenceValue;

	// Reference to the administrative unit where the measure has been taken
	private int countryId;

	// The identification of the specific structural element the measure is related
	// with (a specific building ID, or District ID…)
	private int structuralId;
}