import random
def wind_speed_calculations():
#-----------------------------------------------------------------------
    wind_speeds=[]
    for i in range (0,14):
        random_number=int(random.random()*31)
        wind_speeds.append(random_number)
        print("The wind speed for day",i,"is",wind_speeds[i])
#-----------------------------------------------------------------------
    avg=0
    for i in range (0,14):
        avg=avg+wind_speeds[i]
    avg=avg/14
    print("The average wind speed is",avg)
#-----------------------------------------------------------------------
    highest_speed=-1
    highest_speed_day=-1
    for i in range (0,14):
        if wind_speeds[i]>highest_speed:
            highest_speed=wind_speeds[i]
            highest_speed_day=i
    print("The highest wind speed is",highest_speed)
    print("The highest wind speed day is",highest_speed_day)
#-----------------------------------------------------------------------
    lowest_speed=1000
    lowest_speed_day=-1
    for i in range (0,14):
        if wind_speeds[i]<lowest_speed:
            lowest_speed=wind_speeds[i]
            lowest_speed_day=i
    print("The lowest wind speed is",lowest_speed)
    print("The lowest wind speed day is",lowest_speed_day)
#-----------------------------------------------------------------------
    for i in range (0,14):
        diffrence=highest_speed-wind_speeds[i]
        print("Day",i,"wind speed is",diffrence,"miles less then the highest wind speed")
#-----------------------------------------------------------------------
wind_speed_calculations()
