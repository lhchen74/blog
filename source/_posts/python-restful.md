---
title: python flask restful
tags: python
date: 2019-02-28
---

### Restful API

```python
from flask import request
from flask import Flask
from flask import jsonify
from flask import abort
from flask import make_response
# flask_httpauth 需要单独安装
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

app = Flask(__name__)


tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    print(request.json)
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != str:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not str:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get(
        'description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@auth.get_password
def get_password(username):
    if username == 'root':
        return 'root'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)
```

### VSCode REST Client Test

```python
@uri=http://localhost:9999/todo/api/v1.0/
@json=Content-Type: application/json;charset=UTF-8
@auth=Authorization: Basic root root



### GET all tasks
GET {{uri}}tasks
{{auth}}
###
curl "http://localhost:9999/todo/api/v1.0/tasks" -u root:root -i


### GET one task
GET {{uri}}tasks/1
###
GET {{uri}}tasks/10


### Post one task
POST {{uri}}tasks
{{json}}

{
    "title": "Read a book"
}


### Put/Update one task
PUT {{uri}}tasks/1
{{json}}

{
    "title": "Learn Flask",
    "description": "IIS + Flask + Restful"
}


### Delete one task
DELETE {{uri}}tasks/1
```

### Requests Test

```python
import requests

uri = 'http://localhost:9999/todo/api/v1.0/'
auth = ('root', 'root')

response = requests.get(f'{uri}tasks', auth=auth)
print(response.json())
```
