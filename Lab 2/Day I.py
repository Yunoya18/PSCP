"""Day I"""
def main():
    """process"""
    year = int(input())
    if year % 4 == 0 and not year % 100 == 0:
        print("Yes")
    elif year % 100 == 0 and year % 400 == 0:
        print("Yes")
    else:
        print("No")

main()
