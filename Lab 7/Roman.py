"""Roman"""
def main():
    """calculate"""
    roman = {"I" : 1, "V" : 5, "X" : 10, "L" : 50,\
            "C" : 100, "D" : 500, "M" : 1000}
    text = input()
    total = 0
    i = 0
    while i <= len(text) - 1:
        if text[i] in roman:
            if (i+1) <= len(text) - 1:
                if roman[text[i+1]] > roman[text[i]]:
                    total += (roman[text[i + 1]] - roman[text[i]])
                    i += 2
                else:
                    total += roman[text[i]]
                    i += 1
            else:
                total += roman[text[i]]
                i += 1
    print(total)

main()
