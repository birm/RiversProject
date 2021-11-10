# Rivers Web Service

Java 17, Spring Boot 2.5.6.
Deps: Spring Web and MariaDB Driver

## Steps to build
1. `./mvnw install` to update the jar (this container does not autobuild the jar)
2. Re-build and re-run the service; e.g. `docker-compose build web` then `docker-compose up web`

## CONCERNS!

 - Building fails locally when I set the properties to the docker compose name. This is ANNOYING. I guess it's a test case failing, how do I get around this? (for now, using `./mvnw spring-boot:run` after `docker-compose up database` with local mount. this is bad.)
