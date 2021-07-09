package com.jdvn.smartcity.tamky.dto.request;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * DTO class to read JSON HTTP request body.
 */
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class TemperatureSensorDataRequest {

    private double temperatureInFahrenheit;

    /**
     * In case device go offline and send request once online.
     */
    private long unixTimestamp;
}
