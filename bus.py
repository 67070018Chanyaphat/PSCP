"""bus"""
def bus_seating_chart():
    # รับข้อมูลจากผู้ใช้
    seats_per_row = int(input())  # จำนวนที่นั่งในแต่ละแถว (ต้องเป็นคู่)
    rows = int(input())            # จำนวนแถวในรถโดยสาร
    target_seat = int(input())     # หมายเลขที่นั่งของนาย ก

    # สร้างผังที่นั่ง
    seating_arrangement = []  # สร้างรายการเก็บข้อมูลที่นั่ง

    for row in range(rows):
        current_row = []
        for seat in range(1, seats_per_row + 1):
            seat_number = row * seats_per_row + seat  # คำนวณหมายเลขที่นั่ง
            if seat_number == target_seat:
                current_row.append("XX")  # ถ้าหมายเลขที่นั่งตรงกับหมายเลขที่นั่งของนาย ก
            else:
                current_row.append(f"{seat_number:02d}")  # แสดงหมายเลขที่นั่ง 2 หลัก
        seating_arrangement.append(current_row)

    # แสดงผลผังที่นั่งในรูปแบบที่ต้องการ
    for i in range(rows):
        # แยกที่นั่งออกเป็น 2 ฝั่ง
        left_side = seating_arrangement[i][:seats_per_row // 2][::-1]  # หมายเลขที่นั่งซ้าย (ย้อนกลับ)
        right_side = seating_arrangement[i][seats_per_row // 2:]       # หมายเลขที่นั่งขวา
        
        # แสดงผลที่นั่งในรูปแบบแถว
        print(" ".join(left_side) + "  " + " ".join(right_side))

# เรียกใช้ฟังก์ชัน
bus_seating_chart()
