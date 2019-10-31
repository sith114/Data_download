import lxml.html
import requests
import json
import pandas as pd
import numpy as np
from lxml import etree

#title="Taken"
class File():

    def open():
        data_frame = pd.read_csv("movies.csv")
        #print(data_frame)
        return data_frame

    def save2():
        data_frame.to_csv("movies_updated.csv", index=False)

    def save(self):
        self.to_csv("movies_updated.csv", index=False)

class Movie_update():
    movie_title=" "

    def title(self,data, ite):
        row = data.values[ite]
        #print(row)
        print(row[1])
        self.movie_title=row[1]
        return self.movie_title

    def dict_create(self):
        web = "http://www.omdbapi.com/?t={}&apikey=55f1c482".format(self.movie_title)
        page = requests.get(web).text
        page = json.loads(page)
        print(page)
        #print(type(page))
        return page

###########################################################################
'''class Omdb():
    def dict_create(self):
        web = "http://www.omdbapi.com/?t={}&apikey=55f1c482".format(self)
        page = requests.get(web).text
        page = json.loads(page)
        print(page)
        #print(type(page))
        return page'''
'''class Get_title():
    def title(self,ite):
        row = self.values[ite]
        #print(row)
        #print(row[1])
        return row[1]'''
class Add_Year():
    pass
############################################################################
#data_frame.shape[0] - ilośc wierszy

#-----------------------------------------------------------
data_frame = File.open()


i=0
movie_list_update = Movie_update()
while i < data_frame.shape[0]:
    ite = i
    movie_list_update.title(data_frame,i)
    movie_list_update.dict_create()
    i+=1

File.save(data_frame)
print("END")