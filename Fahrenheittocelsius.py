"""
Namn: Rasmus Hén
Operativsystem: Windows 10
"""

print("Hallå där, välkommen till konverteraren!")

while True: #Starts a loop that continues as long as the input isn't valid
    try: #Tests if the input gives a ValueError
        fahrenheit = float(input("Hur många grader Fahrenheit vill du konvertera till Celsius? "))
        break
    except ValueError:
        print("Fel typ av input")

celsius = (fahrenheit - 32) * 5 / 9 #Changes Fahrenheit to Celsius

celsius = str("{:.2f}".format(celsius))#Rounds off to 2 decimals and changes to string
#celsius = str(round(celsius, 2)) A different way to round off to 2 decimals and change to string

print("Hej igen, temperaturen i Celsius är:", celsius)

