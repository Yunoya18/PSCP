"""OTP"""
def main():
    """process"""
    while True:
        num = input()
        if num == "0":
            break
        else:
            num_dict = {}
            for i in num:
                num_dict[i] = num_dict.get(i, 0) + 1
            num_value = list(num_dict.values())
            if len(num) == 4 and num_value.count(2) == 1:
                print("Valid")
            elif len(num) == 6 and (num_value.count(2) == 2 or num_value.count(3) == 1):
                print("Valid")
            elif len(num) == 8 and (num_value.count(2) == 3 or num_value.count(3) == 2):
                print("Valid")
            else:
                print("Invalid")

main()
