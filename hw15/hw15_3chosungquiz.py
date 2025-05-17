import random

chosung = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 
                'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

def to_chosung_ch(ch):
    if '가' <= ch <= '힣':
        return chosung[(ord(ch)- ord('가')) //588]
    else:
        return ch
    
def to_chosung(text):
    full_text = []
    for ch in text:
        full_text.append(to_chosung_ch(ch))
    return full_text

def main():
    problems = ['경민', '운학', '리우', '영재', '세민', '소희', '원희', '사쿠', '정원', '선우', '성훈']
    solution = problems[random.randrange(len(problems))]

    is_correct = False

    for i in range(5):
        answer = input(f"{to_chosung(solution)} 은 뭘까~요~???")

        if answer == solution:
            print("정답입니다!!!!!!!!!!!!!!!!!")
            is_correct = True
            break
        else:
            print("땡이에요..다시 한 번 시도해보시길!!")
    if is_correct:
        print("님 축하드려요!!!! 님은 진짜 천재임")
    else:
        print(f"게임이 오버됏어요..... ㅠㅜ 정답은 {solution} 였습니다!!!!")

if __name__ == '__main__':
    main()