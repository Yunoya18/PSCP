"""FourDirections"""
def main():
    """process"""
    text = input()
    row1 = ""
    row2 = ""
    row3 = ""
    row4 = ""
    row5 = ""
    for i in text:
        if i == "U":
            row1 += "  *   "
            row2 += " ***  "
            row3 += "* * * "
            row4 += "  *   "
            row5 += "  *   "
        elif i == "D":
            row1 += "  *   "
            row2 += "  *   "
            row3 += "* * * "
            row4 += " ***  "
            row5 += "  *   "
        elif i == "L":
            row1 += "  *   "
            row2 += " *    "
            row3 += "***** "
            row4 += " *    "
            row5 += "  *   "
        elif i == "R":
            row1 += "  *   "
            row2 += "   *  "
            row3 += "***** "
            row4 += "   *  "
            row5 += "  *   "
    print(row1, row2, row3, row4, row5, sep="\n")

main()
