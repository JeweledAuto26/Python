print("Is the employee's salary hourly?")
print("Type 1 for yes and 0 for no:")
x = int(input())
if x > 0:
    print("Enter hours worked:")
    hours = int(input())
    if hours > 40:
        pay = 15 * 40 + (20* (hours - 40))
    else:
        pay = 15 * hours
else:
    pay = 500
print("Employee's pay is",pay,".")

    
