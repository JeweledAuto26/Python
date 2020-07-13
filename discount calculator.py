original_price=float(input())
print("The entered price is",original_price)
current_price=original_price
discount=0.1
days=("Monday","Tuesday","Wednesday","Thursday","Friday")
for day in days:
    new_price=current_price * (1-discount)
    current_price=new_price
    print("The price for", day,"is",new_price)
