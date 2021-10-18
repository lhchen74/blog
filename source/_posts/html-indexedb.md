---
title: html IndexedDB
tags: html
---

```html
<h1>IndexedDB</h1>

<script>
  // test dbname, 2 version
  var request = window.indexedDB.open('test', 2)
  request.onerror = function(event) {
    console.log('数据库打开报错')
  }

  var db

  // 新建数据库与打开数据库是同一个操作。如果指定的数据库不存在，就会新建。
  // 不同之处在于，后续的操作主要在 upgradeneeded 事件的监听函数里面完成，
  // 因为这时版本从无到有，所以会触发这个事件。
  request.onupgradeneeded = function(event) {
    console.log('onupgradeneeded...')
    db = event.target.result
    console.log(db)
    if (!db.objectStoreNames.contains('person')) {
      objectStore = db.createObjectStore('person', { keyPath: 'id' })
      objectStore.createIndex('name', 'name', { unique: false })
      objectStore.createIndex('email', 'email', { unique: true })
    }
  }

  request.onsuccess = function(event) {
    db = request.result
    console.log(db)
    console.log('数据库打开成功')
    function add() {
      var request = db
        .transaction(['person'], 'readwrite')
        .objectStore('person')
        .add({ id: 2, name: '张三', age: 24, email: 'lishi@example.com' })

      request.onsuccess = function(event) {
        console.log('数据写入成功')
      }

      request.onerror = function(event) {
        console.log('数据写入失败')
      }
    }

    add()

    function read() {
      var transaction = db.transaction(['person'])
      var objectStore = transaction.objectStore('person')
      var request = objectStore.get(1)

      request.onerror = function(event) {
        console.log('事务失败')
      }

      request.onsuccess = function(event) {
        if (request.result) {
          console.log('Name: ' + request.result.name)
          console.log('Age: ' + request.result.age)
          console.log('Email: ' + request.result.email)
        } else {
          console.log('未获得数据记录')
        }
      }
    }

    read()

    function readAll() {
      var objectStore = db.transaction('person').objectStore('person')

      objectStore.openCursor().onsuccess = function(event) {
        var cursor = event.target.result

        if (cursor) {
          console.log('Id: ' + cursor.key)
          console.log('Name: ' + cursor.value.name)
          console.log('Age: ' + cursor.value.age)
          console.log('Email: ' + cursor.value.email)
          cursor.continue()
        } else {
          console.log('没有更多数据了！')
        }
      }
    }

    readAll()

    function update() {
      var request = db
        .transaction(['person'], 'readwrite')
        .objectStore('person')
        .put({ id: 1, name: '李四', age: 35, email: 'lisi4@example.com' })

      request.onsuccess = function(event) {
        console.log('数据更新成功')
      }

      request.onerror = function(event) {
        console.log('数据更新失败')
      }
    }

    update()

    // function remove() {
    //     var request = db.transaction(['person'], 'readwrite')
    //         .objectStore('person')
    //         .delete(1);

    //     request.onsuccess = function (event) {
    //         console.log('数据删除成功');
    //     };
    // }

    // remove();
  }
</script>
```
