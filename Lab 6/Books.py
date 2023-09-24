"""Books"""
import math
def main():
    """calculate"""
    num_book = int(input())
    page_per = int(input())
    num_x = int(input())
    num_y = int(input())
    day = 0
    count = 0
    count_page = 0
    while True:
        page = math.ceil(page_per * ((num_x + day)/(num_y + day)))
        if count == num_book:
            break
        if page >= page_per:
            day += (num_book - count)
            break
        count_page += page
        if count_page >= page_per:
            count += 1
            count_page = 0
        day += 1
    print(day)

main()
