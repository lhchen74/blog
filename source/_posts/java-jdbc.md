---
title: Java	Jdbc
tags: java
date: 2019-03-22
---

### ojdbc.jar install

由于 ojdbc 在 maven 中央仓库中不存在，需要手动安装到本地 maven 仓库

1. 在 oracle 官网或者 oracle 安装目录的 jdbc\lib 下找到 ojdbc 相关 jar 文件

2. 执行 mvn 命令
   `mvn install:install-file -DgroupId=com.oracle -DartifactId=ojdbc14 -Dversion=11.2.0 -Dpackaging=jar -Dfile=ojdbc14.jar`
   
   如果出现错误: The goal you specified requires a project to execute but there is no POM in this directory (D:\DEV10G\jdbc\lib). Please verify you invoked Maven from the correct directory.
   
   为参数添加 ""
   
   `mvn install:install-file "-DgroupId=com.oracle" "-DartifactId=ojdbc14" "-Dversion=11.2.0" "-Dpackaging=jar" "-Dfile=ojdbc14.jar"`
   
3. 添加依赖

   ```xml
   <dependency>
       <groupId>com.oracle</groupId>
       <artifactId>ojdbc14</artifactId>
       <version>11.2.0</version>
   </dependency>
   ```

### jdbc operation

```java
package com.jbn;

import java.sql.*;

class JdbcOperation {
    private static Connection conn = null; // 数据库连接对象

    private static String driver = "oracle.jdbc.driver.OracleDriver"; // 驱动

    private static String url = "jdbc:oracle:thin:@//ip:port/instance"; // 连接字符串

    private static String username = "username"; // 用户名

    private static String password = "password"; // 密码

    // 获得连接对象
    private static synchronized Connection getConn() {
        if (conn == null) {
            try {
                Class.forName(driver);
                conn = DriverManager.getConnection(url, username, password);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        return conn;
    }

    // 执行查询语句
    public void query(String sql, boolean isSelect) throws SQLException {
        PreparedStatement pstmt;
        try {
            pstmt = getConn().prepareStatement(sql);
            ResultSet rs = pstmt.executeQuery();
            while (rs.next()) {
                String name = rs.getString("name");
                System.out.println(name);
            }
            rs.close();
            pstmt.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // 执行非查询语句
    public void query(String sql) throws SQLException {
        PreparedStatement pstmt;
        pstmt = getConn().prepareStatement(sql);
        pstmt.execute();
        pstmt.close();
    }

    // 关闭连接
    public void close() {
        try {
            getConn().close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}

public class JdbcTest {

    public static void main(String[] args) {
        JdbcOperation jdbcOperation = new JdbcOperation();
        try {
            jdbcOperation.query("create table flower(id int, name varchar2(20))");
            jdbcOperation.query("insert into flower values(1,'lavender')");
            jdbcOperation.query("insert into flower values(2,'violet')");
            jdbcOperation.query("select * from flower", true);
        } catch (SQLException e) {
            System.out.println(e);
        }
    }
}
```
