"""PH"""
def main():
    """process"""
    check_ph = float(input())
    if 0 <= check_ph <= 14:
        if check_ph < 7:
            print("acidic")
        elif check_ph == 7:
            print("neutral")
        else:
            print("akaline")
    else:
        print("error")

main()
