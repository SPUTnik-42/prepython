import math 

a = int(input("INPUT THE SIDE OF THE TRIANGLE "))
b = int(input("INPUT THE SECOND SIDE OF THE TRIANGLE "))
c = int(input("INPUT THE THIRD SIDE OF THE TRIANGLE "))
s = (a+b+c)/ 2
area = sqrt(s(s-a)(s-b)(s-c))

print("the area of the triangle is " , area)