# Maddox: 2
# Isaac: 3


# 1) Takes two values (feet and inches) and converts to meters
#freaky_feet = float(input("Enter feet: "))
#winches = float(input("Enter inches: "))
#meters = (freaky_feet * 0.3048) + (winches * 0.0254)
#print(f"{freaky_feet} ft {winches} in is equal to {meters} m.")


# 2) Changes coordinates from polar to Cartesian
from cmath import cos, sin
r = float(input("Enter radius: "))
teeta = float(input("Enter angle in deg: "))
teeta_rad = teeta*(3.14159/180) # this is da formula theta*pi/180deg which is used to convert deg to rad
x = r*cos(teeta_rad) # polar to cart formula
y = r*sin(teeta_rad) # also polar to cart formula
print(f"The polar coordinates (r={r}, θ={teeta}°) are (x={x}, y={y}) in cartesian coordinates.")


