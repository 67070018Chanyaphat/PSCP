import json

def taking_turns():
    """Taking Turns"""
    original_list = json.loads(input())
    n = len(original_list)

    # สร้าง list ใหม่
    new_list = []
    
    # ใช้ตัวชี้เพื่อวนลูปผ่านสองด้าน
    for i in range((n + 1) // 2):
        # เพิ่มจากด้านขวา
        if n - 1 - i >= 0:
            new_list.append(original_list[n - 1 - i])  # เพิ่มจากด้านขวา
        # เพิ่มจากด้านซ้าย
        if i < n:
            new_list.append(original_list[i])  # เพิ่มจากด้านซ้าย

    # ถ้า n เป็นจำนวนคู่ ให้ลบค่าที่เพิ่มซ้ำออก
    if n % 2 == 0:
        new_list.pop()  # ลบค่าที่ซ้ำออก

    return new_list

# เรียกใช้ฟังก์ชันและพิมพ์ผลลัพธ์
result = taking_turns()
print(result)
