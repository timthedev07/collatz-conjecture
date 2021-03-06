import sys
from tqdm import tqdm
from src.utils import collatzArr


def main():

    data = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
    }

    # number of samples
    N: int = 1000000

    totalNums = 0

    for i in tqdm(range(1, N + 1)):
        hailstoneNumbers = collatzArr(i, True)

        for hailstoneNumber in hailstoneNumbers:
            data[int(hailstoneNumber[0])] += 1
            totalNums += 1

    percentages = {k: (lambda x: f"{round((x / totalNums) * 100, 2)}%")(v) for k, v in data.items()}

    with open("../../out/digits.txt", "w") as f:
        f.writelines(list(map((lambda kv: f"Digit {kv[0]}: {kv[1]}\n"), percentages.items())))
        f.write("\nOriginal data:\n")
        f.writelines(list(map((lambda kv: f"Digit {kv[0]}: {kv[1]}\n"), data.items())))


if __name__ == "__main__":
    main()
