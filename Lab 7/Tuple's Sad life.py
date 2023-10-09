"""Tuple's Sad life"""
def main():
    """process"""
    text = input()
    num = input()
    text = text.split()
    text = tuple(text)
    position = text.index(num)
    lenght = text.count(num)
    for _ in range(lenght):
        for _ in range(lenght):
            print(position, end=" ")
        print()

main()
