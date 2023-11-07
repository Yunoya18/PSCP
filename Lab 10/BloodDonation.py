"""BloodDonation"""
def main():
    """process"""
    age = int(input())
    weight = int(input())
    times = int(input())
    sign = "False"
    if age == 17 or 60 <= age <= 70:
        sign = input()
    if 17 <= age <= 70:
        if (age == 17 or 60 <= age <= 70) and sign == "False":
            check = "No"
        elif times == 0 and age > 55:
            check = "No"
        else:
            if weight >= 45:
                check = "Yes"
            else:
                check = "No"
    else:
        check = "No"
    print(check)

main()
