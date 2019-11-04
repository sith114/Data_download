import Api_download

import argparse


#execfile("Api_download.py")
'''a=Api_download.Movie_update()
b=Api_download.File()
a.data_row(b.open(),100)
a.add_title('a')'''

parser = argparse.ArgumentParser(description='Write text info a file.')

# Define arguments

parser.add_argument('--data',type=int,help="Download movies data, give num > 0 to download",default='0')
parser.add_argument('--sort_by1',type=str,help="Add movie, give movie title",default=None)
parser.add_argument('--add',type=str,help="Add movie, give movie title",default=None)
args = parser.parse_args()


#Pobieranie danych utworzenie pliku movies_updated.csv
if args.data != 0:
    Api_download.Pobranie()

if args.sort_by1 is not None:
    print(args.sort_by1)
    data_frame = Api_download.File.open("movies_updated2.csv")
    data_frame = data_frame.sort_values(by=[args.sort_by1])
    if args.sort_by1 == 'year':
        print(data_frame[["title","year"]])
    elif args.sort_by1 == 'title':
        print(data_frame[["title"]])

if args.add is not None:
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




