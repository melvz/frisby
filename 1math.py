import math

a = 42
b = 16
c = 32


#I assigned sub variable for "S"
s = a + b + c

y = s / 2

#I assigned sub variables for the minuses
h1 = y - a
h2 = y - b
h3 = y - c


xv = y * h1 * h2 * h3


#this is the area variable
ab = math.sqrt( xv )

print ab
