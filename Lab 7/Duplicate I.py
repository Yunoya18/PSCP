"""Duplicate I"""
def main():
    """process"""
    first_num = int(input())
    second_num = int(input())
    first_set = set()
    second_set = set()
    for _ in range(first_num):
        first_set.add(input())
    for _ in range(second_num):
        second_set.add(input())
    final_set = first_set.intersection(second_set)
    if len(final_set) == 0:
        print("Nope")
    else:
        for i in reversed(sorted(final_set)):
            print(i)

main()
