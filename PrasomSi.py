"""PrasomSib"""
def prasomsib(number_long):
    """count when prasomsib"""
    count = 0
    length = len(number_long)

    # ตรวจสอบทุกช่วงของตัวเลขในสตริง
    for start in range(length):
        current_sum = 0

        # เริ่มจากตำแหน่ง start และไปยังตำแหน่งถัดไป
        for end in range(start, length):
            current_sum += int(number_long[end])  # บวกค่าเข้าไปใน current_sum

            if current_sum == 10:  # ถ้าผลรวมเท่ากับ 10
                count += 1  # เพิ่มตัวนับ

            if current_sum > 10:  # ถ้าผลรวมเกิน 10 ก็ไม่ต้องตรวจต่อ
                break

    print(count)
prasomsib(input())
