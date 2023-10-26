"""Seeker"""
def main():
    """process"""
    text = input()
    num = ""
    for i in text:
        if i.isnumeric():
            num += i
        else:
            num += " "
    num_list = list(map(int, num.split()))
    print(sum(num_list))

main()
