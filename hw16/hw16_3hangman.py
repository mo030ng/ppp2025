import random

def check(solution, answer, input_ch):
    is_correct = False
    for i in range(len(solution)):
        if solution[i] == input_ch:
            answer[i] = solution[i]
            is_correct = True
    return is_correct
        
def main():
    problems = ['apple', 'banana', 'mango', 'melon', 'grape']
    solution = problems[random.randrange(len(problems))]
    is_correct = False

    heart = 5

    answer = ["_" for n in range(len(solution))]

    while True:
        input_ch = input(f"{''.join(answer)}?")

        if check(solution, answer, input_ch):
            print(f"{input_ch}가 포함되어잇음!!!!!")
        else:
            print("당신이 생각하는 그 단어가 아닌거가튼데요?? 그 글자 아녜욤..")
            heart -= 1
            print(f"남은 기회는 단{heart}번!!!")

        if "_" not in answer:
            is_correct = True
            break
        
        if heart <= 0:
            break
    
    if is_correct:
        print("님 완전 천재!!!!!!")
    else:
        print("게임이 오버됏긔.. 좀만 더 해보셈!!!!")
            

if __name__ == '__main__':
    main()