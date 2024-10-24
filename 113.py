"""113"""
def oneonethree(num):
    """hate one one three"""
    # ใช้ replace เพื่อลบ '113' ออกจากสตริง
    new_num = num.replace("113", "")

    # ถ้ายังมี '113' อยู่ใน new_num ให้เรียกฟังก์ชันอีกครั้ง
    if "113" in new_num:
        return oneonethree(new_num)

    return new_num
print(oneonethree(input()))
