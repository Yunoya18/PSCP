"""SurprisingVote"""
def main():
    """process"""
    total = float(input())
    highest = float(input())
    second = total - highest
    if second >= highest:
        second = highest
    lowest = total - highest - second
    if highest - lowest > 2:
        print("Surprising")
    else:
        print("Not surprising")

main()
