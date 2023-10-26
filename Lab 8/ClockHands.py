"""ClockHands"""
def main():
    """calculate"""
    hour = int(input())
    minute = int(input())
    hour *= 5 #1ชั่วโมงขยับ5ช่อง
    hour += minute / 12 #12นาทีต่อ1ช่อง ชั่วโมง
    hour = hour % 60 #มีแค่60ช่อง
    print(minute <= hour < minute + 1)

main()
