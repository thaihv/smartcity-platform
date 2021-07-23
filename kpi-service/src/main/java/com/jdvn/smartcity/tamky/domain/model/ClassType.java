package com.jdvn.smartcity.tamky.domain.model;

import java.util.Set;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import javax.persistence.Table;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Entity
@Table(name = "classtype") // This table stores a first level classifications for the KPIs.
public class ClassType {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;
	
	private String code; // Identifier in a human readable form	
	private String name;
	
    @OneToMany(mappedBy="classtype")
    private Set<Classification> classifications;

}