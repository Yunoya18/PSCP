"""Sequence X"""
def main():
    """process"""
    num = int(input())
    for i in range(1, num + 1):
        print("   " * (num-i), end="")
        for mmm in range(1, i + 1):
            print("%02d" % mmm, end=" ")
        for nnn in reversed(range(1, i)):
            print("%02d" % nnn, end=" ")
        print()
    for j in range(1, num):
        print("   " * (j), end="")
        for kkk in range(1, num - j + 1):
            print("%02d" % kkk, end=" ")
        for ggg in reversed(range(1, num - j)):
            print("%02d" % ggg, end=" ")
        print()

main()
