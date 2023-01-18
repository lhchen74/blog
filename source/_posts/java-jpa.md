---
title: Java Jpa
tags: java
date: 2019-11-2
---

### pom.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.9.RELEASE</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.example</groupId>
    <artifactId>jpaorm</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>jpaorm</name>
    <description>Demo project for Spring Boot</description>

    <properties>
        <java.version>1.8</java.version>
    </properties>

    <dependencies>
        <!-- jpa -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
				<!-- mysql -->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <scope>runtime</scope>
        </dependency>
        <!-- lombok 简化类定义, idea 中使用需要安装 lombok plugin -->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <optional>true</optional>
        </dependency>
        <!-- springboot -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>

</project>

```

### application.yaml

```yaml
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/jpaormtest?serverTimezone=UTC&useUnicode=true&characterEncoding=utf-8
    username: root
    password: root
  jpa:
    generate-ddl: true
```

### User

```java
package com.example.jpaorm;

import lombok.Data;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
@Data
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    int id;
    String name;
    int age;
}
```

### UserRep

```java
package com.example.jpaorm;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface UserRep extends JpaRepository<User, Integer> {
    List<User> findByName(String name);

    @Query(value = "select * from user where name=?", nativeQuery = true)
    List<User> findByNameNativeQuery(String name);
}
```

### JpaormApplication

```java
package com.example.jpaorm;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.util.List;

@SpringBootApplication
public class JpaormApplication implements CommandLineRunner {

    public static void main(String[] args) {
        SpringApplication.run(JpaormApplication.class, args);
    }

    @Autowired
    UserRep userRep;

    @Override
    public void run(String... args) throws Exception {
        User user = new User();
        user.setName("babb");
        user.setAge(11);
        userRep.save(user);

        List<User> users = userRep.findByName("babb");
        System.out.println(users);

        List<User> users2 = userRep.findByNameNativeQuery("babb");
        System.out.println(users2);
    }

}
```

