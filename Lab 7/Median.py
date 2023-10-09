"""Median"""
def main():
    """process"""
    total = int(input())
    num_list = []
    for _ in range(total):
        num = int(input())
        num_list.append(num)
    num_list.sort()
    if total % 2 == 0:
        median = (num_list[int(total/2) - 1] + num_list[int(total/2)]) / 2
    else:
        median = num_list[int((total - 1)/2)]
    median = int(median * 10)
    median /= 10
    print(median)

main()
