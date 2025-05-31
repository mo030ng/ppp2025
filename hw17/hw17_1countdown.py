import time
import tkinter as tk
from tkinter import simpledialog
import rich

window = tk.Tk()
window.withdraw()

def gui_input(text):
    return simpledialog.askstring(title="입력창", prompt=text)

def count_down(count):

    for n in range(count):
        rich.print(f"[bold blue]{count - n}!![/bold blue]" , end= "\r")
        time.sleep(1)
    rich.print(f"[bold red]BOMB!![/bold red] :boom:")

def main():
    countdown = gui_input("몇 초를 카운트할까여?")

    count = int(countdown)
    rich.print(f"[bold green]{count}초 후 폭발함!!!!!!!!!![/bold green] :bomb:") 
    count_down(count)


if __name__ == '__main__':
    main()