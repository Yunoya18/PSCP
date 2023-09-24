"""Key"""
def main():
    """calculate"""
    num = input()
    step_1 = 0
    for i in num:
        step_1 += int(i)
    step_2 = ""
    count = 0
    for j in reversed(num):
        step_2 = j + step_2
        count += 1
        if count == 3:
            break
    step_2 = int(step_2) * 10
    step_3 = step_1 + step_2
    if step_3 < 1000:
        step_3 += 1000
    elif len(str(step_3)) > 4:
        step_3 = str(step_3)[len(str(step_3))-4:len(str(step_3))]
    print(step_3)

main()
