package com.jdvn.smartcity.tamky.util;

import com.jdvn.smartcity.tamky.dto.message.TemperatureSensorDataMessage;

/**
 * Temperature sensor data Apache Kafka message deserializer class.
 */
public class TemperatureSensorDataMessageDeserializer extends SensorDataMessageDeserializer<TemperatureSensorDataMessage> {

    public TemperatureSensorDataMessageDeserializer() {
        super(TemperatureSensorDataMessage.class);
    }

}
