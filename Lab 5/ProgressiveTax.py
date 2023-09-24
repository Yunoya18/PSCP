"""ProgressiveTax"""
def main():
    """calculate"""
    cost = 0
    total = float(input())
    if total > 4000000:
        cost += (total - 4000000) * (35/100)
        total = 4000000
    if total > 2000000:
        cost += (total - 2000000) * (30/100)
        total = 2000000
    if total > 1000000:
        cost += (total - 1000000) * (25/100)
        total = 1000000
    if total > 750000:
        cost += (total - 750000) * (20/100)
        total = 750000
    if total > 500000:
        cost += (total - 500000) * (15/100)
        total = 500000
    if total > 300000:
        cost += (total - 300000) * (10/100)
        total = 300000
    if total > 150000:
        cost += (total - 150000) * (5/100)
        total = 150000
    print(int(cost))

main()
