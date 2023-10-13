import random
import time
import numpy as np
A=np.zeros((7,7)) #The game matrix
B=np.zeros((7,7))   #The test matrix
b=0
win=0
subwin=0
def filler(x):
    flag=1
    for j in range(7):
        if((A[6-j,x]==0)&(flag==1)):  #Checking the unfilled state from bottom
            if(player==1):
                A[6-j,x]=1
                flag=0
            else :
                A[6-j,x]=2
                flag=0
def fillerB(x): #Filling B

    flag=1
    for j in range(7):
        if((B[6-j,x]==0)&(flag==1)):
            if(player==1):
                B[6-j,x]=1
                flag=0
            else :
                B[6-j,x]=2
                flag=0            
def checkhorizontal(a):     #Checks for horizontal win in A
    
    global win
    flag2=0
    for i in range(7):
        N=0
        jprev=-1
        for j in range(7):
            
            if(A[i,j]==a):
                if N==0:
                    jprev=j-1
                if(j==jprev+1):
                    N=N+1                 
                jprev=j
            else:
                N=0
            if(N==4):
                flag2=a
    if(flag2!=0):
        #print(a,'wins')
        win=1

def checkvertical(a):       #Checks for vertical win in A
    
    global win
    flag2=0
    for j in range(7):
        N=0
        iprev=-1
        for i in range(7):
            
            if(A[i,j]==a):
                if N==0:
                    iprev=i-1
                if(i==iprev+1):
                    N=N+1                 
                iprev=i
            else:
                N=0
            if(N==4):
                flag2=a
               
    if(flag2!=0):
        #print(a,'wins')
        win=1

def checkdiagonal(a):

    global win
    flag2=0
    for i in range(6,2,-1):
        for j in range(4):

            if((A[i][j]==a)&(A[i-1][j+1]==a)&(A[i-2][j+2]==a)&(A[i-3][j+3]==a)):
                #print(a,'wins')
                win=1

    for i in range(6,2,-1):
        for j in range(6,2,-1):

            if((A[i][j]==a)&(A[i-1][j-1]==a)&(A[i-2][j-2]==a)&(A[i-3][j-3]==a)):
                #print(a,'wins')
                win=1
draw=1
def checkdraw():
    global draw
    draw=1
    for i in range(7):
        for j in range(7):
             if(A[i][j]==0):
                 draw=0
    
def checkit(a):
    global win
    checkhorizontal(a)
    checkvertical(a)
    checkdiagonal(a)


subwin=0
def checkhorizontalB(a): #Checks for horizontal win in B
    
    global subwin
    flag2=0
    for i in range(7):
        N=0
        
        for j in range(7):
            
            if(B[i,j]==a):
                if N==0:
                    jprev=j-1
                if(j==jprev+1):
                    N=N+1                 
                jprev=j
            else:
                N=0
            if(N==4):
                flag2=a
    if(flag2!=0):
        
        subwin=1

def checkverticalB(a): #Checks for vertical win in B
    
    global subwin
    flag2=0
    for j in range(7):
        N=0
        for i in range(7):
            
            if(B[i,j]==a):
                if N==0:
                    iprev=i-1
                if(i==iprev+1):
                    N=N+1                 
                iprev=i
            else:
                N=0
            if(N==4):
                flag2=a
               
    if(flag2!=0):
        
        subwin=1

def checkdiagonalB(a):

    global subwin
    flag2=0
    for i in range(6,2,-1):
        for j in range(4):

            if((B[i][j]==a)&(B[i-1][j+1]==a)&(B[i-2][j+2]==a)&(B[i-3][j+3]==a)):
                subwin=1

    for i in range(6,2,-1):
        for j in range(6,2,-1):

            if((B[i][j]==a)&(B[i-1][j-1]==a)&(B[i-2][j-2]==a)&(B[i-3][j-3]==a)):
                subwin=1

                
def checkitB(a):  #To check the subwin condition with B
    global subwin
    checkhorizontalB(a)
    checkverticalB(a)
    checkdiagonalB(a)
def Equate():  #Funtion to equate B to A
    for i in range(7):
        for j in range(7):
            B[i][j]=A[i][j]

def playai():
    global b
    global subwin
    global player
    flag2=0
    winstrat=0
    blockstrat=0
    for ply1 in range(7):   #Test for self win by trying all moves
        subwin=0
        player=2
        Equate()
        fillerB(ply1)

        checkitB(2)
        if(subwin==1):
            b=ply1
            winstrat=1

    if(winstrat==0):  #If self didn't win
        for ply1 in range(7):   #Test for opponent win and block by trying all opponent moves
            subwin=0
            player=1
            Equate()
            fillerB(ply1)
            checkitB(1)
            if(subwin==1):
                b=ply1
                blockstrat=1
    block2strat=0
    if((winstrat==0)&(blockstrat==0)):
        subwin=0
        
        doublestrat=0
        for ply1 in range(7):   #Try double throw and block it
        
            for ply2 in range(7):
                if(subwin==0):
                    player=1
                    Equate()
                    fillerB(ply1)
                    fillerB(ply2)
                    checkitB(1)
                    if(subwin==1):

                        b=ply1
                        block2strat=1

    if((winstrat==0)&(blockstrat==0)&(block2strat==0)):
        subwin=0
        doublestrat=0
        for ply1 in range(7):   #Try double throw and win it
        
            for ply2 in range(7):
                if(subwin==0):
                    player=2
                    Equate()
                    fillerB(ply1)
                    fillerB(ply2)
                    checkitB(2)
                    if(subwin==1):
                        b=ply1
                        doublestrat=1
    if((winstrat==0)&(blockstrat==0)):
        
        for ply1 in range(7):   #Try opponent move and avoid losing
            for ply12 in range(7): 
                subwin=0
                player=2
                Equate()
                fillerB(ply1)
                player=1
                fillerB(ply12)
                checkitB(1)
                if(subwin==1):
                    avoidb=ply1
                    
                    while(b==avoidb):
                        b=random.randint(0,6)
        
def playai1():
    global a
    global subwin
    global player
    flag2=0
    winstrat=0
    blockstrat=0
    for ply1 in range(7):   #Test for self win by trying all moves
        subwin=0
        player=1
        Equate()
        fillerB(ply1)

        checkitB(1)
        if(subwin==1):
            a=ply1
            winstrat=1

    if(winstrat==0):  #If self didn't win
        for ply1 in range(7):   #Test for opponent win and block by trying all opponent moves
            subwin=0
            player=2
            Equate()
            fillerB(ply1)
            checkitB(2)
            if(subwin==1):
                a=ply1
                blockstrat=1

    tryply1=0 
    

                
    block2strat=0
    if((winstrat==0)&(blockstrat==0)):
        subwin=0
        
        doublestrat=0
        for ply1 in range(7):   #Try double throw and block it
        
            for ply2 in range(7):
                if(subwin==0):
                    player=2
                    Equate()
                    fillerB(ply1)
                    fillerB(ply2)
                    checkitB(2)
                    if(subwin==1):
                        a=ply1
                        block2strat=1

    if((winstrat==0)&(blockstrat==0)&(block2strat==0)):
        subwin=0
        doublestrat=0
        for ply1 in range(7):   #Try double throw and win it
        
            for ply2 in range(7):
                if(subwin==0):
                    player=1
                    Equate()
                    fillerB(ply1)
                    fillerB(ply2)
                    checkitB(1)
                    if(subwin==1):
                        a=ply1
                        doublestrat=1

    if((winstrat==0)&(blockstrat==0)):
     
        for ply1 in range(7):   #Try opponent move and avoid losing
            for ply12 in range(7): 
                subwin=0
                player=1
                Equate()
                fillerB(ply1)
                player=2
                fillerB(ply12)
                checkitB(2)
                if(subwin==1):
                    avoida=ply1
                   
                    while(a==avoida):
                        a=random.randint(0,6)

                 
print('Enter a number for column from 1 to 7')   
onewin=0
twowin=0
drawstot=0

while 1:
    
    str1=''
    A=np.zeros((7,7)) #The game matrix
    B=np.zeros((7,7))   #The test matrix
    b=0
    win=0
    for i in range(49):
        
        if((win==0)&(draw==0)):

            player=1
            
            a=random.randint(0,6)
            playai1()            #Gettingply1Ai
            player=1
            filler(a)
            checkit(1)
            str1=str1+str(a)
        if((win==0)&(draw==0)):
            b=random.randint(0,6)
     
            playai()            #Gettingply1Ai
            
            player=2
            filler(b)
            str1=str1+str(b)
           
            checkit(2)
        """
        if((win==0)&(draw==0)):
            print(A)
            print('Pleyer1',a+1)
            print('Player2',b+1)
        """
        checkdraw()    


    if(win==1):
        
        if(player==1):
            onewin+=1
        else:
            twowin+=1
    if(draw==1):
        
        drawstot+=1


