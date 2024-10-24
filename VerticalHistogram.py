"""VerticalHistogram"""
def histogram(sentence):
    # เลือกเฉพาะตัวอักษรและทำการเก็บข้อมูลใน dictionary
    alpha = [ch for ch in sentence if ch.isalpha()]
    dict_his = {}
    for a in alpha:
        if a not in dict_his:
            dict_his[a] = 1
        else:
            dict_his[a] += 1

    # เรียงลำดับตัวอักษรโดยตัวพิมพ์ใหญ่ก่อน ตามด้วยตัวพิมพ์เล็ก a-z
    sorted_keys = sorted(dict_his.keys(), key=lambda x: (x.islower(), x))
    
    # ค่ามากสุดที่เจอเพื่อหาความสูงของ histogram
    max_count = max(dict_his.values())
    
    # สร้างแผนภูมิแนวตั้ง โดยมีตัวเลขทางซ้าย พร้อมช่องว่างระหว่างตัวเลขกับแผนภูมิ
    for level in range(max_count, 0, -1):
        row = f"{level:2}  "  # จัดรูปแบบตัวเลขทางซ้าย (มีสองช่องว่าง)
        for key in sorted_keys:
            if dict_his[key] >= level:
                row += "* "
            else:
                row += "  "
        print(row.rstrip())  # ตัดช่องว่างขวาสุดออก
    
    # พิมพ์ตัวอักษรเรียงลำดับด้านล่างแผนภูมิ
    print("   " + " ".join(sorted_keys))  # ช่องว่างสี่ช่องหน้าตัวอักษร

# ทดสอบฟังก์ชัน
histogram(input())
