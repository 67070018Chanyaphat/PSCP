"""Hamming"""
def hamming_distance(str1, str2):
    """Calculate the Hamming distance between two strings."""
    distance = 0
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            distance += 1
    return distance

# รับข้อมูลจากผู้ใช้
input1 = input().strip()
input2 = input().strip()

# แสดงผล
print(hamming_distance(input1, input2))
