"""MultiplyMatrixPQR"""
def main():
    """process"""
    num_p = int(input())
    num_q = int(input())
    num_r = int(input())
    matrix_a = []
    matrix_b = []
    for _ in range(num_p):
        num = []
        for _ in range(num_q):
            num.append(int(input()))
        matrix_a.append(num)
    for _ in range(num_q):
        num = []
        for _ in range(num_r):
            num.append(int(input()))
        matrix_b.append(num)
    result = [[0 for _ in range(num_r)] for _ in range(num_p)]
    for i in range(num_p):
        for j in range(num_r):
            for current in range(num_q):
                result[i][j] += matrix_a[i][current] * matrix_b[current][j]
    for line in result:
        print(*line)

main()
