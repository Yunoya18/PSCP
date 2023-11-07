"""Perfect"""
def main():
    """process"""
    num = int(input())
    total_num = []
    for num in range(2, num+1):
        num_list = []
        for i in range(1, int(num**0.5)+1):
            if num % i == 0:
                check = num / i
                if check != num and check != i:
                    num_list.append(check)
                num_list.append(i)
        if sum(num_list) == num:
            total_num.append(num)
    print(sum(total_num))

main()
