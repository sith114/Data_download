import lxml.html
import requests
import json
from lxml import etree

title="Taken"
web="http://www.omdbapi.com/?t={}&apikey=55f1c482".format(title)
#page = requests.get("http://www.omdbapi.com/?t=Taken&apikey=55f1c482").text
page = requests.get(web).text
print(page)

print(type(page))


x = json.loads(page)
print(x)
print(type(x))
print(x["Year"])
print(x["Title"])

#a