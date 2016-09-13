# A
# Amount of seconds in 42:42
print(42*60+42)

# B
# miles in 10 km

print(10 * .62137) # .62137 mi in a km

#C
#volume of a sphere of radius 4 and 6
from math import pi
print("Volume of radius 4: ", pi*4**3)
print("Volume of radius 6: ", pi*6**3)

#D
#Celsius to Fahrenheit of 40deg
Fahrenheit = 9.0/5 * 40 + 32  # where 40 is Celsius

#Fahrenheit to Celsius
Celsius = (40 - 32) * 5.0/9  # where 40 is 40deg Fahrenheit

print("40 F to Celsius: ", Celsius)
print("40 C to Fahrenheit: ", Fahrenheit)

#E
#Cubes fit in a rectangular prism
side_a = int(input("Enter the length for a side of a cube: "))
cube = side_a**3
prism = side_a*(2*side_a)*(3*side_a)
print("{} amount of cubes fit in the prism".format(prism/cube))


#F
#takes vehicle 5 hr to get from a to b going 10m/s, how many km b/w a&b
total_meters = 5*(10*3600) # 60*60 = 3600, amount of seconds in an hour
km = total_meters / 1000
print("Total km for the journey was: " + str(km) + "km")
