package com.jdvn.smartcity.tamky.domain.model;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@Entity
@Table(name = "ReportKpi")
public class ReportKpi {

	@Id
	private Long reportID;
	
	private Long kpiID;

}