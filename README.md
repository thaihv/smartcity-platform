"# smartcity-platform" 
A boilerplate code  for smartcity-platform. 
It includes:
 - A real time service for archiving data from sensor:
   Kafka
   Influxdb
   Spring Boot 2
 - A KPI service for creating and storing smart city Key Performance Indicators:
   Hibernate
   PostgresSQL database
   Springboot
 - Micro-services using Sping Cloud for Discovery and Registrer and API gateway, Circuit breaker
 - Keycloak security framework for securing identity,Single Sign On for Users, Devices, Applications and Services  
 - A UI microservice to illustrate consuming APIs from above microservices using Angular 11   
 
Prerequisite
JDK 1.8 
Maven 3.6.x
Docker (18.09.2)
Docker Compose (1.23.2)
Nodejs 14+
Run Keycloak, Kafka, influxDB image in Docker
$ docker-compose -f keycloak-postgres-compose.yml up
$ docker-compose -f kafka-mqtt-influxdb-compose.yml up


