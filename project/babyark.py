import tkinter as tk
import random
import webbrowser

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

favorites = []
current_place = {"name": "", "link": ""}

def recommend(price):
    choice = random.choice(restaurants[price])
    current_place["name"] = choice[0]
    current_place["link"] = choice[1]
    result_label.config(text=f"🍽️ 추천 식당: {choice[0]}")

def open_map():
    if current_place["link"]:
        webbrowser.open(current_place["link"])

def add_favorite():
    if current_place["name"] and current_place not in favorites:
        favorites.append(current_place.copy())
        result_label.config(text=f"⭐ '{current_place['name']}' 찜했어요!")

def random_from_favorites_popup():
    popup = tk.Toplevel(root)
    popup.title("여기 중에 어디를 가야 좋을까??")
    popup.geometry("320x320")
    popup.configure(bg="#DDEEFF")

    tk.Label(popup, text="계속 고민된다면, 내가 결정해줄게!!!", font=("Helvetica", 13), bg="#DDEEFF").pack(pady=10)

    # 최종 식당 결정 버튼
    pick_btn = tk.Button(popup, text="오늘 밥약은?", font=("Helvetica", 14, "bold"),
                         bg="#3399FF", fg="white", width=12, height=2, relief="raised")
    pick_btn.pack(pady=10)

    # 결과 영역 (pick_btn 바로 아래에 생성됨)
    result_frame = tk.Frame(popup, bg="#DDEEFF")
    result_frame.pack()

    def choose_one():
        # 기존 결과 제거
        for widget in result_frame.winfo_children():
            widget.destroy()

        if favorites:
            choice = random.choice(favorites)

            # 결과 출력
            result_label = tk.Label(result_frame, 
                text=f"요기 오때 → {choice['name']}", 
                font=("Helvetica", 14, "bold"),
                bg="#DDEEFF"
            )
            result_label.pack(pady=10)

            # 지도 열기 버튼
            map_btn = tk.Button(result_frame, text="📍 지도 열기", command=lambda: webbrowser.open(choice['link']),
                                bg="#3399FF", fg="white", font=("Helvetica", 11))
            map_btn.pack()
        else:
            tk.Label(result_frame, text="찜한 식당이 없어요!", bg="#DDEEFF", font=("Helvetica", 11)).pack()

    # 버튼에 기능 연결
    pick_btn.config(command=choose_one)

def show_favorites():
    def delete_favorite(item):
        favorites.remove(item)
        fav_window.destroy()
        show_favorites()

    fav_window = tk.Toplevel(root)
    fav_window.title("⭐ 찜한 식당 목록")
    fav_window.geometry("350x450")
    fav_window.configure(bg="#E6F0FA")

    tk.Label(fav_window, text="💙 찜한 맛집들 💙", font=("Helvetica", 14, "bold"), bg="#E6F0FA").pack(pady=10)

    for item in favorites:
        frame = tk.Frame(fav_window, bg="#E6F0FA")
        frame.pack(fill="x", pady=2, padx=10)

        name_btn = tk.Button(frame, text=item["name"], bg="#A7C7E7", font=("Helvetica", 12),
                             command=lambda l=item["link"]: webbrowser.open(l))
        name_btn.pack(side="left", fill="x", expand=True)

        del_btn = tk.Button(frame, text="❌", bg="#4682B4", fg="white", font=("Helvetica", 10, "bold"),
                            command=lambda i=item: delete_favorite(i))
        del_btn.pack(side="right")

    # "뭘 먹어야 하지?" 버튼
    think_btn = tk.Button(fav_window, text="여기 중에 오디가까??",
                          font=("Helvetica", 12), bg="#6FA8DC",
                          command=random_from_favorites_popup)
    think_btn.pack(pady=20)

#  메인 UI
root = tk.Tk()
root.title("후배들과의 밥약!!! ")
root.geometry("500x350")
root.configure(bg="#E6F0FA")

title = tk.Label(root, text="💙 후배들과의 밥약 💙", font=("Helvetica", 16, "bold"), bg="#E6F0FA")
title.pack(pady=10)

btn_frame = tk.Frame(root, bg="#E6F0FA")
btn_frame.pack(pady=10)

btn_1 = tk.Button(btn_frame, text="만원이하", width=10, bg="#A7C7E7", font=("Helvetica", 12), command=lambda: recommend("만원이하"))
btn_2 = tk.Button(btn_frame, text="만원대", width=10, bg="#6FA8DC", font=("Helvetica", 12), command=lambda: recommend("만원대"))
btn_3 = tk.Button(btn_frame, text="오늘돈많음!", width=10, bg="#357ABD", fg="white", font=("Helvetica", 12), command=lambda: recommend("오늘돈많음!"))
btn_4 = tk.Button(btn_frame, text="마라탕", width=10, bg="#357ABD", fg="white", font=("Helvetica", 12), command=lambda: recommend("마라탕"))

btn_1.grid(row=0, column=0, padx=5)
btn_2.grid(row=0, column=1, padx=5)
btn_3.grid(row=0, column=2, padx=5)
btn_4.grid(row=0, column=3, padx=5)

result_label = tk.Label(root, text="너의 지갑 사정에 맞는 가격대를 눌러봐!\n(일인분 기준 가격이야 !!)", font=("Helvetica", 13), bg="#E6F0FA")
result_label.pack(pady=20)

map_btn = tk.Button(root, text="📍 지도 열기", command=open_map, bg="#A7C7E7", font=("Helvetica", 12))
map_btn.pack(pady=5)

favorite_btn = tk.Button(root, text="⭐ 찜하기", command=add_favorite, bg="#00BFFF", font=("Helvetica", 12))
favorite_btn.pack(pady=5)

show_btn = tk.Button(root, text="📋 찜 목록 보기", command=show_favorites, bg="#6FA8DC", font=("Helvetica", 12))
show_btn.pack(pady=5)

root.mainloop()
