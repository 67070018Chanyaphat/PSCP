"""water"""
def calculate_water_bill():
    '''Calculate the total water bill for a given number of months based 
    on given rates and thresholds.'''

    # รับจำนวนเดือน
    n = int(input())
    # รับอัตราค่าน้ำประปา (บาทต่อลูกบาศก์เมตร)
    a = float(input())
    # รับจำนวนลูกบาศก์เมตรเกินที่ต้องคิดอัตราค่าน้ำประปาใหม่
    b = float(input())
    # รับอัตราค่าน้ำประปาส่วนที่เกิน (บาทต่อลูกบาศก์เมตร)
    c = float(input())
    # รับจำนวนเงินที่ไม่ต้องเสียค่าน้ำประปา (บาท)
    d = float(input())

    total_cost = 0  # ค่าใช้จ่ายรวม

    for _ in range(n):
        usage = float(input())  # รับปริมาณการใช้น้ำในแต่ละเดือน
        if usage <= b:
            cost = usage * a  # ถ้าใช้ไม่เกิน b ลูกบาศก์เมตร คำนวณตามอัตราปกติ
        else:
            cost = (b * a) + ((usage - b) * c)  # ถ้าใช้เกิน b ลูกบาศก์เมตร คำนวณตามอัตราพิเศษ

        if cost > d:
            total_cost += cost  # ถ้าค่าน้ำเกิน d บาท ให้เพิ่มเข้าค่าใช้จ่ายรวม

    print(f"{total_cost:.2f}")  # แสดงค่าใช้จ่ายรวมเป็นทศนิยม 2 ตำแหน่ง

calculate_water_bill()
