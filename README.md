# A Smartcity Platform using microservices
**This code is used as the boilerplate code for Smart City platform project. It includes microservices:**
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
    * Sring Cloud Gateway
    * Netflix Eureka
 1. Keycloak security framework for securing identity,Single Sign On for Users, Devices, Applications and Services  
 1. A UI microservice to illustrate consuming APIs from above microservices. It is an angular application wrapped by spring boot to make it as a Euraka client. It uses javascript libraries
    * Angular 12
    * keycloak-js
    * chart.js   
 
## Prerequisite
#### Infrastructure components
- Ubuntu (tested v20.04) 
- Docker (18.09.2)
- Docker Compose (1.23.2) 

#### Development
- JDK 1.8 
- Maven 3.6.x
- Nodejs 14+

## How to run
### Install infrastructure components in Docker
These docker compose files should be run and installed in a seperate server or an instance cloud of your development infrastructure 
#### Run and setup Keycloak image in Docker
- $ docker-compose -f keycloak-postgres-compose.yml up
- Access to ***http://{your_keycloakserver}:8080/auth/***, login with username/password is defined in *keycloak-postgres-compose.yml* file and click Manage/Import and choose *keycloak-data-export.json* file to import data settings for all clients (**ui-service**, **kpi-service**, **realtime-service**, **api-gateway**)
- Add more users, if needed
#### Run and setup Kafka, Mosquitto, influxDB images in Docker
- $ docker-compose -f kafka-mqtt-influxdb-compose.yml up
- In case you want to test send/receive a message using MQTT protocal, install mqtt-connector image (already have done in docker compose file) then download [MQTT connector](https://www.confluent.io/hub/) from the Confluent hub and unzip all *./lib/.jar* to *./tmp/custom/jars*. Restart mqtt-connector image and configure it via http by using a curl command:
   * curl -d @./*connect-mqtt-source.json* -H "Content-Type: application/json" -X POST http://{your_mqttserver}:8083/connectors 

### Build and Run code 
#### Build
- Go to ./smartcity-platform folder, run $ mvn clean compile install
- For ui-service, this is a Angular app integrated with Spring Boot, in case you want to run it with Nodejs. Go to ././src/main/resources/frontend/ui-service folder, run  $ npm install
#### Run
- Go to ./discovery-service/ 
   * Run $ mvn spring-boot:run
   * Open (http://localhost:8761) if run successfully, you will see list of services registered as Eureka clients
- Go to ./realtime-service/
   * Run $ mvn spring-boot:run 
   * To test this microservice use a command curl (or Postman application) to send a HTTP get request to get sample temperature data points from database
     > curl -X GET http://localhost:8091/realtime/temperatures?startTime=1632044000&endTime=1632044042  \
  -H 'Content-Type: application/json' 
   * And response to get if run successfully
     > {\
   "deviceId":"da153676-b1ba-4225-b785-a86361165890",\
   "data":[\
       &nbsp;&nbsp; {\
          &nbsp;&nbsp;&nbsp;&nbsp; "unixTimestamp":1632044000,\
          &nbsp;&nbsp;&nbsp;&nbsp; "temperatureInFahrenheit":76.0\
       &nbsp;&nbsp; },\
       &nbsp;&nbsp; {\
          &nbsp;&nbsp;&nbsp;&nbsp; "unixTimestamp":1632044001,\
          &nbsp;&nbsp;&nbsp;&nbsp; "temperatureInFahrenheit":98.0\
      &nbsp;&nbsp;  }\
   &nbsp;]\
}
- Go to ./kpi-service/
   * Run $ mvn spring-boot:run Or $ java -Dfile.encoding=UTF-8 -jar kpi-service-0.0.1-SNAPSHOT.jar
   * Open (http://localhost:8090/kpi/list) to see the list of KPI for smart city 
- Go to ./ui-service/
   * Run $ mvn spring-boot:run
   * Open (http://localhost:8081/mytamky/) to view UI example of consuming microservices.
- Go to ./api-gateway/ 
   * Run $ mvn spring-boot:run 
   * Open (http://localhost:8080/mytamky/) and try calls to microservices if things run well. This is a main entry point for this boilerplate code. Every API calls will go to port 8080.
- Optionally, In order to test the ui service that is not needed to access behind the Gateway and user can login to system every time she wants, go to ./ui-community-service/ 
   * Run $ mvn spring-boot:run 
   * Open (http://localhost:18081/community/) to test API calls with/without loggedin!
