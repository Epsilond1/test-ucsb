# -*-coding:utf-8 -*-
import postgresql
from bottle import route, run, debug, template, get, request
import re

db = postgresql.open('pq://postgres:postgres@laptop:5432/ussc')


@property
def charset(self, default='UTF-8'):
    if 'charset=' in self.content_type:
        return self.content_type.split('charset=')[-1].split(';')[0].strip()
    return default


def isvalidphone(phone):
    return re.match(r'[7-8]{1}[0-9]{9}', phone) and len(phone) == 11


@route('/')
def main():
    return template('main_forms')


@get('/show')
def printdb():
    result = db.query('SELECT * FROM users')
    return template('input', rows=result)


def stripchar(pattern, sym):
    result = ""
    for i in range(len(pattern)):
        if pattern[i] in sym:
            continue
        else:
            result += pattern[i]

    return result


@route('/add', method='POST')
def add_to_db():
    phone = stripchar(str(request.POST.get('phone').strip()), ['', ' ', '(', ')', '-', '+'])
    user = request.POST.get('name')
    if isvalidphone(phone):
        index = db.query("select count(*) from users")[0][0] + 1
        db.query("insert into users (id,pnumber,uname) values({0}, '{1}', '{2}');".format(index, phone, user))
        return template('success')
    else:
        return template('errphone')

debug(True)
run()

db.close()
