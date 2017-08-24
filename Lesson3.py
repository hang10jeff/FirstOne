wind = eval(input("Enter wind speed: "))

if wind >= 74 and wind <= 95:
    print ("Cat1")
elif wind >= 96 and wind <= 110:
    print ("Cat2")
elif wind >= 111 and wind <= 130:
    print ("Cat3")
elif wind >= 131 and wind <= 155:
    print ("Cat4")
elif wind >= 156:
    print ("Cat5")
else:
    print ("N/A")
