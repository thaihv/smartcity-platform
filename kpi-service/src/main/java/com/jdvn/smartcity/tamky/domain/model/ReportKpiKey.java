package com.jdvn.smartcity.tamky.domain.model;

import java.io.Serializable;

import javax.persistence.Column;
import javax.persistence.Embeddable;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.NoArgsConstructor;

@Embeddable
@EqualsAndHashCode
@Data
@NoArgsConstructor
@AllArgsConstructor
public class ReportKpiKey implements Serializable {


	@Column(name = "kpi_id")
    Long kpiId;

    @Column(name = "report_id")
    Long reportId;

}