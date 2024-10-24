"""ISBN"""
def isbn(num):
    """isbn check last digit"""
    num = num.split("-")
    num = "".join(num)
    # ตรวจสอบความยาวของเลข ISBN
    if len(num) != 10:
        print("Invalid ISBN length.")
        return

    # คำนวณค่า checksum
    summa = 0
    for i in range(len(num) - 1):
        summa += int(num[i]) * (10 - i)

    # คำนวณ digit สุดท้าย
    last_digit = (11 - (summa % 11)) % 11

    # ตรวจสอบ digit สุดท้าย
    if last_digit == 10:
        last_digit = 'X'  # ใช้ 'X' แทน 10
    else:
        last_digit = str(last_digit)

    # เปรียบเทียบกับ digit สุดท้ายที่ป้อนมา
    if last_digit == num[-1]:
        print("Yes")
    else:
        print(f"No {last_digit}")

isbn(input())
