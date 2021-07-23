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
import lombok.EqualsAndHashCode;
import lombok.NoArgsConstructor;
import lombok.ToString;

@Data
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
    
    
    @OneToMany(mappedBy="classification")
    private Set<Category> categories;

}