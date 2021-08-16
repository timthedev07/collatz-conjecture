from typing import List
import numpy as np
import matplotlib.pyplot as plt


def main():
    # frequency of numbers in range 1...9
    data = loadData("../../out/digits.txt")

    plt.plot(data)
    plt.fill_between(list(range(len(data))), data)
    plt.show()


"""Read digits.txt"""


def loadData(path: str) -> List[int]:
    with open(path, "r") as file:
        lines = file.readlines()
        nums = list(map((lambda x: int(x[9:])), lines[11:]))
        return nums


if __name__ == "__main__":
    main()
