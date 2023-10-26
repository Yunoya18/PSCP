"""Day2011"""
def main():
    """calculate"""
    day = int(input())
    month = int(input())
    month_daylist = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_day = day + sum(month_daylist[:month-1])
    if total_day % 7 == 1:
        print("Saturday")
    elif total_day % 7 == 2:
        print("Sunday")
    elif total_day % 7 == 3:
        print("Monday")
    elif total_day % 7 == 4:
        print("Tuesday")
    elif total_day % 7 == 5:
        print("Wednesday")
    elif total_day % 7 == 6:
        print("Thursday")
    elif total_day % 7 == 0:
        print("Friday")

main()
