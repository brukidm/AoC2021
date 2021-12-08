with open(r"input.txt") as f:
    values = f.read().split('\n')
    total = 0
    for value in values:
        decoder = {}
        codes, digits = value.split(" | ")
        codes, digits = codes.strip(), digits.strip()

        codes = sorted(codes.split(" "), key=len)

        code_1 = "".join(sorted(codes[0]))
        code_7 = "".join(sorted(codes[1]))
        code_8 = "".join(sorted(codes[-1]))
        code_4 = "".join(sorted(codes[2]))

        code_4_8_diff = ""
        for c in code_8:
            if c not in code_4:
                code_4_8_diff += c

        five_digit_codes = codes[3:6]
        six_digit_codes = codes[6:9]

        for code in five_digit_codes:
            if code_1[0] in code and code_1[1] in code:
                code_3 = code
            else:
                for c in code_4_8_diff:
                    if c not in code:
                        code_5 = code

        five_digit_codes.remove(code_5)
        five_digit_codes.remove(code_3)
        code_2 = five_digit_codes.pop()
        code_2 = "".join(sorted(code_2))
        code_3 = "".join(sorted(code_3))
        code_5 = "".join(sorted(code_5))
        
        for code in six_digit_codes:
            if not(code_1[0] in code and code_1[1] in code):
                code_6 = code
            else:
                for c in code_4_8_diff:
                    if c not in code:
                        code_9 = code

        six_digit_codes.remove(code_6)
        six_digit_codes.remove(code_9)
        code_0 = six_digit_codes.pop()
        code_0 = "".join(sorted(code_0))
        code_6 = "".join(sorted(code_6))
        code_9 = "".join(sorted(code_9))

        decoder = {
            code_0: "0",
            code_1: "1",
            code_2: "2",
            code_3: "3",
            code_4: "4",
            code_5: "5",
            code_6: "6",
            code_7: "7",
            code_8: "8",
            code_9: "9",
        }
        number = ""
        for digit in digits.split(" "):
            number += decoder["".join(sorted(digit))]
        print(number)
        total += int(number)
    print(total)