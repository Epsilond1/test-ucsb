# -*-coding:utf-8 -*-
import postgresql
from bottle import route, run, debug, template, get, request

db = postgresql.open('pq://postgres:postgres@laptop:5432/ussc')


@property
def charset(self, default='UTF-8'):
    if 'charset=' in self.content_type:
        return self.content_type.split('charset=')[-1].split(';')[0].strip()
    return default


def checkphone(phone):
    pass


@route('/')
def main():
    return template('main_forms')


@get('/show')
def printdb():
    result = db.query('SELECT * FROM users')
    return template('input', rows=result)


@route('/add', method='POST')
def add_to_db():
    phone = str(request.POST.get('phone').strip())
    user = str(request.POST.get('name').strip())
    index = db.query("select count(*) from users")[0][0] + 1
    db.query("insert into users (id,pnumber,uname) values({0}, '{1}', '{2}');".format(index, phone, user))
    return template('success')


debug(True)
run()

db.close()
