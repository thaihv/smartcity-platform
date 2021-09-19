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
#### Run and setup Kafka, Mosquitto, influxDB images in Docker
- $ docker-compose -f kafka-mqtt-influxdb-compose.yml up
- In case you want to test send/receive a message using MQTT protocal, install mqtt-connector (already have done in docker compose file) and configure it via http:
   * curl -d @./*connect-mqtt-source.json* -H "Content-Type: application/json" -X POST http://localhost:8083/connectors 
#### Build
- Go to ./smartcity-platform folder, run $ mvn clean compile install
- For ui-service, this is a Angular app, you have to run it with Nodejs. Go to ./ui-service folder, run  $ npm install
#### Run
- Go to ./discovery-service/ 
   * Run $ mvn spring-boot:run
   * Open (http://localhost:8761) if run successfully, you will see list of services registered as Eureka clients
- Go to ./realtime-service/
   * Run $ mvn spring-boot:run 
   * To test this microservice use a command curl to send a HTTP get request to get sample temperature data points from database
     > curl -X GET http://localhost:8091/realtime/temperatures?startTime=1563142100&endTime=1757733151 \
  -H 'Content-Type: application/json' 
   * And response to get if run successfully
     > {\
   "deviceId":"e01a7bc8-ee40-48ba-80ee-f8acbaba5f14",\
   "data":[\
        {\
           "unixTimestamp":1563142700,\
           "temperatureInFahrenheit":20.0\
        },\
        {
           "unixTimestamp":1563142701,\
           "temperatureInFahrenheit":21.0\
        }\
   ]\
}
- Go to ./kpi-service/
   * Run $ mvn spring-boot:run Or $ java -Dfile.encoding=UTF-8 -jar kpi-service-0.0.1-SNAPSHOT.jar
   * Open (http://localhost:8090/kpi/list) to see the list of KPI for smart city 
- Go to ./ui-service/
   * Run $ ng serve --open
   * Open (http://localhost:4200) to view UI example of consuming microservices.
- Go to ./api-gateway/ 
   * Run $ mvn spring-boot:run 
   * Open (http://localhost:8080) and try calls to microservices if things run well. This is a main entry point for this boilerplate code
