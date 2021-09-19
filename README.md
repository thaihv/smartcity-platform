# A Smartcity Platform Using Microservices
__A boilerplate code  for smartcity-platform.__ **It includes:**
 1. A real time service for archiving data from sensor.The techstack is used:
    * Kafka
    * Influxdb
    * Spring Boot 2
 1. A KPI service for creating and storing smart city Key Performance Indicators. The techstack is used:
    * Hibernate
    * PostgresSQL
    * Spring Boot 2
 1. Microservices using Sping Cloud for Discovery and Registrer
    * API gateway
    * Eureka
 1. Keycloak security framework for securing identity,Single Sign On for Users, Devices, Applications and Services  
 1. A UI microservice to illustrate consuming APIs from above microservices. It uses javascript libraries
    * Angular 12
    * keycloak-js
    * chart.js   
 
## Prerequisite
- JDK 1.8 
- Maven 3.6.x
- Docker (18.09.2)
- Docker Compose (1.23.2)
- Nodejs 14+
Run Keycloak, Kafka, influxDB image in Docker
- $ docker-compose -f keycloak-postgres-compose.yml up
- $ docker-compose -f kafka-mqtt-influxdb-compose.yml up


