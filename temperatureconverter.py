# Function 1 Start
def category(category):
    while True:
        category_01 = input(category)
        if category_01 in ["A","B","C","D","E","F"]:
            print("You choosed category:", category_01)
            return category_01
        print("Only A,B,C,D,E and F are allowed. Please type any one of following\nA\nB\nC\nD\nE\nF")
"""
The fun. will get the category from the user
"""
# Fuction 1 Completed
# Function 2 Starts
def temp_001(temperature):
    while True:
        temperature_01 = input(temperature)
        try:
            temperature_ = float(temperature_01)
            print(f"The temperature is: {temperature_}")
            return temperature_
        except ValueError:
            print("You entered an incorrect format! Letters are not allowed. Only numbers please!\n")
            """
            The function will keep asking for input until a valid number is entered. If the user enters something that cannot be converted to a float, it will catch the ValueError and prompt the user again.
            """
# Function 2 Completed
# Functions End
# Program Starts


    print("What unit do you want to convert:\nA\tCelsius → Kelvin\nB\tKelvin → Celsius\nC\tCelsius → Fahrenheit\nD\tFahrenheit → Celsius\nE\tFahrenheit → Kelvin\nF\tKelvin → Fahrenheit")

askcat = category("What type of conversion are you looking for (e.g. A,B,C,D,E OR F):")
asktem = temp_001(f"Enter the temperature:\t")
celtokel = asktem + 273.15
keltocel = asktem - 273.15
celtofah = asktem * 9/5+32
fahtocel = (asktem - 32)*5/9
fahtokel = (asktem - 32)*5/9+273.15
keltofah = (asktem - 273.15)*9/5+32 

if (askcat == "A"):
    print(f"To convert Celsius → Kelvin we use formula:\tK=C+273.15\nand by using the formula the final answer is {celtokel}K")
elif(askcat == "B"):
     print(f"To convert Kelvin → Celsius we use formula:\tC=K−273.15\nand by using the formula the final answer is {keltocel}°C")
elif(askcat == "C"):
     print(f"To convert Celsius → Fahrenheit we use formula:\tF=C*9/5+32\nand by using the formula the final answer is {celtofah}°F")
elif(askcat == "D"):
    print(f"To convert Fahrenheit → Celsius we use formula:\tC=(F-32)*5/9\nand by using the formula the final answer is {fahtocel}°C")
elif(askcat == "E"):
    print(f"To convert Fahrenheit → Kelvin we use formula:\tK=(F-32)*5/9+273.15\nand by using the formula the final answer is {fahtokel}K")
elif(askcat == "F"):
     print(f"To convert Kelvin → Fahrenheit we use formula:\tF=(K-273.15)*9/5+32\nand by using the formula the final answer is {keltofah}°F")
    






