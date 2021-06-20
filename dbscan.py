import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN

def classify(df):
    # df = pd.read_csv('test.csv')
    df = df
    blobs = df[["Salary","Age"]]
    
    preds = DBSCAN(700, 2).fit(df[["Salary","Age"]])
    labels = list(preds.labels_)
    
    names = list(df["Name"])
    data = dict(zip(names, labels))
    print(data)
    
    for x,y in data.items():
        if y == 0:
            data[x] = 'A CLASS'
        elif y == 1:
            data[x] = 'B CLASS'
        elif y == -1:
            data[x] = 'UNKNOWN CLASS'
        else: 
            data[x] = 'C CLASS'
    
    for x, y in data.items():
        print(x,y)
    return list(data.values())