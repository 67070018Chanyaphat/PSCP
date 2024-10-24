"""day arkkkkkkkkkkk"""
def find_day(d, m):
    """day eiei"""
    # สร้างลิสต์ของวันในสัปดาห์
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # จำนวนวันของแต่ละเดือนในปี 2011
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # วันของสัปดาห์ในวันที่ 1 มกราคม 2011 คือวันเสาร์
    start_day_of_week = 5  # Saturday
    # คำนวณจำนวนวันตั้งแต่ต้นปีถึงวันที่ d เดือน m
    total_days = sum(days_in_month[:m-1]) + d - 1
    # คำนวณวันในสัปดาห์
    day_of_week = (start_day_of_week + total_days) % 7

    return days[day_of_week]
# คำนวณและแสดงผลลัพธ์
print(find_day(int(input()), int(input())))
