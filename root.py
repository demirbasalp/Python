#a x^2- b 6x+ c 5
# d = b^2-4ac
#r1= -

from math import sqrt

a= int(input("A katsay�s�n� giriniz:"))
b= int(input("B katsay�s�n� giriniz:"))
c= int(input("C katsay�s�n� giriniz:"))

d= b**2-4*a*c

x1 = (-1*b - sqrt(d) ) / (2*a)
x2 = (-1*b + sqrt(d) ) / (2*a)

print(x1)
print(x2)

