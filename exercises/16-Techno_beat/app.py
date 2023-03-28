def lyrics_generator(lista):
    song = ""
    counter = 0
    for i in lista:
        if i == 0:
            song += "Boom "
        if i == 1:
            song += "Drop the base "
            counter +=1
            if counter == 3:
                song += "!!!Break the base!!! "
                counter = 0
    return song
# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))