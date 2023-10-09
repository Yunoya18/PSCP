"""LineSorting"""
def main():
    """process"""
    num = int(input())
    text_list = []
    for _ in range(num):
        text = input()
        text_list.append(text)
    text_list.sort(key=len)
    for i in text_list:
        print(i)

main()
