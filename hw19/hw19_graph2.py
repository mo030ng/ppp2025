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
