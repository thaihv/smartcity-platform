package com.jdvn.smartcity.tamky.exception;

import org.springframework.web.bind.annotation.ControllerAdvice;

import lombok.extern.slf4j.Slf4j;

@Slf4j
@ControllerAdvice
public class ApplicationExceptionHandler extends BaseExceptionHandler {

    public ApplicationExceptionHandler() {
        super(log);
    }

}