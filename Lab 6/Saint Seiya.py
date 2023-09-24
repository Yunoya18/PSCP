"""Saint Seiya"""
def main():
    """calculate"""
    sec = int(input())
    goal = int(input())
    total = 0
    time1 = (sec // 6)
    time2 = (sec // 2) - time1
    if time1 + (time2*165) <= goal: #เช็คว่าถึงจำนวนที่กำหนดไหม ถ้าไม่ถึงให้คำนวณเลย ไม่ต้อง loop
        total = (time1 + (time2*165))
    else:
        for i in range(2, sec + 1, 2):
            if total >= goal: #เพกาซัส โรลลิ่งแครช
                total += (12*(sec - (i-1)))
                break
            elif i % 6 == 0: #เพกาซัส หมัดดาวหาง
                total += 1
            else: #เพกาซัส หมัดดาวตก
                total += 165
    print(total)

main()
