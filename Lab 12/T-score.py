"""T-score"""
def main():
    """calculate"""
    num = int(input())
    input()
    student = [int(input()) for _ in range(num)]
    mean = sum(student) / num
    student_sqr = list(map(lambda x: x**2, student))
    s_d = ((num * sum(student_sqr) - (sum(student)**2)) / (num * (num-1))) ** 0.5
    student = list(map(lambda x: (x - mean)/s_d, student))
    student = list(map(lambda x: 50 + (10 * x), student))
    student = list(map(lambda x: "%.2f" % x, student))
    print(*student, sep="\n")

main()
