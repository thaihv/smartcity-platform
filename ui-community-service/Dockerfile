FROM openjdk:8-jdk-alpine
MAINTAINER JungdoUIT-VN
ARG JAR_FILE=target/*.jar
ADD ${JAR_FILE} ui-community-service-0.0.1-SNAPSHOT.jar
ENTRYPOINT ["java","-jar","/ui-community-service-0.0.1-SNAPSHOT.jar"]
