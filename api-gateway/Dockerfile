FROM openjdk:8-jdk-alpine
MAINTAINER JungdoUIT-VN
EXPOSE 8080
ARG JAR_FILE=target/*.jar
ADD ${JAR_FILE} api-gateway-0.0.1-SNAPSHOT.jar
ENTRYPOINT ["java","-jar","/api-gateway-0.0.1-SNAPSHOT.jar"]
