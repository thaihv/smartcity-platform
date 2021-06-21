package com.jdvn.smartcity.tamky.exception;

/**
 * Exception class in case InfluxDB data could not be accessed.
 */
public class DataAccessException extends RuntimeException {

    public DataAccessException(String message) {
        super(message);
    }
}
