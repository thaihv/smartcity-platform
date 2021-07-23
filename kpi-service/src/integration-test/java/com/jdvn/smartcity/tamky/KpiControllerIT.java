package com.jdvn.smartcity.tamky;

import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.context.TestPropertySource;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;
import org.springframework.test.web.servlet.result.MockMvcResultHandlers;
import org.springframework.test.web.servlet.result.MockMvcResultMatchers;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;
import org.springframework.web.context.WebApplicationContext;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultHandlers.print;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@RunWith(SpringRunner.class)
@SpringBootTest(classes = {KpiServiceApplication.class})
@AutoConfigureMockMvc
@TestPropertySource(locations = "classpath:application-integrationtest.yml")
public class KpiControllerIT {

    @Autowired
    private WebApplicationContext context;
    
	@Autowired
	private MockMvc mockMvc;
	
    @Before
    public void setup() {
        mockMvc = MockMvcBuilders.webAppContextSetup(context)   
        		   .build(); 
    }
    
	@Test
	public void testSayHi() throws Exception {
		this.mockMvc.perform(MockMvcRequestBuilders.get("/kpi-all"))
				.andExpect(MockMvcResultMatchers.status().isOk())
//				.andExpect(content().contentType(MediaType.APPLICATION_JSON))
//				.andExpect(MockMvcResultMatchers.view().name("hello"))
				.andDo(MockMvcResultHandlers.print());
	}
}