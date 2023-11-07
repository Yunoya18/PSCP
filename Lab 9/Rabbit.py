"""Rabbit"""
import math
def main():
    """calculate"""
    rabbit = int(input())
    total_jump = int(input())
    carrot = int(input())
    use = min(rabbit, carrot)
    use_jump = (use * (use + 1))/2
    if use_jump > total_jump:
        highest = math.floor((((2*total_jump)+(1/4))**(1/2))-(1/2))
        use_jump = (highest * (highest + 1))/2
        rabbit_left = max(0, rabbit - highest)
        carrot_left = max(0, carrot - highest)
    else:
        rabbit_left = max(0, rabbit - carrot)
        carrot_left = max(0, carrot - rabbit)
    jump_left = int(total_jump - use_jump)
    if carrot_left == 0 and rabbit_left == 0 and jump_left == 0:
        print("Ahhahaha")
    else:
        print(rabbit_left, jump_left, carrot_left)

main()
