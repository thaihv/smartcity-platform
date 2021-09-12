package com.jdvn.smartcity.tamky.api;

import com.jdvn.smartcity.tamky.dto.request.TemperatureSensorDataRequest;
import com.jdvn.smartcity.tamky.dto.response.DataCollectionStatusResponse;
import com.jdvn.smartcity.tamky.service.SensorDataCollectorService;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;


/**
 * This class provide API endpoints to collect temperature data from sensors.
 */
@RestController
@CrossOrigin
public class TemperatureCollectorAPI {

    private final SensorDataCollectorService temperatureSensorDataCollectorService;

    public TemperatureCollectorAPI(SensorDataCollectorService temperatureSensorDataCollectorService) {
        this.temperatureSensorDataCollectorService = temperatureSensorDataCollectorService;
    }

    /**
     * Collect temperature from sensors.
     *
     * @param dataRequest the temperature data request.
     * @return the response entity a boolean indicating request status and HTTP Status 201.
     */
    @PostMapping("/temperatures")
    public ResponseEntity<DataCollectionStatusResponse> collectTemperature(
            @RequestBody TemperatureSensorDataRequest dataRequest) {
        return new ResponseEntity(temperatureSensorDataCollectorService.collect(dataRequest), HttpStatus.CREATED);
    }

    /**
     * Collect temperatures in bulk from sensors in case device to offline.
     *
     * @param dataRequests list of temperature data request.
     * @return the response entity list of booleans indicating request status and HTTP Status 207.
     */
    @PostMapping("/temperatures/batch")
    public ResponseEntity<List<DataCollectionStatusResponse>> collectTemperatures(
            @RequestBody List<TemperatureSensorDataRequest> dataRequests) {
        return new ResponseEntity(temperatureSensorDataCollectorService.collect(dataRequests), HttpStatus.MULTI_STATUS);
    }
}
