package com.jdvn.smartcity.tamky.domain.model;

import java.util.Set;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.OneToMany;
import javax.persistence.Table;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Entity
@Table(name = "category") // This table stores the third level classifications for the KPIs
public class Category {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;
	
	private String code; // Identifier in a human readable form
	private String name;

    
    @ManyToOne
    @JoinColumn(name = "classification_id") 
    private Classification classification;
    
    
    @OneToMany(mappedBy = "category")    
    Set<CategoryKpi> hasKpis;

}