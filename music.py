"""music love but i hate"""
def song_list():
    """แงงงงงงงงงงงงงงงงงงงงงงงง"""
    n = int(input())  # รับจำนวนเพลง
    artist_songs = {}  # สร้าง dictionary เพื่อเก็บศิลปินและเพลง

    for _ in range(n):
        entry = input().strip()  # รับข้อมูลแต่ละเพลง
        artist, song = entry.split("-", 1)  # แยกชื่อศิลปินและชื่อเพลง

        if artist not in artist_songs:
            artist_songs[artist] = []  # สร้างรายการเพลงใหม่ถ้ายังไม่มี
        artist_songs[artist].append(song)  # เพิ่มชื่อเพลงในรายการของศิลปิน

    # แสดงผลชื่อศิลปินและเพลง
    for artist, songs in artist_songs.items():
        print(artist)  # แสดงชื่อศิลปิน
        for song in songs:
            print(song)  # แสดงชื่อเพลง

# เรียกใช้ฟังก์ชัน
song_list()
