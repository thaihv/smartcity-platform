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
@Table(name = "ClassificationType") // This table stores the second level classifications for the KPIs
public class ClassificationType {

	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
	private Long classTypeID;
	private String name;

}