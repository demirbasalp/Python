from datetime import time
from sqlite3 import Date


x = 5
q = 4.5
y = "alp"

a = 4+5

w = x+q
print(w)

w = w+3
print(w)

#type fonskiyonu

type(w)
print(x, type(x))
print(q, type(q))
print(a, type(a))
print(w, type(w))
print(y, type(y))

actualYear = 2023
birthYear = int(input("Please enter your birthyear:"))
age = actualYear - birthYear
print(age)

x += 5
print(x)

#Booleans
#Logic 

from math import sqrt

a= int(input("A katsayýsýný giriniz:"))
b= int(input("B katsayýsýný giriniz:"))
c= int(input("C katsayýsýný giriniz:"))

d= b**2-4*a*c

x1 = (-1*b - sqrt(d) ) / (2*a)
x2 = (-1*b + sqrt(d) ) / (2*a)

print(x1)
print(x2)
