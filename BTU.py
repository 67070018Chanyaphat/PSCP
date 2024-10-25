"""BTU"""
def btu_rate_size500(area):
    """btu for upper 500"""
    recommend_air = None
    if 100 <= area <= 150:
        recommend_air = 5000
    elif 150 < area <= 250:
        recommend_air = 6000
    elif 250 < area <= 300:
        recommend_air = 7000
    elif 300 < area <= 350:
        recommend_air = 8000
    elif 350 < area <= 400:
        recommend_air = 9000
    elif 400 < area <= 450:
        recommend_air = 10000
    elif 450 < area <= 550:
        recommend_air = 12000
    return recommend_air
def btu_rate_size2500(area):
    """btu for upper 2500"""
    recommend_air = None
    if 550 <= area <= 700:
        recommend_air = 14000
    elif 700 < area <= 1000:
        recommend_air = 18000
    elif 1000 < area <= 1200:
        recommend_air = 21000
    elif 1200 < area <= 1400:
        recommend_air = 23000
    elif 1400 < area <= 1500:
        recommend_air = 24000
    elif 1500 < area <= 2000:
        recommend_air = 30000
    elif 2000 < area <= 2500:
        recommend_air = 34000
    return recommend_air

def check_btu(area, height, people, type_room, light_room):
    """BTU check rate"""
    if area <= 550:
        btu = btu_rate_size500(area)
    else:
        btu = btu_rate_size2500(area)
    if height > 8:
        height_count = height-8
        btu += (height_count*1000)
    if people > 2:
        people_count = people-2
        btu += (people_count*600)
    if type_room == "kitchen":
        btu += 4000
    if light_room == "facing the sun":
        btu += (0.1*btu)
    elif light_room == "shaded":
        btu -= (0.1*btu)
    print(int(btu))
check_btu(int(input()), int(input()), int(input()), input(), input())
