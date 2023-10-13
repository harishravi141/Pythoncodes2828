import random

options=['200 $','400 $','600 $','1000 $']
op2=['pay ','won  ']

while 1:
    print(random.choice(op2)+str(random.randint(100,1000))+' Crore ₹ ' )
    a=input()
