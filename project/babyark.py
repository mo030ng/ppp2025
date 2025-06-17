import tkinter as tk
import random
import webbrowser

# 가격대별 식당 목록
restaurants = {
    "만원이하": [
        ("하루샤브", "https://naver.me/IGJy9WBQ"),
        ("면식당", "https://naver.me/502M34gw"),
        ("모두랑떡볶이", "https://naver.me/xoHiTay1"),
        ("황제보쌈", "https://naver.me/Gq84Chej"),
        ("덕천식당", "https://naver.me/513Nymt0"),
        ("도야짬뽕", "https://naver.me/Grmaya0K"),
        ("롤링파스타", "https://naver.me/xmxeLSzp"),
        ("육쌈냉면", "https://naver.me/5UT0228h"),
    ],
    "만원대": [
        ("고수닭갈비", "https://naver.me/FQVvNF10"),
        ("만배식탁", "https://naver.me/5ZJxa0ar"),
        ("백소정", "https://naver.me/GFBha9Ym"),
        ("고기듬뿍 국물두루치기", "https://naver.me/GoDEDUcM"),
        ("화덕초대파불고기", "https://naver.me/F74kqy0S"),
        ("언더그라운드", "https://naver.me/Fio7tNtL"),
        ("미소야", "https://naver.me/FO9oWvPf"),
        ("청양농장", "https://naver.me/GkR3n3DW"),
    ],
    "오늘돈많음!": [
        ("계도리", "https://naver.me/IDFU27cC"),
        ("테트리스찜닭", "https://naver.me/5ZJM0VFN"),
        ("해브어굿테이블", "https://naver.me/xKEkF2K6 "),
        ("치히로", "https://naver.me/FTXwWIBP"),
    ],
    "마라탕" : [
        ("미미마라", "https://naver.me/5UEFbbLK"),
        ("탕화쿵푸", "https://naver.me/GQ1ZqL55"),
        ("이런이궈", "https://naver.me/FW0B6Bua")
    ]
}

# 추천된 식당 저장용
current_place = {"name": "", "link": ""}

# 추천 함수
def recommend(price):
    choice = random.choice(restaurants[price])
    current_place["name"] = choice[0]
    current_place["link"] = choice[1]
    result_label.config(text=f"오늘 밥약은 >> {choice[0]} << 에서!!! (어때??)")

# 지도 열기 함수
def open_map():
    if current_place["link"]:
        webbrowser.open(current_place["link"])

# tkinter GUI 만들기
root = tk.Tk()
root.title("오늘은 후배들과 점심약속이 있는 날!!")
root.geometry("400x350")
root.configure(bg="#FFF0F5")  # 연핑크 배경

title = tk.Label(root, text="💖 두근두근 후배와의 밥약 💖", font=("Helvetica", 16, "bold"), bg="#FFF0F5")
title.pack(pady=10)

# 버튼 만들기
btn_frame = tk.Frame(root, bg="#FFF0F5")
btn_frame.pack(pady=10)

btn_1 = tk.Button(btn_frame, text="만원이하", width=10, bg="#FFB6C1", font=("Helvetica", 12), command=lambda: recommend("만원이하"))
btn_2 = tk.Button(btn_frame, text="만원대", width=10, bg="#FF69B4", font=("Helvetica", 12), command=lambda: recommend("만원대"))
btn_3 = tk.Button(btn_frame, text="오늘돈많음!", width=10, bg="#FF1493", font=("Helvetica", 12), command=lambda: recommend("오늘돈많음!"))
btn_4 = tk.Button(btn_frame, text="마라탕", width=10, bg="#FF1493", font=("Helvetica", 12), command=lambda: recommend("마라탕"))

root.geometry("500x250")

btn_1.grid(row=0, column=0, padx=5)
btn_2.grid(row=0, column=1, padx=5)
btn_3.grid(row=0, column=2, padx=5)
btn_4.grid(row=0, column=3, padx=5)

# 결과 출력
result_label = tk.Label(root, text="너의 지갑 상황에 맞춰\n 밥약하기 좋은 맛집들을 알려줄게!!!!", font=("Helvetica", 13), bg="#FFF0F5")
result_label.pack(pady=20)

# 지도 열기 버튼
map_btn = tk.Button(root, text="📍 지도 열기", command=open_map, bg="#FFB6C1", font=("Helvetica", 12))
map_btn.pack()

root.mainloop()
