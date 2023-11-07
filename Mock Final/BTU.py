"""BTU"""
def main():
    """calculate"""
    size = int(input())
    height = int(input())
    people = int(input())
    temp = input()
    status = input()
    total = 5000*(size in range(100, 151)) + 6000*(size in range(151, 251))\
    + 7000*(size in range(251, 301)) + 8000*(size in range(301, 351))\
    + 9000*(size in range(351, 401)) + 10000*(size in range(401, 451))\
    + 12000*(size in range(451, 551)) + 14000*(size in range(551, 701))\
    + 18000*(size in range(701, 1001)) + 21000*(size in range(1001, 1201))\
    + 23000*(size in range(1201, 1401)) + 24000*(size in range(1401, 1501))\
    + 30000*(size in range(1501, 2001)) + 34000*(size in range(2001, 2501))
    if height > 8:
        total += 1000*(height-8)
    if people > 2:
        total += 600*(people-2)
    if temp != "Normal":
        total += 4000
    if status == "facing the sun":
        total *= (110/100)
    elif status == "shaded":
        total *= (90/100)
    print(int(total))

main()
