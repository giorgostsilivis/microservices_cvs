import pandas as pd 
import os
import shutil
import sqlite_writer

def do_it():
    os.chdir("downloads")
    filelist = [f for f in os.listdir()]
    namelist = []
    agelist = []
    salarylist = []
    for f in filelist:
        df = pd.read_csv(f)
        for i in range(0,len(df)):
            name = df['Name'][i]
            namelist.append(name)
            age = df['Age'][i]
            agelist.append(age)
            salary = df['Salary'][i]
            salarylist.append(salary)
    os.chdir("..")
    sqlite_writer.sqlite_write()
    for f in filelist:
        shutil.move('downloads/'+str(f), 'backup'+'/'+str(f))
    # print(namelist)
    # print(agelist)
    # print(salarylist)
    