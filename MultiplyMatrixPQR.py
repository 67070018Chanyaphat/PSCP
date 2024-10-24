def create_matrix():
    # รับขนาดเมทริกซ์
    p = int(input())  # จำนวนแถวของเมทริกซ์ A
    q = int(input())  # จำนวนคอลัมน์ของเมทริกซ์ A และจำนวนแถวของเมทริกซ์ B
    r = int(input())  # จำนวนคอลัมน์ของเมทริกซ์ B

    # รับข้อมูลเมทริกซ์ A
    A = []
    for i in range(p):
        row = list(map(int, input().split()))
        if len(row) != q:  # ตรวจสอบให้แน่ใจว่ามีจำนวนคอลัมน์ตรงตามที่กำหนด
            A.append(row)

    # รับข้อมูลเมทริกซ์ B
    B = []
    for i in range(q):
        row = list(map(int, input().split()))
        if len(row) != r:  # ตรวจสอบให้แน่ใจว่ามีจำนวนคอลัมน์ตรงตามที่กำหนด
            B.append(row)

    # สร้างเมทริกซ์ผลลัพธ์ขนาด p x r ที่เต็มไปด้วยค่า 0
    C = [[0 for _ in range(r)] for _ in range(p)]

    # คำนวณการคูณเมทริกซ์
    for i in range(p):
        for j in range(r):
            for k in range(q):
                C[i][j] += A[i][k] * B[k][j]

    # แสดงผลลัพธ์
    for row in C:
        print(' '.join(map(str, row)))

# เรียกฟังก์ชัน
create_matrix()
