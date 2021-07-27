package com.jdvn.smartcity.tamky.domain.model;

import java.io.Serializable;

import javax.persistence.Column;
import javax.persistence.Embeddable;

import lombok.AllArgsConstructor;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;


@Getter 
@Setter
@Embeddable
@EqualsAndHashCode
@NoArgsConstructor
@AllArgsConstructor
public class ReportKpiKey implements Serializable {


	@Column(name = "kpi_id")
    Long kpiId;

    @Column(name = "report_id")
    Long reportId;

}