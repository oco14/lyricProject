from pandas import DataFrame, read_csv
from bs4 import BeautifulSoup
from CreateDir import*
from dataExtract import*

import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib
import requests
import re


#this function scrapes the web for the top 100 songs on a given day in history
def getChartsForDate(Month, Day, Year):
    
    #Gaining access to the billboards hot 100 for the specified date
    webpage = requests.get("https://www.billboard.com/charts/hot-100"+ "/" + Year + "-" + Month + "-" + Day)
    #turning the contents of the page into a soup
    soup = BeautifulSoup(webpage.content, "html.parser")
    #scraping top song and artist off the charts
    topSong = soup.select('.chart-number-one__title')
    topArtist = soup.select('.chart-number-one__artist')

    #scraping 2-100 ranked songs off the charts
    songs_list = soup.select('.chart-list-item__title-text')
    artists_list = soup.select('.chart-list-item__artist')

    #intializing lists for the final song list and artist list
    final_song_list = []
    final_artists_list = []
    
    #adding song and artist to lists after removing tags for top song
    #final_song_list.append(topSong[0].text.strip())
    final_artists_list.append(topArtist[0].text.strip())

    #adding songs 2-100 to list after removing tags
    for x in songs_list:
        final_song_list.append(x.text.strip())
    #adding artist to list after removing tags
    for y in artists_list:
        final_artists_list.append(y.text.strip())

    #creating data frame for songs and artist in top 100
    #Top100Songs = pd.DataFrame({'Songs': final_song_list, 'Artist': final_artists_list})
    #Top100Songs.to_csv('Top100Songs' + Month + Day + Year + ".csv")

    #return data frame of top 100 songs
    #return Top100Songs
    return (final_artists_list)

#this function scrapes the web for the lyrics to a song and creates a txt output of the song
def getSongLyricsToTXT (song, artist):

    #changing variables to append to weblink
    songSearch = song.replace(" ", "-")
    artistSearch = artist.replace(" ", "-")
    
    #gaining access to lyrics page
    lyricPage = requests.get('https://genius.com/'+ artistSearch + '-' + songSearch +"-"+'lyrics')
    print ('https://genius.com/'+ artistSearch + '-' + songSearch +"-"+'lyrics')
    #creating soup of page contents
    songSoup = BeautifulSoup(lyricPage.content, 'html.parser')
    #scraping lyrics and removing all tags
    lyrics = songSoup.select('.lyrics')
    if(len(lyrics) != 0):
        lyrics[0] = lyrics[0].text.strip()

        path = ('.\\artists\\'+artistSearch+ "\\"  +songSearch).replace(" ",",").replace("-",",")
        #creating txt file and writing song lyrics to txt file
        createDir(path)
        lyricsFile = open((path+'\lyrics.txt'), 'w')
        lyricsFile.write(lyrics[0])
        lyricsFile.close()

        #seperating the words and creating a file   
        songWords = extract(path+'\lyrics.txt')
        songWords = sorted(songWords,key = lambda x: x[0])
        #print (songWords)
        writeSong = open(path+"\words.txt", 'w')
        writeSong.write(str(songWords))
        writeSong.close()

    
#this function scrapes the web for the lyrics to a song and creates a txt output of the song
def getSongToTXT (artist):

    #changing variables to append to weblink
   
    artistSearch = artist.replace(" ", "-")
    
    #gaining access to lyrics page
    lyricPage = requests.get('https://genius.com/artists/'+ artistSearch )
    print ('https://genius.com/'+ artistSearch)
    #creating soup of page contents
    songSoup = BeautifulSoup(lyricPage.content, 'html.parser')
    #scraping lyrics and removing all tags
    songs = songSoup.select('.mini_card-title')
     
    for song in songs:
        song = song.text.strip()
        print (song)
        getSongLyricsToTXT(song,artist)
   
   # songs[0] = songs[0].text.strip()
   # print (songs[0])
   # songs[1] = songs[1].text.strip()
   # print (songs[1])
    
    #getSongLyricsToTXT(songs[0],artist)







