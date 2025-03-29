

def c2f(tc):
    return (tc*5/9)+32

def main():
    temp_c=int(input("화씨로 변환할 섭씨온도를 입력하세요: "))
    temp_f= c2f(temp_c)
    print(f"{temp_c}C => {temp_f:.3f}F")

    
if __name__=="__main__":
    main()


