from typing import List, Union


"""Generate an array of numbers containing all the hailstone numbers in the sequence"""


def collatzArr(n: int, asStr: bool = False) -> List[Union[int, str]]:
    arr = []
    while n != 1:
        arr.append(n)
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1

    if asStr:
        return list(map((lambda x: str(x)), arr))

    return arr


if __name__ == "__main__":
    main()
