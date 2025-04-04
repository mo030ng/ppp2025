def get_range_list(n):
    return list(range(1,1-n-1,-1))

def main():
    n= int(input("n값을 입력하세요: "))
    print(get_range_list(n))

if __name__=="__main__":
    main()