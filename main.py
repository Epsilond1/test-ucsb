# -*-coding:utf-8 -*-
import postgresql
from bottle import route, run, debug, template, get, request

db = postgresql.open('pq://postgres:postgres@laptop:5432/ussc')


def checkphone(phone):
    pass


@route('/')
def main():
    return template('main_forms')


@get('/add')
def add_to_db():
    phone = str(request.GET.get('phone').strip())
    user = str(request.GET.get('name').strip())
    index = db.query("select count(*) from users")[0][0] + 1
    db.query("insert into users (id,pnumber,uname) values({0}, '{1}', '{2}');".format(index, phone, user))
    return template('success')


debug(True)
run()

db.close()
