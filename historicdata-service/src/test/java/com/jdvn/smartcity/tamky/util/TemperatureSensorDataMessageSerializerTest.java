package com.jdvn.smartcity.tamky.util;

import com.jdvn.smartcity.tamky.dto.message.TemperatureSensorDataMessage;
import com.jdvn.smartcity.tamky.util.TemperatureSensorDataMessageSerializer;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;

public class TemperatureSensorDataMessageSerializerTest {

    @Test
    public void shouldSerializeTemperatureSensorDataMessageObject() {

        // Given

        TemperatureSensorDataMessageSerializer serializer = new TemperatureSensorDataMessageSerializer();

        TemperatureSensorDataMessage message = TemperatureSensorDataMessage.builder()
                .deviceId("123")
                .temperatureInFahrenheit(10)
                .unixTimestamp(1563142799L)
                .build();

        // When
        byte[] serializedObject = serializer.serialize("any topic", message);

        // Then
        assertNotNull(serializedObject);
        assertEquals("{\"deviceId\":\"123\",\"temperatureInFahrenheit\":10.0,\"unixTimestamp\":1563142799}",
                new String(serializedObject));
    }
}
