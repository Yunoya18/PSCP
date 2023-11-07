"""Heads and Legs"""
def main():
    """calculate"""
    num = int(input())
    leg = int(input())
    if leg < num*2 or leg > num*4 or leg % 2 == 1 or (num == 0 and leg != 0):
        print("Impossible")
    else:
        rabbit = (leg - (2*num)) / 2
        bird = num - rabbit
        print(int(rabbit), int(bird))
 
main()
