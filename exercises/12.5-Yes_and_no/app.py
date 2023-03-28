theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
newList = list(map(lambda i : "wiki" if i == 1 else "woko", theBools)) 

print(newList)

