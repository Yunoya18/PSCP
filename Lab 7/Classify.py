"""Classify"""
def main():
    """procecss"""
    student = []
    while True:
        num = input()
        if num == "END":
            break
        student.append((num[0:2], num[2:4]))
    student.sort()
    check = []
    check_year = 0
    for i in student:
        if i not in check:
            if i[0] != check_year:
                print(i[0], int(i[1]), student.count(i))
            else:
                print("--", int(i[1]), student.count(i))
        check.append(i)
        check_year = i[0]

main()
