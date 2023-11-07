"""Discount"""
def main():
    """process"""
    book_price = []
    while True:
        price = input()
        if price == "ENTER":
            break
        else:
            book_price.append(int(price))
    book_price.sort()
    total_book = len(book_price)
    if total_book < 20:
        free = min(2, total_book // 6)
    else:
        free = total_book // 5
    print(sum(book_price[free:]))

main()
