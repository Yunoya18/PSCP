"""S0rt"""
def main():
    """process"""
    num_list = []
    final_num = []
    while True:
        num = input()
        if num == "END":
            break
        num_list.append(int(num))
    while len(num_list) > 0:
        current = None
        for i in num_list:
            if current == None:
                current = i
            else:
                if i < current:
                    current = i
        final_num.append(current)
        num_list.remove(current)
    print(*final_num, sep="\n")

main()
