
from SongDataScrape import*
from dataExtract import*
from CreateDir import*

#songName = "Better Now"
#artist = "Cake"
#artists = ['Cake','Pink Floyd','Kanye West', 'Led Zeppelin']
artists = ['Cake']
for artist in artists:  
    path = '.\\artists\\' +artist.replace(" ",",")
    createDir(path)

    getSongToTXT(artist)
    #getSongLyricsToTXT(songName, artist)
    #printPairs(pullWords("Better-Now-lyrics"), "Better Now")



    #filePathLyrics = ('.\lyrics\\' +artist+","+songName+'.txt').replace(" ",",")
    #filePathCounts = ('.\counts\\' +artist+","+songName+'.txt').replace(" ",",")
    #readFile = open((fileName), "r")
    #content = readFile.readlines

    #songWords = extract(filePathLyrics)
    #songWords = sorted(songWords,key = lambda x: x[0])
    #print (songWords)
    #writeSong = open(songName+".txt", 'w')
    #writeSong.write(str(songWords))
    #writeSong.close()
        