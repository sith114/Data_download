import lxml.html
import requests
import json
import pandas as pd
import numpy as np
from lxml import etree

class File():

    def open(self):
        data_frame = pd.read_csv(self)
        #print(data_frame)
        return data_frame

    '''def save2():
        data_frame.to_csv("movies_updated.csv", index=False)'''

    def save(self):
        self.to_csv("movies_updated.csv", index=False)

class Movie_update():
    movie_title=" "
    movie_dict=""
    frame_data_row=""

    def data_row(self,data_frame,i):
        frame_data_row=data_frame.values[i]
        self.frame_data_row=frame_data_row
        #print(self.frame_data_row)
        return self.frame_data_row


    def title(self,data_frame, ite):
        row = data_frame.values[ite]
        #print(row)
        #print(row[1])
        self.movie_title=row[1]
        return self.movie_title

    def dict_create(self):
        web = "http://www.omdbapi.com/?t={}&apikey=55f1c482".format(self.movie_title)
        page = requests.get(web).text
        self.movie_dict = json.loads(page)
        #print(self.movie_dict)
        return self.movie_dict

    def add_year(self):
        #print(self.movie_dict.get("Year"))
        self.frame_data_row[2]=self.movie_dict.get("Year")
        #print(self.frame_data_row)
        return self.frame_data_row

    def update_data_frame(self,data_frame,i):
        data_frame[i:i+1]=self.frame_data_row
        #print(data_frame)
        return data_frame

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
data_frame = File.open("movies.csv")


i=0
movie_list_update = Movie_update()
while i < data_frame.shape[0]:

    movie_list_update.data_row(data_frame,i)

    movie_list_update.title(data_frame,i)
    movie_list_update.dict_create()
    movie_list_update.add_year()
    movie_list_update.update_data_frame(data_frame,i)


    i+=1

File.save(data_frame)
#File.save2()
print(data_frame)
print("END")