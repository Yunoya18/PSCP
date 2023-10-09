"""PickThemAgain"""
def main():
    """process"""
    num = input()
    num_list = num.split()
    count = 0
    for i in reversed(num_list):
        if int(i) % 3 == 0 or int(i) % 5 == 0:
            print(i)
            count += 1
    if count == 0:
        print("Nope")

main()
