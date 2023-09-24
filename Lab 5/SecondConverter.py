"""SecondConverter"""
def main():
    """calculate"""
    num_k = int(input())
    num_s = int(input())
    num_m = int(input())
    num_h = int(input())
    hour = 0
    minute = 0
    second = num_k
    minute = second // num_s
    hour = minute // num_m
    second = second % num_s
    minute = minute % num_m
    hour = hour % num_h
    print(hour, minute, second, sep=":")

main()
