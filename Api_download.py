import requests
import json
import pandas as pd




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

    def data_row(self,data_frame,i):
        frame_data_row=data_frame.values[i]
        self.frame_data_row=frame_data_row
        #print(self.frame_data_row)
        return self.frame_data_row

    def add_title(self,title):

        data_frame.loc[data_frame.index.max()+1]=[data_frame.index.max()+1,title,"","","","","","","","","","","",""]
        #self.frame_data_row[1] = title
        print(data_frame)


    def title(self,data_frame, i):
        row = data_frame.values[i]
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
    def add_movie(self):
        self.frame_data_row[2] = self.movie_dict.get("Year")
        self.frame_data_row[3] = self.movie_dict.get("Runtime")
        self.frame_data_row[4] = self.movie_dict.get("Genre")
        self.frame_data_row[5] = self.movie_dict.get("Director")
        self.frame_data_row[6] = self.movie_dict.get("Actors")
        self.frame_data_row[7] = self.movie_dict.get("Writer")
        self.frame_data_row[8] = self.movie_dict.get("Language")
        self.frame_data_row[9] = self.movie_dict.get("Country")
        self.frame_data_row[10] = self.movie_dict.get("Awards")
        self.frame_data_row[11] = self.movie_dict.get("imdbRating")
        self.frame_data_row[12] = self.movie_dict.get("imdbVotes")
        self.frame_data_row[13] = self.movie_dict.get("BoxOffice")
        return  self.frame_data_row
    """def add_year(self):
        #print(self.movie_dict.get("Year"))
        self.frame_data_row[2]=self.movie_dict.get("Year")
        #print(self.frame_data_row)
        return self.frame_data_row

    def add_runtime(self):
        #print(self.movie_dict.get("Runtime"))
        self.frame_data_row[3]=self.movie_dict.get("Runtime")
        #print(self.frame_data_row)
        return self.frame_data_row

    def add_genre(self):
        #print(self.movie_dict.get("Runtime"))
        self.frame_data_row[4]=self.movie_dict.get("Genre")
        #print(self.frame_data_row)
        return self.frame_data_row

    def add_director(self):
        #print(self.movie_dict.get("Runtime"))
        self.frame_data_row[5]=self.movie_dict.get("Director")
        #print(self.frame_data_row)
        return self.frame_data_row

    def add_cast(self):
        #print(self.movie_dict.get("Runtime"))
        self.frame_data_row[6]=self.movie_dict.get("Actors")
        #print(self.frame_data_row)
        return self.frame_data_row

    def add_writer(self):
        # print(self.movie_dict.get("Runtime"))
        self.frame_data_row[7] = self.movie_dict.get("Writer")
        # print(self.frame_data_row)
        return self.frame_data_row

    def add_language(self):
        # print(self.movie_dict.get("Runtime"))
        self.frame_data_row[8] = self.movie_dict.get("Language")
        # print(self.frame_data_row)
        return self.frame_data_row

    def add_country(self):
        # print(self.movie_dict.get("Runtime"))
        self.frame_data_row[9] = self.movie_dict.get("Country")
        # print(self.frame_data_row)
        return self.frame_data_row

    def add_awards(self):
        # print(self.movie_dict.get("Runtime"))
        self.frame_data_row[10] = self.movie_dict.get("Awards")
        # print(self.frame_data_row)
        return self.frame_data_row

    def add_imdb_rating(self):
        # print(self.movie_dict.get("Runtime"))
        self.frame_data_row[11] = self.movie_dict.get("imdbRating")
        # print(self.frame_data_row)
        return self.frame_data_row

    def add_imdb_votes(self):
        # print(self.movie_dict.get("Runtime"))
        self.frame_data_row[12] = self.movie_dict.get("imdbVotes")
        # print(self.frame_data_row)
        return self.frame_data_row

    def add_box_office(self):
        # print(self.movie_dict.get("Runtime"))
        self.frame_data_row[13] = self.movie_dict.get("BoxOffice")
        # print(self.frame_data_row)
        return self.frame_data_row
    """
    def update_data_frame(self,data_frame, i):
        data_frame[i:i+1]=self.frame_data_row
        #print(data_frame)
        return data_frame

#data_frame.shape[0] - ilośc wierszy

#-----------------------------------------------------------
data_frame = File.open("movies.csv")
#print(data_frame)

i=0
movie_list_update = Movie_update()

while i < data_frame.shape[0]:
    print("Pobieranie danych")
    movie_list_update.data_row(data_frame,i)
    movie_list_update.title(data_frame,i)
    #print(movie_list_update.movie_title)
    movie_list_update.dict_create()
    '''movie_list_update.add_year()
    movie_list_update.add_runtime()
    movie_list_update.add_genre()
    movie_list_update.add_director()
    movie_list_update.add_cast()
    movie_list_update.add_writer()
    movie_list_update.add_language()
    movie_list_update.add_country()
    movie_list_update.add_awards()
    movie_list_update.add_imdb_rating()
    movie_list_update.add_imdb_votes()
    movie_list_update.add_box_office()'''
    movie_list_update.add_movie()
    movie_list_update.update_data_frame(data_frame,i)
    i+=1

File.save(data_frame)
print(data_frame)
#print("END")

movie_list_update.add_title("Nana")