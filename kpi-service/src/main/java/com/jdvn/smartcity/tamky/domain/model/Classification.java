package com.jdvn.smartcity.tamky.domain.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Entity
@Table(name = "Classification") // This table stores a first level classifications for the KPIs.
public class Classification {

	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
	private Long classID;
	private String name;
	private Long classTypeID;

}