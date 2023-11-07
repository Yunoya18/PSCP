"""NumDays"""
def main():
    """calculate"""
    day_1 = int(input())
    month_1 = int(input())
    day_2 = int(input())
    month_2 = int(input())
    dayin_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day_1 > dayin_month[month_1-1] or day_2 > dayin_month[month_2-1]:
        print("Impossible")
    else:
        diff = abs((day_1 + sum(dayin_month[:month_1-1])) - (day_2 +sum(dayin_month[:month_2-1])))
        print(diff)
 
main()
