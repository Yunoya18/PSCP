"""Temperature"""
def main():
    """convert"""
    temp = float(input())
    con_from = input()
    con_to = input()
    if con_from == "F":
        temp = (temp - 32) * (5/9)
    elif con_from == "K":
        temp = temp - 273.15
    elif con_from == "R":
        temp = (temp * (5/9)) - 273.15
    if con_to == "F":
        temp = temp * (9/5) + 32
    elif con_to == "K":
        temp = temp + 273.15
    elif con_to == "R":
        temp = (temp + 273.15) * (9/5)
    print("%.2f" % temp)

main()
