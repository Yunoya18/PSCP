"""Donut"""
def main():
    """calculate"""
    price = int(input())
    piece = int(input())
    free = int(input())
    need = int(input())
    times = need // (piece + free)
    left = need - (times *(piece + free))
    total_price = times * piece * price
    total_piece = times * (piece + free)
    if left >= piece:
        total_price += (piece * price)
        total_piece += (piece + free)
    else:
        total_price += (left * price)
        total_piece += left
    print(total_price, total_piece)

main()
