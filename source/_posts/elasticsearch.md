---
title: Elasticsearch
tags: java
date: 2019-11-26
---

### postman

```yaml
index page: GET localhost:9200/
get all index: GET localhost:9200/_all
create index: PUT localhost:9200/person
delete index: DELETE localhost:9200/person
create data: POST localhost:9200/person/_doc/1

body
{
	"first_name": "Babb",
	"last_name": "Chen",
	"age": 15,
	"about": "I love programming and good at sql",
	"interests": ["music", "java"]
}

get by id: localhost:9200/person/_doc/1
search: localhost:9200/person/_doc/_search?q=first_name:babb

```

### kibana

**获取所有索引**

```
GET _all
```

**根据 ID 获取数据**

```
GET /person/_doc/1
```

**DSL 结构化查询**

可以省略 /person/_doc/_search 中的 _doc, 建议一个 index,  一个 type,  _doc 是默认 type

should 相当于 mysql 中的 or

must 相当于 mysql 中的 and

```json
POST /person/_search
{
  "query": {
    "bool": {
      "should": [
        {
          "match": {
            "last_name": "chen"
          }
        },
        {
          "match": {
            "about": "programming"
          }
        }
      ]
    }
  }
}

POST /person/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "last_name": "chen"
          }
        },
        {
          "match": {
            "about": "programming"
          }
        }
      ]
    }
  }
}
```

### logstash

**mysql 数据**

```mysql
use elastic;

create table blog (
	id int(11) not null auto_increment,
    title varchar(60) default null,
    author varchar(60) default null,
    content mediumtext,
    create_time datetime default null,
    update_time datetime default null,
    primary key (id)
) engine=InnoDB auto_increment=12 default charset=utf8mb4;

insert into blog values(null, 'php', 'babb', 'php是世界上最好的语言', sysdate() - 10, sysdate()-1);
insert into blog values(null, 'Hello world', 'babb', 'Hello world is 世界, 你好', sysdate() - 5, sysdate());
insert into blog values(null, 'php', 'babb', 'php is the best language of the world', sysdate() - 5, sysdate());
```

**mysql.conf**

```json
input {
  jdbc {
        jdbc_driver_library => "../logstash-7.4.0/mysql-connector-java-8.0.16.jar"
        jdbc_driver_class => "com.mysql.jdbc.Driver"
        jdbc_connection_string => "jdbc:mysql://127.0.0.1:3306/elastic"
        jdbc_user => "root"
        jdbc_password => "root"
        schedule => "* * * * *"
        # 为 true 表示重启 logstash 重新读取数据库所有内容，false 会从上次读取的内容开始往后读取
        clean_run => true
        statement => "select * FROM blog WHERE update_time > :sql_last_value AND update_time < NOW() ORDER BY update_time desc"
  }
}


output {
  elasticsearch {
    hosts => ["127.0.0.1:9200"]
    index => "blog"
    document_id => "%{id}"
  }
}
```

`logstash -f ../conf/myql.conf`

C:\Program Files\Elastic\logstash-7.4.0\bin>logstash -f  ..\config\mysql.conf
错误: 找不到或无法加载主类 Files\Elastic\logstash-7.4.0\logstash-core\lib\jars\animal-sniffer-annotations-1.14.jar;
原因: Program Files 存在空格, 将 logstash-7.4.0直接移动到 c 盘下

错误:  com.mysql.cj.jdbc.Driver not loaded. Are you sure you've included the correct jdbc driver in :jdbc_driver_library
移动 mysql-connector-java-8.0.16.jar 到 C:\logstash-7.4.0\logstash-core\lib\jars 目录下，将 jdbc_driver_library 修改位空即 jdbc_driver_library => "", 另外 mysql 8 需要将 jdbc_driver_class => "com.mysql.jdbc.Driver" 修改为
jdbc_driver_class => "com.mysql.cj.jdbc.Driver"

错误:  Unable to connect to database. Tried 1 times {:error_message=>"Java::JavaSql::SQLException: The server time zone value '锟叫癸拷锟斤拷\u05FC时锟斤拷' is unrecognized or represents more than one time zone. You must configure either the server or JDBC driver (via the serverTimezone configuration property) to use a more specifc time zone value if you want to utilize time zone support."}
修改jdbc_connection_stringg，设置 Timezone 为 UTC jdbc_connection_string  => "jdbc:mysql://127.0.0.1:3306/elastic?useTimezone=true&useLegacyDatetimeCode=false&serverTimezone=UTC"

修改后的配置如下

```json
input{
    jdbc{
        jdbc_driver_library => ""
        jdbc_driver_class => "com.mysql.cj.jdbc.Driver"
        jdbc_connection_string => "jdbc:mysql://127.0.0.1:3306/elastic?useTimezone=true&useLegacyDatetimeCode=false&serverTimezone=UTC"
        jdbc_user => "root"
        jdbc_password => "root"
        schedule => "* * * * *"
        clean_run => true
        statement => "select * FROM blog WHERE update_time > :sql_last_value AND update_time < NOW() ORDER BY update_time desc"
    }
}

output {

    elasticsearch{
        hosts => ["127.0.0.1:9200"]
        index => "blog"
        document_id => "%{id}"
    }

}
```

运行 `logstash -f ../conf/myql.conf`， Postman 查询 `localhost:9200/blog/_doc/_search`

### tokenizer

标准分词器对中文支持不友好

```json
POST _analyze
{
	"analyzer": "standard",
    "text": "我是中国人"
}
```

IK 分词器，下载 [Ik分词器](https://github.com/medcl/elasticsearch-analysis-ik/releases) 放到 Elasticsearch 的 plugins 目录 C:\Program Files\Elastic\Elasticsearch\7.4.0\plugins

