def max_temp_gap_year(dates,tmax,tmin):
    year_max={}
    for i in range(len(dates)):
        year, month, day = dates[i]
        tx = tmax[i]
        tm = tmin[i]
        gap = tx - tm
        if year not in year_max:
            year_max[year] = ([year, month, day], gap)
        else:
            if gap > year_max[year][1]:
                year_max[year] = ([year, month, day], gap)

    return year_max

def get_weather_data(fname, col_idx):
    weather_datas = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_datas.append(float(tokens[col_idx]))
    return weather_datas

def get_weather_date(fname):
    weather_dates = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_dates.append([int(tokens[0]), int(tokens[1]), int(tokens[2])])
    return weather_dates 


def main():
    filename = "./hw11/weather(146)_2001-2022.csv"
    dates = get_weather_date(filename)
    tmax = get_weather_data(filename, 3)
    tmin = get_weather_data(filename, 5)
    year_max_gap = max_temp_gap_year(dates, tmax, tmin)
    for year in sorted(year_max_gap.keys()):
        max_gap_date, max_gap = year_max_gap[year]
        # print(f"일교차가 가장 큰 일자는 {max_gap_date}이고, 해당일의 일교차는 {max_gap:.1f}도 입니다.")
        print(f"{year}년, {max_gap_date[1]}일, {max_gap_date[2]}일, {max_gap:.1f}도")

if __name__ == "__main__":
    main()



def gdd(tavg):
    temp_cum = 0
    base_temp = 5
    for t in tavg: 
        if t >= base_temp:
            temp_cum += (t-base_temp)
    return temp_cum

def gdd_season(tavg, dates):
    gdd_year = {}
    base_temp = 5
    for i in range(len(tavg)): 
        t = tavg[i]
        year, month, day = dates[i]
        if month in [5,6,7,8,9] :
            if t >= base_temp:
                if year not in gdd_year:
                    gdd_year[year] = 0
                    gdd_year[year] += (t-base_temp)
    return gdd_year

def main():
    filename = "./lec/weather(146)_2001-2022.csv"
    dates = get_weather_date (filename)
    tavg = get_weather_data (filename, 4)
    gdd_by_year = gdd_season(tavg, dates)

    for year in sorted(gdd_by_year.keys()):
        print(f"{year}년, {gdd_by_year[year]:.1f}도")

if __name__ =="__main__":
    main()