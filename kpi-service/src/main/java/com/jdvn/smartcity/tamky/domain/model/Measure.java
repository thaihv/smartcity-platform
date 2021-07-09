package com.jdvn.smartcity.tamky.domain.model;

import java.sql.Date;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@Entity
@Table(name = "measure")
public class Measure {

	@Id
	private int measureID;

	private int kpiID;
	private Date startDate;
	private Date endDate;
	private float value; // The results of the aggregated data calculated from the StartDate to the
							// EndDate, or the specific value of the KPI in that period of time
	private float referenceValue; // The estimated value this measure should have, according to some simulations
	private int countryID; // Reference to the country where the measure has been taken
	private int structuralID; // The identification of the specific structural element the measure is related
								// with (a specific building ID, or District ID…)
}