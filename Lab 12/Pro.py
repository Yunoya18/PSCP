"""Pro"""
def main():
    """calculate"""
    num_x, num_y, num_a, num_z = (int(input()) for _ in range(4))
    total = ((num_z // num_x) * num_y) + (num_z % num_x)
    print(total * num_a)

main()
