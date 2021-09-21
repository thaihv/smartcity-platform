FROM openjdk:8-jdk-alpine
MAINTAINER JungdoVN
EXPOSE 8080
ARG JAR_FILE=target/api-gateway-0.0.1-SNAPSHOT.jar
ADD ${JAR_FILE} app.jar
ENTRYPOINT ["java","-jar","/app.jar"]