package com.jdvn.smartcity.tamky.domain.model;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@Entity
@Table(name = "Unit")
public class Unit {

	@Id
	private int unitID;
	
	private String name; //name of the unit for human readability (“Watt”, “Degree Celsius”, “Watt hour”...)
	private String symbol; //symbol of the unit (e.g. W, ºC, Wh…)

}