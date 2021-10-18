---
title: Python Send Mail
tags: python
date: 2019-02-28
---

### send mail

```python
import smtplib
import os.path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


port = 25
smtp_server = 'xxx'


def mail(sender, receiver, subject, content, files=None):
    """
    sender, receiver: a string of comma separated email addresses
    content: html or plain text
    files: a list of pathnames of attachments
    """
    message = MIMEMultipart('alternative')
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receiver

    disclaimer = 'The HTML version of this email may not be rendered properly, displaying plain text instead.\n\n'
    html = content
    content = disclaimer + content
    plain_part = MIMEText(content, 'plain')  # plain text
    html_part = MIMEText(html, 'html')  # html
    message.attach(plain_part)
    message.attach(html_part)

    if files:
        for filename in files:
            with open(filename, 'rb') as attachment:
                binary_part = MIMEApplication(attachment.read())

            binary_part.add_header('Content-Disposition', 'attachment',
                                   filename=os.path.basename(filename))
        message.attach(binary_part)

    with smtplib.SMTP(smtp_server, port) as server:
        recipients = [to_addr.strip() for to_addr in receiver.split(',')]
        server.sendmail(sender, recipients, message.as_string())


if __name__ == '__main__':
    sender = ''
    receiver = ''
    subject = '[TEST] multipart test 中文測試'
    content = '<h1>Hello, World</h1>'
    files = ['中文繁體UTF8.txt',
             '中文简体GB2312.txt']
    mail(sender, receiver, subject, content, files)
```

### send mail use template

mail.py

```python
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader
import os
import requests


def get_data():
    data = requests.get(
        'https://jsonplaceholder.typicode.com/users/1/posts').json()
    return data


def mail(content):
    from_email = 'Babb_Chen@sdc.sercomm.com'
    to_email = 'Babb_Chen@sdc.sercomm.com'
    subject = 'This is a email from Python with a table!'
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = from_email
    message['To'] = to_email

    message.attach(MIMEText(content, "html"))
    body = message.as_string()

    server = SMTP('xxx', 25)
    # server.starttls()
    # server.login(from_email, 'your password')
    server.sendmail(from_email, to_email, body)

    server.quit()


def send_mail():
    data = get_data()
    keys = data[0].keys()
    title = 'Posts List'

    # core component of JinJa
    env = Environment(loader=FileSystemLoader(
        '%s/templates/' % os.path.dirname(__file__)))
    template = env.get_template('child.html')
    output = template.render(title=title, items=data, keys=keys)
    mail(output)


if __name__ == "__main__":
    send_mail()
```

templates/base.html

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <style>
            .table {
                font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
                width: 100%;
                border-collapse: collapse;
            }

            .table td,
            .table th {
                font-size: 1em;
                border: 1px solid #98bf21;
                padding: 3px 7px 2px 7px;
            }

            .table th {
                font-size: 1.1em;
                text-align: left;
                padding-top: 5px;
                padding-bottom: 4px;
                background-color: #a7c942;
                color: #ffffff;
            }

            .table tr.even td {
                color: #000000;
                background-color: #eaf2d3;
            }
        </style>
    </head>
    <body>
        <div class="content">{% block content %}{% endblock %}</div>
    </body>
</html>
```

templates/child.html

```jinja2
{% extends "base.html" %} {% block content %}
<h1>{{title}}</h1>

<table class="table">

    <tr>
        {% for key in keys %}
           <th>{{key}}</th>
        {% endfor %}
    </tr>

    {% for item in items %}
        {% if loop.index is divisibleby 2 %}
            <tr class="even">
                {% for key in keys %}
                   <td>{{item[key]}}</td>
                 {% endfor %}
            </tr>
        {% else %}
            <tr class="odd">
                {% for key in keys %}
                   <td>{{item[key]}}</td>
                {% endfor %}
            </tr>
        {% endif %}
    {% endfor %}
    
</table>
        
{% endblock %}
```

