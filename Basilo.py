# THIS PROJECTS GENERATES RANDOM EVENTS IN A MONTH, 
# THE EVENTS AFFECT BASILO's GROWTH

# Basilo

# what can i add to basilo

# soil 
# affectes leaves
# sunny = soil - 1
# range of 10

import random

daily_weather = ["sunny","partly cloudy","rainy","normal"]
daily_wind = [0,1,2,3,4]

leaves = 0
flowers = 0
day = 1
week = 7
month = 30

#for the soil
# i had to do this on top of a variable and then do something else down there

soil = 3
MAX_SOIL = 20
MIN_SOIL = 1

# define list and then randomize once per day.

def run_simulation():
    # Copa del árbol (hojas y flores)
    for i in range(1, leaves + 1):
        print(" " * (leaves - i), end="")  # Espacios para centrar
        print("🌿 " * i)                   # Hojas en forma triangular
    
    # Flores debajo de las hojas (opcional)
    if flowers > 0:
        print(" " * (leaves - 1), end="")  # Centrar las flores
        print("💮 " * flowers)
    
    # Tronco del árbol (representado con 🫠 o 🌲)
    print(" " * (leaves - 1), end="")
    print("🫠")  # O puedes usar "|" o "🌲" para el tronco
    
    # Tierra (suelo)
    print("💩 " * soil)

while day <= month:
                                                # loop for days in the month
    for i in range(month):
        # hadto: balance basilo's growth by setting limits -> should search a more efficient way. 
        if MIN_SOIL > soil:
            soil = 0       
        if MAX_SOIL < soil:
            soil = 20                                # same loop within the loop
        wind = random.choice(daily_wind)
        weather = random. choice(daily_weather) #setting random wind and weather

        #checking for soil

        if soil < 3:
            leaves = leaves - 1
            flowers = flowers - 1
        else:
            pass
        if soil >= 28:
            flowers = flowers + 2
        else:
            pass

        #checking for weather AND wind
                # affects: leaves, flowers, soil
                                                                                                    
        if weather == "sunny":
            if wind < 4:
                print("Day", day," was a nice day, +2 leaves") # best outcome
                leaves = leaves + 2
                flowers = flowers + 1
                soil = soil - 1
            else:
                leaves = leaves + 1
                soil = soil - 3
            print()
        elif weather == "rainy": 
            if wind < 3:
                print("Day",day,"was rainy, Basilo lost 1 leaves")
                leaves = leaves -1
                soil = soil + 3
                print()
            else:
                print("Thunderstorm on day",day,", bad luck, - 2 leaves.")
                leaves = leaves - 2
                flowers = flowers - 1
                soil = soil + 1

                # we must count the day outside of the "ifs" to save time, days are looping through still
        elif weather == "partly cloudy":
            if wind < 3:
                leaves = leaves + 1
            else:
                leaves = leaves - 1

        else:
            print("It was a boring day... nothing happened")
        print("Today was",weather,", the wind was",wind,"and the soil is at",soil,".")

        day = day + 1
        if leaves == 0:
            leaves = leaves + 2
         
    # the higher the wind the more leaves we lose
    # add flowers every x days

print(" BASILO WAS BORN! 🫠")

run_simulation()
print()
print(f"Leaves =",abs(leaves), "Flowers =",abs(flowers),"soil =",abs(soil))

print("Basilo is",day,"days old.")

print("bye")
