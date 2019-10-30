import lxml.html
import requests
import json
import pandas as pd
import numpy as np
from lxml import etree

#title="Taken"

class Open_file():
    def open():
        data_frame = pd.read_csv("movies.csv")
        return data_frame

class Save_file():
    def save(self):
        self.to_csv("movies.csv", index=False)

class Omdb():
    def dict_create(self):
        web = "http://www.omdbapi.com/?t={}&apikey=55f1c482".format(self)
        page = requests.get(web).text
        page = json.loads(page)
        print(page)
        print(type(page))

class Get_title():
    def title(self):
        row = self.values[0]
        #print(row[1])
        return row[1]

#data_frame.shape[0] - ilośc wierszy

data_frame = Open_file.open()
print(data_frame.shape[0])
x=Get_title.title(data_frame)
print("Movie title:",x)
Omdb.dict_create(x)

Save_file.save(data_frame)
