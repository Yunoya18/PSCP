"""FibonacciRecursionV1"""
def fibo(num):
    """fibonacci"""
    if num == 0:
        return 0
    elif num == 1:
        return 1
    final_num = fibo(num-1) + fibo(num-2)
    return final_num

def main():
    """process"""
    num = int(input())
    print(fibo(num))

main()
