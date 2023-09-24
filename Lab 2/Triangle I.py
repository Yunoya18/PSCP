"""Triangle I"""
# ต้องเรียงเลขก่อน
def main():
    """check"""
    num_a = float(input())
    num_b = float(input())
    num_c = float(input())
    if num_a <= num_b and num_b <= num_c:
        num_a, num_b, num_c = num_a, num_b, num_c
    elif num_a <= num_c and num_c <= num_b:
        num_a, num_b, num_c = num_a, num_c, num_b
    elif num_b <= num_a and num_a <= num_c:
        num_a, num_b, num_c = num_b, num_a, num_c
    elif num_b <= num_c and num_c <= num_a:
        num_a, num_b, num_c = num_b, num_c, num_a
    elif num_c <= num_a and num_a <= num_b:
        num_a, num_b, num_c = num_c, num_a, num_b
    elif num_c <= num_b and num_b <= num_a:
        num_a, num_b, num_c = num_c, num_b, num_a
    if num_c**2 + 0.01 >= num_a**2 + num_b**2 >= num_c**2 - 0.01:
        print("Yes")
    else:
        print("No")

main()
