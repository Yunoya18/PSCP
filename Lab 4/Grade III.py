"""Grade III"""
def check_grade(score):
    """check"""
    if 95 <= score <= 100:
        grade = 4
    elif 90 <= score < 95:
        grade = 3.5
    elif 85 <= score < 90:
        grade = 3
    elif 80 <= score < 85:
        grade = 2.5
    elif 75 <= score < 80:
        grade = 2
    elif 70 <= score < 75:
        grade = 1.5
    elif 65 <= score < 70:
        grade = 1
    elif 60 <= score < 65:
        grade = 0.5
    elif 0 <= score < 60:
        grade = 0
    return grade

def main():
    """process"""
    num = int(input())
    total = 0
    for _ in range(num):
        total += check_grade(float(input()))
    grade = total / num
    if len(str(grade)) == 3:
        final_grade = str(grade)
        final_grade += "0"
    else:
        final_grade = int(grade*10**2)/10**2
    print(final_grade)

main()
