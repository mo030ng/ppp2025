import math

r=int(input("반지름은 몇 입니까?"))
p=math.pi
a= pow(r,2)*p
b= 2*p*r
print("반지름 {}의 원의 둘레는 {:.1f}이고, 원의 면적은 {:.2f}이다.".format(r,b,a))