"""RunGame"""
def main():
    """process"""
    start = 0
    text = list(map(int, input().split()))
    total = 0
    for i in text:
        total += (abs(i - start))
        start = i
    print(total)

main()
