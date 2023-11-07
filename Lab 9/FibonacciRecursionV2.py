"""FibonacciRecursionV2"""
MEMO_ = {0:0, 1:1}
def fibo(num):
    """calculate"""
    if num <= 0:
        return 0
    if num in MEMO_:
        return MEMO_[num]
    else:
        result = fibo(num-1) + fibo(num-2)
    MEMO_[num] = result
    return result

def main(num, count, total, least):
    """process"""
    check = int(num/800) + 1
    if count != check + 1:
        total += (fibo(min(num, least)) - fibo(least-800))
        count += 1
        least += 800
        main(num, count, total, least)
    else:
        print(total)

main(int(input()), 1, 0, 800)
