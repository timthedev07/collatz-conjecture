from typing import List
import numpy as np
import matplotlib.pyplot as plt


def main():
    data = loadData("../out/digits.txt")


"""Read digits.txt"""


def loadData(path: str) -> List[float]:
    with open(path, "r") as file:
        lines = file.readlines()
        print(line for line in lines)

        return []


if __name__ == "__main__":
    main()
