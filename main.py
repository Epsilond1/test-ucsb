#!/usr/bin/python3.5
# -*-coding:utf-8 -*-
import postgresql
from bottle import route, run, debug, template, get, request, default_app, error
import re
import datetime

log_broker = open('log-main-application.log', 'a')

try:
    db = postgresql.open('pq://postgres:password@188.116.57.50:5432/ussc')
except Exception:
    log_broker.writelines('{0} Fail on connect to database\n'.format(datetime.datetime.now()))
else:
    log_broker.writelines('{0} Connect to DB succesfull\n'.format(datetime.datetime.now()))


@property
def charset(self, default='UTF-8'):
    if 'charset=' in self.content_type:
        return self.content_type.split('charset=')[-1].split(';')[0].strip()
    return default

@error(500)
@error(501)
@error(502)
def internralerror(code):
	return 'Servery ploxo {0}'.format(code)

def isvalidphone(phone):
    return re.match(r'[7-8]{1}[0-9]{9}', phone) and len(phone) == 11


@route('/')
def main():
    return template('main_forms.tpl')


@get('/show')
def printdb():
    result = db.query('SELECT * FROM users')
    return template('input.tpl', rows=result)


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
        return template('success.tpl')
    else:
        return template('errphone.tpl')

# debug(True)
# run(port=888)

if __name__ == '__main__':
    run(host='188.116.57.50', port=8181)
# Run bottle in application mode. Required in order to get the application working with uWSGI!
else:
    application = app = default_app()

# bottle.run(app=StripPathMiddleware(app),server='python_server',host='188.116.57.50',port=9999)
# test_ussc = application = default_app()
# db.close()
log_broker.close()
