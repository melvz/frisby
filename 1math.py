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

# "XV" is the area variable
xv = y * h1 * h2 * h3


#let's get the sqrt of the area variable
ab = math.sqrt( xv )

print ab
