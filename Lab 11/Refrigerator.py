"""Refrigerator"""
def main():
    """calculate"""
    input()
    food = list(map(int, input().split()))
    day = 0
    fridge = None
    while 0 not in food:
        if fridge != None:
            food.append(fridge)
        fridge = min(food)
        food.remove(fridge)
        food = list(map(lambda x: x - 1, food))
        day += 1
    print(day)

main()
