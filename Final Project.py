#!/usr/bin/env python
# coding: utf-8

# In[9]:


import requests

url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

search = input("What movie or show would you like to search: ")
page_number = input("Which page you want to search: ")
querystring = {"page":f"{page_number}", "r":"json","s":f"{search}"}

headers = {
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
    'x-rapidapi-key': "7d238656bamshd39f022196547f4p1571bcjsn73ec87d5dcf7"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

movie_search = response.json()

import pandas as pd
movie_search_df = pd.DataFrame(movie_search['Search'])
movie_search_df[['Title', 'Year', 'imdbID', 'Type']]


# In[10]:


number=int(input("Enter the number of the search (0-9) to check the Poster & the IMDb rating and metascore:"))


from IPython.display import Image
display(Image(movie_search['Search'][number]['Poster']))



url_2 = "https://movie-database-imdb-alternative.p.rapidapi.com/"

imdbid = movie_search['Search'][number]['imdbID']
querystring_2 = {"i":f"{imdbid}","r":"json"}

headers_2 = {
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
    'x-rapidapi-key': "7d238656bamshd39f022196547f4p1571bcjsn73ec87d5dcf7"
    }

response_2 = requests.request("GET", url_2, headers=headers_2, params=querystring_2)

rating = response_2.json()
IMDb_rating = rating["imdbRating"]
metascore = rating['Metascore']
print(f"Type        =====> {movie_search['Search'][number]['Type']}")
print(f"IMDB rating =====> {IMDb_rating}/10")
print(f"Metascore   =====> {metascore}")
      
if float(IMDb_rating) >= 7.5:
      print(f"This might be a good {movie_search['Search'][number]['Type']}! You should go take a look!!")
if float(IMDb_rating) < 7.5 and float(IMDb_rating) > 4:
        print(f"The score is not too high, not sure if is good {movie_search['Search'][number]['Type']}, you can still take a look!")
if float(IMDb_rating) <= 4:
            print(f"It is not a good {movie_search['Search'][number]['Type']}, probably you don't want to wast your time on this!")


# In[11]:


title = movie_search['Search'][number]['Title']
year = movie_search['Search'][number]['Year']

url_3 = "https://youtube-search.p.rapidapi.com/search"

querystring_3 = {"q":f"{title}{year}","part":"snippet","key":"AIzaSyCHs-Lj8kAymNCK08pZS2dBPEOafhwnyRk"}

headers_3 = {
    'x-rapidapi-host': "youtube-search.p.rapidapi.com",
    'x-rapidapi-key': "7d238656bamshd39f022196547f4p1571bcjsn73ec87d5dcf7"
    }

response_3 = requests.request("GET", url_3, headers=headers_3, params=querystring_3)

youtube_search = response_3.json()

try:
    from IPython.display import YouTubeVideo
    display(YouTubeVideo(youtube_search['items'][0]['id']['videoId']))
except KeyError:
    from IPython.display import YouTubeVideo
    display(YouTubeVideo(youtube_search['items'][1]['id']['videoId']))


# In[8]:


import json
from requests import get
payload = {"api-key": "a742facd673bc5d8c18826847e1f236cb59138d25e63b989192d80ea"}
response = requests.get('https://api.ipdata.co', params=payload).json()

location = response['city']#getting user's location


url = "https://google-search1.p.rapidapi.com/google-search"
querystring = {"q":"movietickets"+location,"hl":"en","gl":"us"}#searching using keywords with location

headers = {
    'x-rapidapi-host': "google-search1.p.rapidapi.com",
    'x-rapidapi-key': "0e1f09891fmsh8435236060fe9bfp15a56bjsnb9457682250e"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
movie_search = response.json()

choice_buy = input("Do you want to get the ticket links for nearby movie theater(yes or no)?")#asking for user's choice for buying tickets
try:
    if choice_buy == 'yes':
        print(f"Ticket link of Regal Destiny USA {movie_search['organic'][0]['url']}")
        print(f"Ticket link of Regal Shoppingtown Mall {movie_search['organic'][1]['url']}")
        print(f"Ticket link of Movie Tavern {movie_search['organic'][2]['url']}")

    else:
        print('Okay, I hope you can find another one you wanna watch!')

except KeyError:
    print('Please enter valid answer!')


# In[ ]:





# In[ ]:





# In[ ]:




