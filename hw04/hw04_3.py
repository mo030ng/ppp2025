sh=int(input("샤인머스켓을 몇 g 드셨습니까? (100g 단위)"))
chp=int(input("천도복숭아를 몇 g 드셨습니까? (100g 단위)"))
wm=int(input("수박을 몇 g 드셨습니까? (100g 단위)"))

calories={"샤인머스켓":66, "천도복숭아":32, "수박":31}
sh_cal= sh/100* calories["샤인머스켓"]
chp_cal= chp/100* calories["천도복숭아"]
wm_cal= wm/100* calories["수박"]

total_calories= sh_cal+chp_cal+wm_cal
print("당신이 먹은 과일의 총 칼로리는 {}입니다.".format(total_calories))
