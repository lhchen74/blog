---
title: Go Read File To Mysql
tags: go
date: 2020-03-17
---

读取文件的每一行到 mysql 的 memo 栏位

```go
package main

import (
	"bufio"
	"database/sql"
	"fmt"
	"io"
	"log"
	"os"
	"path/filepath"

	_ "github.com/go-sql-driver/mysql"
)

func init() {
	logPath := ""
	logFile, err := os.OpenFile(logPath, os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0644)
	if err != nil {
		fmt.Println("open log file failed, err:", err)
		return
	}
	log.SetOutput(logFile)
	log.SetPrefix("[TEST]")
	log.SetFlags(log.Llongfile | log.Lmicroseconds | log.Ldate)
}

var db *sql.DB // global db

func initDB() (err error) {
	log.Println("initDB start")
	dsn := "root:root@tcp(127.0.0.1:3306)/test" // DSN:Data Source Name
	db, err = sql.Open("mysql", dsn)            // The password for the account will not be checked
	if err != nil {
		return err
	}
	err = db.Ping() // Try connect database, check the dsn is correct
	if err != nil {
		return err
	}
	log.Println("initDB success")
	return nil
}

func insertRows(rows [][]string) { 
	log.Println("insertRows start")
	sqlStr := "insert into som_edi_test_source(type, filename, memo) values (?,?,?)"
	for _, row := range rows {
		ret, err := db.Exec(sqlStr, row[0], row[1], row[2])
		if err != nil {
			log.Fatal("insert failed, error: ", err)
			return
		}
		theID, err := ret.LastInsertId()
		if err != nil {
			log.Fatal("get lastinsert ID failed, error:", err)
			return
		}
		log.Println("insert row success, the id is", theID)
	}
	log.Println("insertRows success")
}

func getFileContents(editype, path string) [][]string {  // [["855", "test.udf", "this is test"], ...]
	filename := filepath.Base(path)
	log.Printf("getFileContents %s %s start", editype, filename)
	var contents [][]string
	file, err := os.Open(path)
	if err != nil {
		log.Fatal("open file failed, error:", err)
		return nil
	}
	defer file.Close()
	reader := bufio.NewReader(file)
	for {
		line, err := reader.ReadString('\n')
		content := []string{editype, filename}

		if err == io.EOF {
			if len(line) != 0 {
				content = append(content, line)
			}
			break
		}
		if err != nil {
			log.Fatal("read file failed, error:", err)
			return nil
		}
		content = append(content, line)
		contents = append(contents, content)
	}
	log.Printf("getFileContents %s %s success", editype, filename)
	return contents
}

func main() {
	err := initDB()
	if err != nil {
		log.Fatal("initDB error: ", err)
		return
	}

	path := ""

	var rowsData = getFileContents("855", path)
	insertRows(rowsData)
}

```

数据库创建语句

```mysql
CREATE TABLE `som_edi_test_source` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(10) DEFAULT NULL,
  `filename` varchar(100) DEFAULT NULL,
  `memo` varchar(2000) DEFAULT NULL,
  `created_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8
```

