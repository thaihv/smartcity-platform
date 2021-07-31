package com.jdvn.smartcity.tamky.domain.model;

import java.util.Set;

import javax.persistence.CascadeType;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.OneToMany;
import javax.persistence.Table;

import com.fasterxml.jackson.annotation.JsonIgnore;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@Entity
@Table(name = "classification") // This table stores the second level classifications for the KPIs
public class Classification {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;

	private String code; // Identifier in a human readable form
	private String name;
	
    @ManyToOne
    @JoinColumn(name = "classtype_id") 
    private ClassType classtype;
    
    
    @OneToMany(fetch = FetchType.EAGER, mappedBy = "classification", cascade = CascadeType.ALL)
    @JsonIgnore
    private Set<Category> categories;

}