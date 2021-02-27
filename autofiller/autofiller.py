# -*- coding: utf-8 -*-
from fillerNotturno import fillerUserData
from telegram_users_database import UsersDatabase
from dateUpdater import dateUpdater


if __name__ == '__main__':

    users = UsersDatabase.get_users()
    dateUpdater()
    date = UsersDatabase.get_date()
    flag = date[2]
    row = date[3]
    column = date[4]
    print(row)
    print(column)
    for user in users:
        print("ciao")
        fillerUserData(user['Aula'],user['Nome'], user['Mail'], user['CodMatricola'], user['Telefono'],1, 2)


