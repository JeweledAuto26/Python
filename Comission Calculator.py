print ("Input Sale Amount:")
sale = int(input())
if sale <= 2000:
    commission = .02
else:
    if sale <= 4000:
        commission = .04
    else:
        if sale <= 6000:
            commission = .07
        else:
            commission = .1
print (commission)
