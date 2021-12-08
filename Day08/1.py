with open(r"input.txt") as f:
    values = f.read().split('\n')

    possible_digits = ["abcdefg", "cf", "bcg", "bceg"]

    total = 0

    for value in values:
        digits = value.split("|")[1].strip()

        digits = digits.split(" ")
        for digit in digits:
            if len("".join(sorted(digit))) in [2, 3, 4, 7]:
                total += 1

    print(total)