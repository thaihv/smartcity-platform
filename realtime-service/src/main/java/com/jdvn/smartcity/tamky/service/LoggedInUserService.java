package com.jdvn.smartcity.tamky.service;

/**
 * Provide logged in user / device info.
 */
public interface LoggedInUserService {

    /**
     * Return UUID of authenticated user / device.
     *
     * @return uuid of device.
     */
    String getLoggedInDeviceId();
}
