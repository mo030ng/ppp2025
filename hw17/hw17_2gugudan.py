import random
import tkinter as tk
from tkinter import simpledialog
import rich

window = tk.Tk()
window.withdraw()

def gui_input(text):
    return simpledialog.askstring(title="입력창", prompt=text)

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
    # name = gui_input("이름이 먼가욤?")
    name = "듀랑이"
    rich.print(f"[bold magenta]{name}[/bold magenta]님 반가워요!!!!!!!!! :rice:")
def main():
    score = 0
    total_problem = 5
    for n in range(total_problem):
        is_correct = problem()
        if is_correct:
            score += 1
    rich.print(f"[bold blue]{score}개 맞췄으니까 {score / total_problem *100:.0f}점 입니다!!!!!![/bold blue]")
    if (score / total_problem * 100) >= 80:
        rich.print(f"[bold white]님 정말 천재시군요!!!!!!!!!!!! 아 안되겟다 제가 천재인증서 드릴게여[/bold white]")
        rich.print(f"             [bold red]:star: 천 재 인 증 서 [/bold red]:star:         ")
        rich.print("")
        rich.print(f"                         [bold red]성 명 : 이 문제를 푼 님!!!!!!!!!!!!!!!![/bold red]:heart:")
        rich.print("")
        rich.print(f"[bold yellow]위 상장은 구구단을 진짜진짜 잘하는 님한테만 드리는건데[/bold yellow]")
        rich.print(f"[bold yellow]그게 진짜 님이라서 제가 더 자랑스러워요[/bold yellow]")
        rich.print(f"[bold yellow]구구단 진짜 잘하신다!!!!!! 축하드려요오오오[/bold yellow]")
        rich.print("")
        rich.print(f"           [bold white]전북대학교 총장 양 오 봉[/bold white]:trophy:")
    else:
        print("조금만 더 열심히 하면 천재 바로 할 수 잇을거가튼데여?!?! 님 화이팅!!!!")

if __name__ == '__main__':
    main()