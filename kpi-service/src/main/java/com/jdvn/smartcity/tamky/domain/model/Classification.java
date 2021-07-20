package com.jdvn.smartcity.tamky.domain.model;

import java.util.Set;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.MapsId;
import javax.persistence.OneToMany;
import javax.persistence.Table;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Entity
@Table(name = "classification") // This table stores a first level classifications for the KPIs.
public class Classification {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;
	
	private String name;
	
    @ManyToOne
    @MapsId("id")
    @JoinColumn(name = "categoryId")    
    private Category category;	
    
    
    @OneToMany(mappedBy = "classification")
    Set<ClassKpi> hasKpis;

}