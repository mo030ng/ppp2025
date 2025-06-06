import matplotlib.pyplot as plt
import numpy as np
import requests
import pandas as pd

def download_weather(station_id, year, filename):
    URL = f"https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv"
    with open(filename, "w", encoding="UTF-8-sig") as f:
        resp = requests.get(URL) 
        resp.encoding = "UTF-8"
        f.write(resp.text)

def main():
    filename = "./weather(146)_2015.csv"
    download_weather(146, 2015, filename)

    df = pd.read_csv(filename, skipinitialspace=True)
    df["tdiff"] = df["tmax"] - df["tmin"]
    
    fig, ax = plt.subplots()
    df["date"] = pd.to_datetime(df[["year", "month", "day"]])
    df.plot("date", "tavg", ax= ax)
    # df.plot("day", "tavg" ax=ax)
    plt.show()

if __name__ == "__main__":
    main()


import matplotlib.pyplot as plt
import numpy as np
def main():
    dices = np.random.randint(1,7, size = 12345)
    print(dices)

    fig, ax = plt.subplots()

    ax.hist(dices, bins=6, color="skyblue")
    plt.show()

if __name__ == '__main__':
    main()
