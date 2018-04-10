import math



P = input("enter P: ")

Y = input("enter Y: ")

R = input("enter R: ")





n = 12 * Y

d = 12 * 100

r = float(R) / d



e = (1 - r) ** n





numerator = P * r

denom = 1 - e





payment = float(numerator) / denom



print payment

#######
