"""sock"""
def organize_socks(socks):
    """sock mai tong sai in pair dai mai"""
    # ใช้ Dictionary เพื่อเก็บจำนวนถุงเท้าแต่ละประเภท
    sock_count = {}

    # นับจำนวนถุงเท้าแต่ละตัว
    for sock in socks:
        if sock in sock_count:
            sock_count[sock] += 1  # เพิ่มจำนวนถุงเท้าหากมีอยู่แล้ว
        else:
            sock_count[sock] = 1  # ถ้าไม่เคยมีให้เริ่มนับที่ 1

    pairs = []  # สร้างลิสต์สำหรับเก็บถุงเท้าคู่
    total_pairs = 0  # ตัวนับจำนวนคู่

    # วนลูปผ่านถุงเท้าทุกตัวใน Dictionary ที่เรียงตามตัวอักษร
    for sock in sorted(sock_count.keys()):
        count = sock_count[sock]  # จำนวนถุงเท้าแต่ละตัว
        pair_count = count // 2  # คำนวณจำนวนคู่
        if pair_count > 0:  # ถ้ามีคู่
            pairs.extend([sock * 2] * pair_count)  # เพิ่มคู่ถุงเท้าลงในลิสต์
            total_pairs += pair_count  # อัปเดตจำนวนคู่

    if pairs:  # ถ้ามีคู่
        print(' '.join(pairs))  # แสดงผลถุงเท้าที่เรียงคู่
    else:
        print("None")  # ถ้าไม่มีคู่
    print(total_pairs)  # แสดงจำนวนคู่ทั้งหมด

# รับ input และเรียกใช้ฟังก์ชัน
socks_input = input().strip()  # รับข้อมูลถุงเท้า
organize_socks(socks_input)  # เรียกใช้ฟังก์ชัน
