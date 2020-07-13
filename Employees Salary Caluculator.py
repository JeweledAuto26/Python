Rate = 12.30
moreEmployees = True
while (moreEmployees == True):
    Hours = int(input("Please enter employee hours:"))
    Pay = Hours * Rate
    print("Employee Pay = " + str(Pay))
    moreEmployees = int(input("Are there any more employees?"))
