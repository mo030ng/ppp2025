def sum_n(n):
    total=0
    for i in range(1,n+1):
        total+=i
    return total

def main():
    n=int(input("숫자를 입력하세요: "))
    total=sum_n(n)
    print(f"1부터 {n}까지의 합은 {total} 입니다. ")

if __name__=="__main__":
    main()