import random

def showNemEnvironment():
    for i in matrix:
        print(i)
def clean():
    matrix[x][y]=0
    #agent new position
    matrix[i][j]="X"

def checkBorder():
    if i<0 or j<0:
        return False
    elif i>3 or j>3:
        return False
    else:
        return True
def istheAllEnvironmentClean():
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]==1:
                return False
    return True

rows, cols = (4, 4)
moveStack=[]
#creatNewEnvironment()
matrix = [[random.randint(0,1) for i in range(cols)] for j in range(rows)]

#Random Agent Position
x,y=random.randint(0,rows-1),random.randint(0,rows-1)
matrix[x][y]="X"
print("Agent has the location " + str(x) +"-"+str(y))
showNemEnvironment()

move=["right","left","up","down"]

i,j=x,y

while True:
    randomMove=random.choice(move)
    if randomMove=="right":
        i, j = x, y + 1
    elif randomMove=="left":
        i, j = x, y - 1
    elif randomMove=="up":
        i,j=x-1,y
    elif randomMove=="down":
        i,j=x+1,y

    if checkBorder() == True:
        print(randomMove)
        moveStack.append(randomMove)
        clean()
        x, y = i, j
        print("------------------------------")
        print("Agent has the location " + str(x) + "-" + str(y))
        showNemEnvironment()
        if istheAllEnvironmentClean() == True:
            print("All The Environments are clean ")
            break
    else:
        print("BORDER")
        #remove
        i, j = x, y


print("All Moves : " + str(moveStack))



















