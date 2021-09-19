# A Smartcity Platform Using Microservices
**A boilerplate code  for smartcity-platform using for Tamky, Quang Nam. It includes:**
 1. A real time service for archiving data from sensors (MQTT) or applications (HTTP).The techstack is used:
    * Kafka
    * Mosquitto
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
## How to run
#### Run and setup Keycloak image in Docker
- $ docker-compose -f keycloak-postgres-compose.yml up
- Access to ***http://{your_keycloakserver}:8080/auth/***, login with username/password defined in *keycloak-postgres-compose.yml* file and click Manage/Import and choose *keycloak-data-export.json* file to import data settings for all clients (ui-service, kpi-service, realtime-service, api-gateway)
- Add more users, if needed
#### Run Kafka, Mosquitto, influxDB images in Docker
- $ docker-compose -f kafka-mqtt-influxdb-compose.yml up
#### Build
- Go to ./smartcity-platform folder, run $ mvn clean compile install
- For ui-service, this is a Angular app, you have to run it with Nodejs. Go to ./ui-service folder, run  $ npm install
#### Run
- Go to ./smartcity-platform/discovery-service/, run $ mvn spring-boot:run
- Go to ./smartcity-platform/api-gateway/, run $ mvn spring-boot:run
- Go to ./smartcity-platform/realtime-service/, run $ mvn spring-boot:run 
- Go to ./smartcity-platform/kpi-service/, run $ mvn spring-boot:run Or $ java -Dfile.encoding=UTF-8 -jar kpi-service-0.0.1-SNAPSHOT.jar
- Go to ./smartcity-platform/ui-service/, run $ ng serve --open

