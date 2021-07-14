package com.jdvn.smartcity.tamky.domain.model;

import java.util.Collection;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import javax.persistence.Table;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.NoArgsConstructor;
import lombok.ToString;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "unit")
public class Unit {
	
	public Unit(String name, String symbol) {
		this.name = name;
		this.symbol = symbol;
	}	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;

	private String name; // the unit for human readability e.g "Watt", "Degree Celsius", or "Watt hour"

	private String symbol; // symbol of the unit e.g. W, ºC, Wh

	@OneToMany(mappedBy = "unit", cascade = CascadeType.MERGE)
    @EqualsAndHashCode.Exclude 
    @ToString.Exclude 
	private Collection<Kpi> kpis;

}