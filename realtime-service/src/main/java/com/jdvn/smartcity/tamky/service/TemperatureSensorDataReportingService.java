package com.jdvn.smartcity.tamky.service;

import com.jdvn.smartcity.tamky.domain.model.TemperatureSensorQueryResult;
import com.jdvn.smartcity.tamky.domain.repository.TemperatureSensorDataRepository;
import com.jdvn.smartcity.tamky.dto.response.TemperatureSensorDataResponse;
import com.jdvn.smartcity.tamky.dto.response.TemperatureSensorDataResponse.TemperatureSensorData;

import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

/**
 * The type Temperature sensor data reporting service.
 */
@Slf4j
@Service
public class TemperatureSensorDataReportingService {

    private final LoggedInUserService loggedInUserService;
    private final TemperatureSensorDataRepository repository;

    public TemperatureSensorDataReportingService(LoggedInUserService loggedInUserService,
                                                 TemperatureSensorDataRepository repository) {
        this.loggedInUserService = loggedInUserService;
        this.repository = repository;
    }

    /**
     * Generate report filtered with start and end time of logged in device.
     *
     * @param startTime the start unix timestamp.
     * @param endTime   the end unix timestamp.
     * @return the DTO of aggregated data.
     */
    public TemperatureSensorDataResponse getReport(long startTime, long endTime) {

        List<TemperatureSensorQueryResult> queryResults
                = repository.getTemperatures(loggedInUserService.getLoggedInDeviceId(), startTime, endTime);

        List<TemperatureSensorData> dataPoints = queryResults.stream()
                .map(data -> new TemperatureSensorData(data.getTime().getEpochSecond(), data.getTemperatureInFahrenheit()))
                .collect(Collectors.toList());

        return TemperatureSensorDataResponse.builder()
                .deviceId(loggedInUserService.getLoggedInDeviceId())
                .data(dataPoints)
                .build();

    }


}
