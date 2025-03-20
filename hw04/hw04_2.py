import math

x=int(input("x의 값을 입력하세요"))
y=int(input("y의 값을 입력하세요"))


if x>0 and y>0:
    print("입력한 좌표는 제1사분면 입니다.")
elif x<0 and y>0:
    print("입력한 좌표는 제2사분면 입니다.")
elif x<0 and y<0:
    print("입력한 좌표는 제3사분면 입니다.")
elif x>0 and y<0:
    print("입력한 좌표는 제4사분면 입니다.")
else:
    print("입력한 좌표는 원점입니다.")
