def average(nums):
    return sum(nums) / len(nums)

def get_weather_data(fname, col_idx):
    weather_datas=[]
    with open (fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_datas.append(float(tokens[col_idx]))
        return weather_datas
    
import os 
import requests

def download_weather(station_id,year,filename):
    URL = f"https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv"
    with open ("./weather_146_2020.csv", "w", encoding="UTF-8-sig") as f: 
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)

def main():
    filename = "./weather_146_2020.csv"
    if not os.path.exists(filename):
        download_weather(146, 2020, filename)

    tavgs = get_weather_data(filename,4)
    print(f"연평균기온은 {average(tavgs):.2f}도 이다.")

    rainfalls = get_weather_data(filename,9)
    count_over_5rain = len([x for x in rainfalls if x>=5])
    print(f"5mm이상 강우 일수는 {count_over_5rain}일 이다.")

    print(f"총 강수량은 {sum(rainfalls):.1f}mm 이다.")

if __name__=="__main__":
    main()