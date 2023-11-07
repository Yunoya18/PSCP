"""Kayak"""
def main():
    """process"""
    num = int(input())
    people = list(map(int, input().split()))
    people.sort(key=int)
    people = people[:-2]
    total = 0
    for i in range(0, num+1, 2):
        total += abs(people[i] - people[i+1])
    print(total)

main()
