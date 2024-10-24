"""why are you hello you not thai"""
def extend_vowel(word):
    """hard to understand"""
    vowels = "aeiouAEIOU"
    last_vowel_pos = -1

    # ค้นหาตำแหน่งของสระตัวสุดท้ายโดยใช้ enumerate
    for i, char in enumerate(word):
        if char in vowels:
            last_vowel_pos = i

    # หากเจอสระตัวสุดท้าย
    if last_vowel_pos != -1:
        # ลากเสียงด้วยการเพิ่มสระตัวสุดท้ายอีก 3 ตัว
        word = word[:last_vowel_pos + 1] + word[last_vowel_pos] * 3 + word[last_vowel_pos + 1:]

    return word

# รับคำเข้ามา
input_word = input().strip()

# แสดงผลคำที่ถูกลากเสียง
print(extend_vowel(input_word))
