---
title: Java 11 HttpClient Examples
tags: java
date: 2019-12-20
---

> 转载: [Java 11 HttpClient Examples – Mkyong.com](https://www.mkyong.com/java/java-11-httpclient-examples/)

This article shows you how to use the new [Java 11 HttpClient](https://docs.oracle.com/en/java/javase/11/docs/api/java.net.http/java/net/http/HttpClient.html) APIs to send HTTP GET/POST requests, and some frequent used examples.

*P.S Tested with Java 11*

## 1. Synchronous Get Request

Java11HttpClientExample1.java

```java
package com.mkyong.http;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpHeaders;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class Java11HttpClientExample1 {

    // default
    // private final HttpClient httpClient = HttpClient.newHttpClient();

    private final HttpClient httpClient = HttpClient.newBuilder()
            .version(HttpClient.Version.HTTP_2)
            .build();

    public static void main(String[] args) throws IOException, InterruptedException {
        Java11HttpClientExample1 obj = new Java11HttpClientExample1();
        obj.sendGET();
    }

    private void sendGET() throws IOException, InterruptedException {

        HttpRequest request = HttpRequest.newBuilder()
                .GET()
                .uri(URI.create("https://httpbin.org/get"))
                .setHeader("User-Agent", "Java 11 HttpClient Bot") // add request header
                .build();


        HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
        // print response headers
        HttpHeaders headers = response.headers();
        headers.map().forEach((k, v) -> System.out.println(k + ":" + v));

        // print status code
        System.out.println(response.statusCode());

        // print response body
        System.out.println(response.body());

    }

}
```



## 2. Asynchronous Get Request

2.1 `httpClient.sendAsync()` to send a request asynchronous, it will return a `CompletableFuture`

Java11HttpClientExample2.java

```java
package com.mkyong.http;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.TimeUnit;

public class Java11HttpClientExample2 {

    private final HttpClient httpClient = HttpClient.newBuilder()
            .version(HttpClient.Version.HTTP_2)
            .build();

    public static void main(String[] args) throws Exception {
        Java11HttpClientExample2 obj = new Java11HttpClientExample2();
        String result = obj.sendGET();
        System.out.println(result);
    }

    private String sendGET() throws Exception {

        HttpRequest request = HttpRequest.newBuilder()
                .GET()
                .uri(URI.create("https://httpbin.org/get"))
                .setHeader("User-Agent", "Java 11 HttpClient Bot")
                .build();
        
        CompletableFuture<HttpResponse<String>> response =
                httpClient.sendAsync(request, HttpResponse.BodyHandlers.ofString());

        return response.thenApply(HttpResponse::body).get(5, TimeUnit.SECONDS);

    }

}
```

## 3. Concurrent Requests

3.1 Add a custom executor.

```java
private final ExecutorService executorService = Executors.newFixedThreadPool(5);

private final HttpClient httpClient = HttpClient.newBuilder()
    .executor(executorService)
    .version(HttpClient.Version.HTTP_2)
    .build();
```

3.2 Send multiple concurrent requests asynchronous.

Java11HttpClientExample3.java

```java
package com.mkyong.java11;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;

public class Java11HttpClientExample3 {

	// optional
    private final ExecutorService executorService = Executors.newFixedThreadPool(5);

    private final HttpClient httpClient = HttpClient.newBuilder()
            .executor(executorService)
            .version(HttpClient.Version.HTTP_2)
            .build();

    public static void main(String[] args) throws Exception {
        Java11HttpClientExample3 obj = new Java11HttpClientExample3();
        obj.sendGET();
    }

    private void sendGET() throws Exception {

        List<URI> targets = Arrays.asList(
                new URI("https://httpbin.org/get?namr=mkyong1"),
                new URI("https://httpbin.org/get?name=mkyong2"),
                new URI("https://httpbin.org/get?namr=mkyong3"),
                new URI("https://httpbin.org/get?namr=mkyong4"),
                new URI("https://httpbin.org/get?namr=mkyong5"));

        List<CompletableFuture<String>> result = targets.stream()
                .map(url -> httpClient.sendAsync(
                        HttpRequest.newBuilder(url)
                                .GET()
                                .setHeader("User-Agent", "Java 11 HttpClient Bot")
                                .build(),
                        HttpResponse.BodyHandlers.ofString())
                        .thenApply(response -> response.body()))
                .collect(Collectors.toList());

        for (CompletableFuture<String> future : result) {
            System.out.println(future.get());
        }
        
    }

}
```

## 4. POST Form Parameters

4.1 Java 11 `HttpClient` didn’t provide API for the form data, we have to construct it manually.

Java11HttpClientExample4.java

```java
package com.mkyong.http;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;

public class Java11HttpClientExample4 {

    private final HttpClient httpClient = HttpClient.newBuilder()
            .version(HttpClient.Version.HTTP_2)
            .build();

    public static void main(String[] args) throws IOException, InterruptedException {
        Java11HttpClientExample4 obj = new Java11HttpClientExample4();
        obj.sendPOST();
    }

	// Sample: 'password=123&custom=secret&username=abc&ts=1570704369823'
    public static HttpRequest.BodyPublisher ofFormData(Map<Object, Object> data) {
        var builder = new StringBuilder();
        for (Map.Entry<Object, Object> entry : data.entrySet()) {
            if (builder.length() > 0) {
                builder.append("&");
            }
            builder.append(URLEncoder.encode(entry.getKey().toString(), StandardCharsets.UTF_8));
            builder.append("=");
            builder.append(URLEncoder.encode(entry.getValue().toString(), StandardCharsets.UTF_8));
        }
        return HttpRequest.BodyPublishers.ofString(builder.toString());
    }

    private void sendPOST() throws IOException, InterruptedException {

        // form parameters
        Map<Object, Object> data = new HashMap<>();
        data.put("username", "abc");
        data.put("password", "123");
        data.put("custom", "secret");
        data.put("ts", System.currentTimeMillis());

        HttpRequest request = HttpRequest.newBuilder()
                .POST(ofFormData(data))
                .uri(URI.create("https://httpbin.org/post"))
                .setHeader("User-Agent", "Java 11 HttpClient Bot") // add request header
                .header("Content-Type", "application/x-www-form-urlencoded")
                .build();

        HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());

        // print status code
        System.out.println(response.statusCode());

        // print response body
        System.out.println(response.body());

    }

}
```

## 5. POST JSON

Java11HttpClientExample5.java

```java
package com.mkyong.http;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;

public class Java11HttpClientExample5 {

    private final HttpClient httpClient = HttpClient.newBuilder()
            .version(HttpClient.Version.HTTP_2)
            .build();

    public static void main(String[] args) throws IOException, InterruptedException {
        Java11HttpClientExample5 obj = new Java11HttpClientExample5();
        obj.sendPOST();
    }

    private void sendPOST() throws IOException, InterruptedException {

        // json formatted data
        String json = new StringBuilder()
                .append("{")
                .append("\"name\":\"mkyong\",")
                .append("\"notes\":\"hello\"")
                .append("}").toString();

		// add json header
        HttpRequest request = HttpRequest.newBuilder()
                .POST(HttpRequest.BodyPublishers.ofString(json))
                .uri(URI.create("https://httpbin.org/post"))
                .setHeader("User-Agent", "Java 11 HttpClient Bot") // add request header
                .header("Content-Type", "application/json")
                .build();

        HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());

        // print status code
        System.out.println(response.statusCode());

        // print response body
        System.out.println(response.body());

    }

}
```

## 6. Authentication

6.1 Start a simple [Spring Security WebApp provides HTTP basic authentication](https://www.mkyong.com/spring-boot/spring-rest-spring-security-example/), and test it with the new Java 11 `HttpClient` APIs

Java11HttpClientExample6.java

```java
package com.mkyong.http;

import java.io.IOException;
import java.net.Authenticator;
import java.net.PasswordAuthentication;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class Java11HttpClientExample6 {

    private final HttpClient httpClient = HttpClient.newBuilder()
            .authenticator(new Authenticator() {
                @Override
                protected PasswordAuthentication getPasswordAuthentication() {
                    return new PasswordAuthentication(
                            "user",
                            "password".toCharArray());
                }
            })
            .build();

    public static void main(String[] args) throws IOException, InterruptedException {
        Java11HttpClientExample6 obj = new Java11HttpClientExample6();
        obj.sendGET();
    }

    private void sendGET() throws IOException, InterruptedException {

        HttpRequest request = HttpRequest.newBuilder()
                .GET()
                .uri(URI.create("http://localhost:8080/books"))
                .setHeader("User-Agent", "Java 11 HttpClient Bot") // add request header
                .build();

        HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());

        // print status code
        System.out.println(response.statusCode());

        // print response body
        System.out.println(response.body());

    }

}
```

## 7. FAQs

7.1 Disabled Redirect.

```java
	private final HttpClient httpClient = HttpClient.newBuilder()
            .followRedirects(HttpClient.Redirect.NEVER)
            .build();
```

Read this [HttpClient.Redirect JavaDoc](https://docs.oracle.com/en/java/javase/11/docs/api/java.net.http/java/net/http/HttpClient.Redirect.html)

7.2 Timeout, 5 seconds.

```java
	private final HttpClient httpClient = HttpClient.newBuilder()
            .connectTimeout(Duration.ofSeconds(5))
            .build();
```

7.3 Set a Proxy.

```java
	private final HttpClient httpClient = HttpClient.newBuilder()
            .proxy(ProxySelector.of(new InetSocketAddress("your-company-proxy.com", 8080)))
            .build();
```