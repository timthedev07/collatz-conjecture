from sys import argv


def main():
    if len(argv) < 2:
        print("Invalid command line argument")
        return

    try:
        n = int(argv[1])
    except:
        print("Invalid command line argument")
        return

    count = 0
    highest = 0

    while n != 1:
        highest = max(highest, n)
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        count += 1

    print(
        f"""Stopping time = {count}
  Highest number reached = {highest}"""
    )


if __name__ == "__main__":
    main()
