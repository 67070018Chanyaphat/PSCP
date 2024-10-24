"""alcohol"""
def qulity_per(sex, weight, qulity_all):
    """Calculate the blood alcohol content based on gender and weight."""
    if sex == "Male":
        rate = qulity_all / (weight * 0.68 * 10)  # สูตรสำหรับผู้ชาย
    else:
        rate = qulity_all / (weight * 0.55 * 10)  # สูตรสำหรับผู้หญิง
    return rate

def alcohol():
    """Determine if it is safe to drive after consuming alcohol."""
    # รับข้อมูลผู้ขับขี่
    sex = input()
    weight = float(input())
    auth_vehicle = input()
    qulity_water = float(input())  # 1 cc = 1 gram
    qulity_al = float(input())
    qulity_can = int(input())
    qulity_hour = int(input())

    # ตรวจสอบการมีใบขับขี่
    has_license = auth_vehicle.lower() == "yes"

    # คำนวณปริมาณแอลกอฮอล์ทั้งหมด
    qulity_all = (qulity_water * qulity_al / 100) * qulity_can  # คำนวณเป็นกรัม
    rate_al = qulity_per(sex, weight, qulity_all)  # คำนวณระดับแอลกอฮอล์ในเลือด (BAC)
    relax = qulity_hour * 0.015  # คำนวณแอลกอฮอล์ที่ถูกขับถ่ายออกไป

    total_al = rate_al - relax  # คำนวณระดับแอลกอฮอล์สุทธิหลังจากเวลาที่พัก
    # ตรวจสอบว่าปลอดภัยหรือไม่
    if has_license and total_al <= 0.05:  # ค่าที่เกินกว่า 50 มิลลิกรัมต่อ 100 มิลลิลิตรคือ 0.05
        print("Safe")
    else:
        print("Not Safe")

# เรียกใช้ฟังก์ชัน
alcohol()
