a=int(input("밑변은 몇 입니까?"))
b=int(input("윗변은 몇 입니까?"))
h=int(input("높이는 몇 입니까?"))
c=(a+b)*h/2
print("윗변={}, 아랫변={}, 높이={}일 떄, 사다리꼴의 면적={}입니다.".format(b,a,h,c))