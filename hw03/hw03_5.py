sh=int(input("샤인머스켓을 몇 g 드셨습니까? (100g 단위)"))
chp=int(input("천도복숭아를 몇 g 드셨습니까? (100g 단위)"))
wm=int(input("수박을 몇 g 드셨습니까? (100g 단위)"))

sh_kcal=sh/100*66
chp_kcal=chp/100*32
wm_kcal=wm/100*31
a= sh_kcal+chp_kcal+wm_kcal
print("당신이 먹은 과일의 총 칼로리는 {}입니다.".format(a))