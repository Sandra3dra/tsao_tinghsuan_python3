print("This is the conditions file")

current_temp = False

while current_temp is False:
    current_temp = input("Enter a temperture: \n")
    print(current_temp)

    if (int(current_temp) <0) or (int(current_temp) == 0):
        print("water is a solid. Icy!")
        current_temp = False

    elif (int(current_temp) <100):
        print("Water is a liquid. Profit!")
        current_temp = False

    elif (int(current_temp) >100) or (int(current_temp) == 100):
        print("Water is a vapor cuz it's HOT!")
        current_temp = False
