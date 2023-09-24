"""Lotto"""
def main():
    """calculate"""
    prize_one = input()
    two_digit_prize = input()
    first_three_digit_prize1 = input()
    first_three_digit_prize2 = input()
    end_three_digit_prize1 = input()
    end_three_digit_prize2 = input()
    num = input()
    total = 0
    if prize_one == "000000":
        close1 = "000001"
        close2 = "999999"
    elif prize_one == "999999":
        close1 = "000000"
        close2 = "999998"
    else:
        close1 = "%06d" % (int(prize_one) + 1)
        close2 = "%06d" % (int(prize_one) - 1)
    if num == prize_one:
        total += 6000000
    if num[-2:] == two_digit_prize:
        total += 2000
    if num[:3] == first_three_digit_prize1:
        total += 4000
    if num[:3] == first_three_digit_prize2:
        total += 4000
    if num[-3:] == end_three_digit_prize1:
        total += 4000
    if num[-3:] == end_three_digit_prize2:
        total += 4000
    if num == close1 or num == close2:
        total += 100000
    print(total)

main()
