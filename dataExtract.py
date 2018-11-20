
from removeChars import*

def extract (file):
    filehandle = open(file,'r')
    lyrics = filehandle.readlines()
    
    # all the words in the song
    words = []
    for lines in lyrics:
        for word in lines.split():
          #temp = removeChars(word)
          words.append(removeChars(word))
       
   
    
    singleWords = [] #no duplicates of words
    for word in words:
        if word not in singleWords:
            singleWords.append(word)
        
    
    wordAndCount = { word:words.count(word) for word in singleWords}
    
    #closing the file
    filehandle.close()
    return wordAndCount

