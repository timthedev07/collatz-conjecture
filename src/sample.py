import numpy as np
import matplotlib.pyplot as plt
from src.utils import collatzArr
from math import log


# this program computes the frequency of each digit being a leading digit among all computed hailstone numbers
def main():
    inputs: list[int] = [7, 26, 72101241]
    X_LABEL: str = "Stopping Points"
    Y_LABEL: str = "Hailstone numbers"

    for n in inputs:
        plt.figure(figsize=(9.5, 4))

        data = collatzArr(n)

        logarithmic = list(map(lambda x: log(x), data))

        x = np.arange(len(data))

        plt.subplots_adjust(left=0.1, bottom=0.2, right=0.9, top=0.9, wspace=0.4, hspace=0.4)

        # first subplot
        plt.subplot(121)
        plt.plot(x, data)
        plt.title("Normal Sample")
        plt.xlabel(X_LABEL)
        plt.ylabel(Y_LABEL)

        # second subplot
        plt.subplot(122)
        plt.plot(x, logarithmic)
        plt.title("Logarithmic Sample")
        plt.xlabel(X_LABEL)
        plt.ylabel(Y_LABEL)

        plt.savefig(f"../../out/plots/samples/n={n}.svg")


if __name__ == "__main__":
    main()
