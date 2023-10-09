"""Runner"""
def check(runner):
    """check"""
    return (runner[3]/runner[1], -runner[1]) #ระยะเวลา ความเร็ว

def main():
    """process"""
    lenght = float(input())
    num = int(input())
    runner_list = []
    for i in range(1, num + 1):
        runner = input()
        runner = runner.split()
        runner = (i, int(runner[0]), int(runner[1]), lenght - int(runner[1]))\
            #ลำดับ ความเร็ว จุดเริ่มต้น ระยะที่เหลือ
        runner_list.append(runner)
    runner_list.sort(key=check)
    print(runner_list[0][0])

main()
