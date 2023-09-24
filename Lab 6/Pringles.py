"""Pringles"""
def main():
    """process"""
    etc1 = input()
    pringle = input()
    etc2 = input()
    lenght = int(input())
    count_before = pringle.count(")")
    left = (" " * lenght) + pringle[lenght:]
    count_after = left.count(")")
    count_left = count_before - count_after
    print(count_left)
    if count_after == 0:
        print("None.")
    else:
        print("There are still some left.")
    print(etc1)
    print(left)
    print(etc2)

main()
