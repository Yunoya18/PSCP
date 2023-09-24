"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def descend(num_a, num_b, num_c):
    """high to low"""
    if num_a >= num_b and num_b >= num_c:
        print('%0.2f, %0.2f, %0.2f'%(num_a, num_b, num_c))
    elif num_a >= num_c and num_c >= num_b:
        print('%0.2f, %0.2f, %0.2f'%(num_a, num_c, num_b))
    elif num_b >= num_a and num_a >= num_c:
        print('%0.2f, %0.2f, %0.2f'%(num_b, num_a, num_c))
    elif num_b >= num_c and num_c >= num_a:
        print('%0.2f, %0.2f, %0.2f'%(num_b, num_c, num_a))
    elif num_c >= num_a and num_a >= num_b:
        print('%0.2f, %0.2f, %0.2f'%(num_c, num_a, num_b))
    elif num_c >= num_b and num_b >= num_a:
        print('%0.2f, %0.2f, %0.2f'%(num_c, num_b, num_a))

def ascend(num_a, num_b, num_c):
    """low to high"""
    if num_a <= num_b and num_b <= num_c:
        print('%0.2f, %0.2f, %0.2f'%(num_a, num_b, num_c))
    elif num_a <= num_c and num_c <= num_b:
        print('%0.2f, %0.2f, %0.2f'%(num_a, num_c, num_b))
    elif num_b <= num_a and num_a <= num_c:
        print('%0.2f, %0.2f, %0.2f'%(num_b, num_a, num_c))
    elif num_b <= num_c and num_c <= num_a:
        print('%0.2f, %0.2f, %0.2f'%(num_b, num_c, num_a))
    elif num_c <= num_a and num_a <= num_b:
        print('%0.2f, %0.2f, %0.2f'%(num_c, num_a, num_b))
    elif num_c <= num_b and num_b <= num_a:
        print('%0.2f, %0.2f, %0.2f'%(num_c, num_b, num_a))

def main():
    """process"""
    check = input()
    num_a = float(input())
    num_b = float(input())
    num_c = float(input())
    if check == "Descend":
        descend(num_a, num_b, num_c)
    elif check == "Ascend":
        ascend(num_a, num_b, num_c)

main()
