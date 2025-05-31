import random
import tkinter as tk
from tkinter import simpledialog
import rich

window = tk.Tk()
window.withdraw()

def gui_input(text):
    return simpledialog.askstring(title="입력창", prompt=text)

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
            rich.print(f"[bold green] {input_ch}가 포함되어잇음!!!!![/bold green]")
        else:
            rich.print("당신이 생각하는 그 단어가 아닌거가튼데요?? 그 글자 아녜욤..")
            heart -= 1
            rich.print(f"[bold red]남은 기회는 단{heart}번!!![/bold red]")

        if "_" not in answer:
            is_correct = True
            break
        
        if heart <= 0:
            break
    
    if is_correct:
        rich.print(f"[bold magenta]님 완전 천재!!!!!! 정답은 {solution}였답니다~[/bold magenta]")
    else:
        rich.print(f"[bold white]게임이 오버됏긔.. 좀만 더 해보셈!!!![/bold white]:sad:")
            

if __name__ == '__main__':
    main()