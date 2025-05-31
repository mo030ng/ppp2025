import tkinter as tk
from tkinter import simpledialog
import rich
import random

window = tk.Tk()
window.withdraw()

def gui_input(text):
    return simpledialog.askstring(title="입력창", prompt=text)

def get_lotto():
    lotto_list = []
    while True:
        n = random.randint(1, 45)
        if n not in lotto_list:
            lotto_list.append(n)
        if len(lotto_list) == 6:
            break

    return sorted(lotto_list)

def main():
    lotto_num = get_lotto()
    rich.print(f"당신의 행운의 로또번호는 {lotto_num}")

if __name__ == '__main__':
    main()