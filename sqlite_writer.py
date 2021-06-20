import sqlite3
import sqlalchemy
import datetime
import pandas as pd
import os
import datetime
import uuid
import dbscan
import copy


def sqlite_write():
    try:
        sqliteConnection = sqlite3.connect('db.sqlite')
        cursor = sqliteConnection.cursor()
        print("Database created and Successfully Connected to SQLite")
    
        sqlite_select_Query = "select sqlite_version();"
        cursor.execute(sqlite_select_Query)
        record = cursor.fetchall()
        print("SQLite Database Version is: ", record)
        
        for i in os.listdir('downloads'):
            auuid = uuid.uuid1()
            df = pd.read_csv('downloads/'+str(i))
            values_list = dbscan.classify(df)
            df1 = df.copy()
            df1['Class'] = values_list
            df.to_sql('data_table',con=sqliteConnection,if_exists='append',index=False)
            df1.to_sql('class_table',con=sqliteConnection,if_exists='append',index=False)
            # cursor.execute(sql)
            sqliteConnection.commit()
    
        cursor.close()
    
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")