"""
โมดูลนี้ประกอบด้วยฟังก์ชันที่คำนวณจำนวนกระต่ายและนก
โดยพิจารณาจากจำนวนสัตว์ทั้งหมดและจำนวนขาทั้งหมด
"""

def find_rabbits_birds(num_animals, num_legs):
    """
    ฟังก์ชันนี้คำนวณจำนวนกระต่ายและนกในกรง
    โดยใช้จำนวนสัตว์ทั้งหมดและจำนวนขาทั้งหมดเป็นข้อมูลอินพุต
    """
    # ตรวจสอบเงื่อนไขเบื้องต้น
    if num_legs % 2 or num_legs < 2 * num_animals or num_legs > 4 * num_animals:
        return "Impossible"

    # คำนวณจำนวนกระต่ายและนก
    rabbits = (num_legs - 2 * num_animals) // 2
    birds = num_animals - rabbits

    if rabbits >= 0 and birds >= 0:
        return rabbits, birds
    return "Impossible"

# รับ input
animal_count = int(input())
leg_count = int(input())

# เรียกฟังก์ชันและแสดงผลลัพธ์
result = find_rabbits_birds(animal_count, leg_count)

if isinstance(result, tuple):
    print(result[0], result[1])
else:
    print(result)
