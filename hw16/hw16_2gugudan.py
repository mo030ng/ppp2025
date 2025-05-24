import random
def problem():
    dan = random.randint(2, 9)
    mul = random.randint(1, 9)

    try: 
        ans = int(input(f"{dan} * {mul} = "))
    except ValueError:
        return False
    
    if ans == dan*mul:
        return True
    return False

def main():
    score = 0
    total_problem = 5
    for n in range(total_problem):
        is_correct = problem()
        if is_correct:
            score += 1
    print(f"{score}개 맞췄으니까 {score / total_problem *100:.0f}점 입니다!!!!!!")
    if (score / total_problem * 100) >= 80:
        print("님 정말 천재시군요!!!!!!!!!!!! 아 안되겟다 제가 천재인증서 드릴게여")
        print("********** 천 재 인 증 서 **********")
        print("")
        print("                         성 명 : 이 문제를 푼 님!!!!!!!!!!!!!!!!")
        print("")
        print("위 상장은 구구단을 진짜진짜 잘하는 님한테만 드리는건데")
        print("그게 진짜 님이라서 제가 더 자랑스러워요")
        print("구구단 진짜 잘하신다!!!!!! 축하드려요오오오")
        print("")
        print("           전북대학교 총장 양 오 봉")
    else:
        print("조금만 더 열심히 하면 천재 바로 할 수 잇을거가튼데여?!?! 님 화이팅!!!!")

if __name__ == '__main__':
    main()