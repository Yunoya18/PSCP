"""BookWorm"""
def main():
    """process"""
    book_set = int(input())
    for _ in range(book_set):
        time = float(input())
        time_list = []
        total_time = 0
        count = 0
        num_book = int(input())
        for _ in range(num_book):
            time_need = float(input())
            time_list.append(time_need)
            time_list.sort()
        for i in time_list:
            total_time += i
            if total_time > time:
                break
            else:
                count += 1
        print(count)

main()
