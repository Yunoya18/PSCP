"""Lucky Number"""
def main():
    """process"""
    num = int(input())
    use = [1]
    if num == 1:
        print(num)
    else:
        total_num = list(range(1, num+1))
        current = total_num[1]
        while len(total_num) >= current:
            del total_num[current-1::current]
            use.append(current)
            for check in total_num:
                if check not in use:
                    current = check
                    break
        print(*total_num)

main()
