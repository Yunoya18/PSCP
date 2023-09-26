"""Password"""
import math
def cal_r(text):
    """calculate r"""
    lower = 0
    upper = 0
    num = 0
    extra = 0
    for i in text:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
        elif i.isnumeric():
            num += 1
    if lower + upper + num != len(text):
        extra += 1
    if lower != 0:
        lower = 1
    if upper != 0:
        upper = 1
    if num != 0:
        num = 1
    num_r = (26*upper) + (26*lower) + (10*num) + (32*extra)
    return num_r

def main():
    """process"""
    text = input()
    num_l = len(text)
    num_r = cal_r(text)
    num_e = math.floor(math.log(num_r**num_l, 2))
    if num_e < 28:
        strength = "Very Weak"
    elif num_e in range(28, 36):
        strength = "Weak"
    elif num_e in range(36, 60):
        strength = "Reasonable"
    elif num_e in range(60, 128):
        strength = "Strong"
    elif num_e >= 128:
        strength = "Very Strong"
    print(num_e)
    print(strength)

main()
