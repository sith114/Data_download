import Api_download
import pandas as pd
import argparse


def runtime():
    data_frame = Api_download.File.open("movies_updated2.csv")
    for i in range(0, data_frame.shape[0]):
        x = data_frame.values[i][3]
        # print(type(x))
        if type(x) == str:
            x = x.split(" ")
            # print(x[0])
            # data_frame["runtime"][i]=int(x[0]) #- nie gwarantuje poprawnosci
            data_frame.loc[i, 'runtime'] = int(x[0])
            # print(data_frame.values[i][3])
        if type(x) == float:
            # data_frame["runtime"][i]=x #- nie gwarantuje poprawnosci
            data_frame.loc[i, 'runtime'] = x
    data_frame = data_frame.sort_values(by=[args.sort_by1], na_position='first')
    return data_frame[["title", "runtime"]].to_string()

def Box_clear(a):
    if type(a) is not float:
        a=a.replace('$', '')
        a=float(a.replace(',', ''))
    else:
        a=0
    return a


parser = argparse.ArgumentParser(description='Write text info a file.')

# Define arguments

parser.add_argument('--data',type=int,help="Download movies data, give num > 0 to download",default='0')
parser.add_argument('--sort_by1',type=str,help="Sort by one: title,year,runtime,genre,director,cast,writer,language,country,awards,imdb_rating,imdb_votes,box_office",default=None)
parser.add_argument('--comp',help="Type of compare, movie1, movie2, movie3..."
                                  "type of comape is: runtime, Box office = box, IMDb Rating", default='',nargs='+')
parser.add_argument('--add',type=str,help="Add movie, give movie title",default=None)
args = parser.parse_args()


#Pobieranie danych utworzenie pliku movies_updated.csv
if args.data != 0:
    Api_download.Pobranie()

#Sortowania
if args.sort_by1 is not None:
    #print(args.sort_by1)
    data_frame = Api_download.File.open("movies_updated2.csv")

    if args.sort_by1 == 'year':
        data_frame = data_frame.sort_values(by=[args.sort_by1])
        print(data_frame[["title","year"]].to_string()) #.to_string() - pozwala printowac

    elif args.sort_by1 == 'title':
        data_frame = data_frame.sort_values(by=[args.sort_by1])
        print(data_frame[["title"]].to_string())

    elif args.sort_by1 == 'runtime':
        print(runtime())


    elif args.sort_by1 == 'genre':
        data_frame = data_frame.sort_values(by=[args.sort_by1])
        print(data_frame[["title","genre"]].to_string())

#Compare====================================================================
elif args.comp is not None:
    data_frame = Api_download.File.open("movies_updated2.csv")
    #print(args.comp)

    #Runtime================================================================
    if args.comp[0]=="runtime":
        #print(data_frame["title"].str.find(args.comp[1],0).to_string())
        for i in range(0, data_frame.shape[0]):
            x = data_frame.values[i][1]
            #print(x)
            if x == args.comp[1]:
                run1=data_frame.values[i][3]
                run1=int(run1.split(" ")[0])

            elif x==args.comp[2]:
                run2=data_frame.values[i][3]
                run2=int(run2.split(" ")[0])

        if run1>run2:
            print(args.comp[1],run1,'is longer than',args.comp[2],run2)
        elif run2>run1:
            print(args.comp[2], run2, 'is longer than', args.comp[1], run1)
    #Box_Office=========================================================
    if args.comp[0]=="box":
        #print("Box")
        for i in range(0, data_frame.shape[0]):
            x = data_frame.values[i][1]
            #print(x)
            if x == args.comp[1]:
                box1=data_frame.values[i][13]

            elif x==args.comp[2]:
                box2=data_frame.values[i][13]
        box1 = Box_clear(box1)
        box2 = Box_clear(box2)

        if box1 > box2:
            print(args.comp[1],box1,'has bigger box office than',args.comp[2],box2)
        elif box2>box1:
            print(args.comp[2], box2, 'has bigger box office than', args.comp[1], box1)
    if args.comp[0]=="IMDb Rating":
        #print("IMDb Rating")
        for i in range(0, data_frame.shape[0]):
            x = data_frame.values[i][1]
            #print(x)
            if x == args.comp[1]:
                imdb1=data_frame.values[i][11]

            elif x==args.comp[2]:
                imdb2=data_frame.values[i][11]
        #print(imdb1,imdb2)
        #print(type(imdb2))
        if imdb1 > imdb2:
            print(args.comp[1],imdb1,'has bigger IMDb Rating than',args.comp[2],imdb2)
        elif imdb2>imdb1:
            print(args.comp[2], imdb2, 'has bigger IMDb Rating than', args.comp[1], imdb1)

#Dodanie do pliku
elif args.add is not None:
    #print(Api_download.data_frame)
    #print(Api_download.File.open("movies_updated2.csv"))
    data_frame = Api_download.File.open("movies_updated2.csv")
    movie_list_update = Api_download.Movie_update
    movie_list_update.add_title(data_frame,args.add)
    movie_list_update.data_row(movie_list_update,data_frame, data_frame.index.max())
    movie_list_update.title(movie_list_update,data_frame, data_frame.index.max())
    movie_list_update.dict_create(movie_list_update)
    movie_list_update.add_movie(movie_list_update)
    movie_list_update.update_data_frame(movie_list_update,data_frame, data_frame.index.max())
    print(data_frame)
    Api_download.File.save2(data_frame)




