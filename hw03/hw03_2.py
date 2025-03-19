import math


weight=int(input("몸무게는 몇kg입니까?"))
height=int(input("키는 몇cm입니까?"))
height_m= height/100
BMI=weight/pow(height_m,2)
print("키는 {}, 몸무게는 {}, BMI= {}". format(height,weight,BMI))