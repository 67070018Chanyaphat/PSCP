"""pro"""
def calculate_buffet_cost():
    """eat mhoo"""
    # รับข้อมูลจากผู้ใช้
    x = int(input())  # จำนวนคนที่มา (จ่ายเท่ากับจำนวน y)
    y = int(input())  # จำนวนคนที่จ่าย
    a = int(input())  # ราคาค่า Buffet ต่อคน
    z = int(input())  # จำนวนคนที่มา

    # คำนวณจำนวนคนที่ต้องจ่ายเงิน
    if z <= y:
        # ถ้าจำนวนคนที่มาน้อยกว่าหรือเท่ากับที่ต้องจ่าย จะจ่ายตามจำนวนคนที่มาทั้งหมด
        total_cost = z * a
    else:
        # ถ้าจำนวนคนที่มากกว่าที่ต้องจ่าย
        groups = z // x  # จำนวนกลุ่ม
        remaining_people = z % x  # คนที่เหลือ
        # คำนวณค่าใช้จ่ายสำหรับกลุ่มที่ใช้โปรลด
        total_cost = (groups * y * a) + (remaining_people * a)

    # แสดงผล
    print(total_cost)

# เรียกใช้ฟังก์ชัน
calculate_buffet_cost()
