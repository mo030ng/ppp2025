import math


weight=int(input("몸무게는 몇kg입니까?"))
height=int(input("키는 몇cm입니까?"))
height_m= height/100
BMI=weight/pow(height_m,2)

print (BMI)
if BMI>=23 and BMI<=24.9 :
    print("당신은 비만 전단계 입니다.")
elif BMI>=25 and BMI<=29.9 :
    print("당신은 1단계 비만 입니다.")
elif BMI>=30 and BMI<=34.9 :
    print("당신은 2단계 비만입니다.")
elif 35<=BMI:
    print("당신은 3단계 비만입니다.")

