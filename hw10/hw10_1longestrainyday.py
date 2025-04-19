def get_weather_data(fname,col_idx):
    weather_datas = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_datas.append(float(tokens[col_idx]))
    return weather_datas

def get_rain_events(rainfalls):
    events=[]
    c_days = 0
    for rain in rainfalls:
        if rain > 0:
            c_days += 1
        else: 
            if c_days > 0:
                events.append(c_days)
            c_days = 0
    if c_days > 0:
        events.append(c_days)
    print(events)
    return events

def main():
    filename = './hw10/weather(146)_2022-2022 (2).csv'
    rainfalls = get_weather_data(filename, 9)
    print(f"최장강우일수는 {max(get_rain_events(rainfalls))}일")

if __name__=='__main__':
    main()