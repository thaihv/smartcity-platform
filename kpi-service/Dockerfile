FROM openjdk:8-jdk-alpine
MAINTAINER JungdoUIT-VN
ARG JAR_FILE=target/*.jar
ADD ${JAR_FILE} kpi-service-0.0.1-SNAPSHOT.jar
ENTRYPOINT ["java","-jar","/kpi-service-0.0.1-SNAPSHOT.jar"]
