"""Difference"""
def main():
    """process"""
    num_a = int(input())
    num_b = int(input())
    set_a = set()
    set_b = set()
    for _ in range(num_a):
        set_a.add(int(input()))
    for _ in range(num_b):
        set_b.add(int(input()))
    final_set = set_a.difference(set_b)
    for i in sorted(final_set):
        print(i, end=" ")

main()
