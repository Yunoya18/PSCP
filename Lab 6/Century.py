"""Century"""
import math
def main():
    """calculate"""
    num = int(input())
    for _ in range(num):
        text = input()
        if "A.D." in text:
            text = text.replace("A.D. ", "")
            year = int(text)
            if year > 0:
                year = math.ceil(year/100)
                print(year)
            else:
                print("ERROR")
        elif "B.E." in text:
            text = text.replace("B.E. ", "")
            year = int(text) - 543
            if year > 0:
                year = math.ceil(year/100)
                print(year)
            else:
                print("ERROR")
        else:
            print("ERROR")

main()
