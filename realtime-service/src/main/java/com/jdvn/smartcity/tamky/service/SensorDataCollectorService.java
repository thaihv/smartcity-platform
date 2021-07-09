package com.jdvn.smartcity.tamky.service;

import java.util.List;

import com.jdvn.smartcity.tamky.dto.response.DataCollectionStatusResponse;

/**
 * Generic collector service APIs.
 */
public interface SensorDataCollectorService<Data> {

    DataCollectionStatusResponse collect(Data data);

    List<DataCollectionStatusResponse> collect(List<Data> dataList);
}
