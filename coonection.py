import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="mfcv3")


def add_user(login,fullname, password):
    cursor = connection.cursor()
    request = f'''INSERT INTO users (login,fullname,password,usertype) VALUES ('{login}','{fullname}','{password}','{"user"}');'''
    print(request)
    cursor.execute(request)
    connection.commit()
    return connection, cursor


def user_exist(login):
    cursor = connection.cursor()
    request = f'''SELECT * FROM users WHERE login ='{login}';'''
    cursor.execute(request)
    if len(cursor.fetchall()) > 0:
        return True
    else:
        return False


def login_user(login, password):
    cursor = connection.cursor()
    request = f'''SELECT * FROM users WHERE login ='{login}' AND password ='{password}';'''
    cursor.execute(request)
    print(request)
    return cursor.fetchall()


def get_mark_with_filial_and_indicator_and_servise():
    cursor= connection.cursor();
    request = f'''SELECT department.fullname, servises.fullname, indicator.name, mark from mark
    INNER JOIN indicator ON indicator.id_indicator=mark.id_indicator
    INNER JOIN servises ON servises.id_servises=mark.id_servise
    INNER JOIN department ON department.id_department=mark.id_dep;'''
    cursor.execute(request)
    print(request)
    return cursor.fetchall()


def get_name(login):
    cursor= connection.cursor()
    request=f'''SELECT fullname FROM users WHERE login ='{login}';'''
    cursor.execute(request)
    print(request)
    return cursor.fetchall()



def get_fullname_department(login):
    cursor= connection.cursor()
    request=f'''select department.fullname from department 
INNER JOIN users ON users.id_users=department.id_user
WHERE users.login='{login}';'''
    cursor.execute(request)
    print(request)
    return cursor.fetchall()


def get_all_indicator():
    cursor = connection.cursor()
    request = f'''SELECT name FROM indicator;'''
    cursor.execute(request)
    print(request)
    return cursor.fetchall()


def get_all_servises():
    cursor = connection.cursor()
    request = f'''SELECT fullname FROM servises;'''
    cursor.execute(request)
    print(request)
    return cursor.fetchall()


def get_usertype_users(login):
    cursor = connection.cursor()
    request = f'''SELECT usertype FROM servises;'''
    cursor.execute(request)
    print(request)
    return cursor.fetchall()



def get_mark_where_user_srvises_indicator(login):
    cursor=connection.cursor();
    request=f'''select * from MARK where id_indicator=1 and id_servise=2
            and id_dep IN(select id_department from department
            inner join users on users.id_users =department.id_user
            where users.login='{login}')  ; '''
    cursor.execute(request)
    # print(request)
    return cursor.fetchall()


def add_new_mark(login):
    cursor=connection.cursor();
    request=f''''''
    cursor.execute(request)
    return cursor.fetchall()