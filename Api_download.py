import lxml.html
import requests
import json
from lxml import etree

title="Taken"



class Omdb():
    def dict_create(self,title):
        web = "http://www.omdbapi.com/?t={}&apikey=55f1c482".format(title)
        page = requests.get(web).text
        page = json.loads(page)
        print(page)
        print(type(page))

o=Omdb()
o.dict_create(title)



