import random
def coin_flip(n_flips):
    heads=0
    tales=0

    for i in range (0,n_flips):
        r=int(random.random()*2)+1
        if(r==1):
            heads=heads+1
        else:
            tales=tales+1
    print("Number of flips =",n_flips)
    print("Number of heads =",heads)
    print("Number of tales =",tales)
        
coin_flip(10)
