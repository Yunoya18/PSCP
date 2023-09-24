"""Stepper II"""
# หน้าไปหลัง หลังไปหน้า
def main():
    """process"""
    start = int(input())
    end = int(input())
    if end >= start:
        for i in range(start, end+1, 1):
            print(i)
    elif start > end:
        for i in range(start, end-1, -1):
            print(i)

main()
