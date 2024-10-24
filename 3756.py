"""37 (56 54 45 46) 37 (54 48"""
def convert_letters_to_numbers(input_string):
    """hard to do marathon"""
    # Mapping of letters to numbers as per the given specification
    letter_to_numbers = {
        'A': [56, 54, 45, 46],
        'B': [6],
        'C': [4, 11],
        'D': [20, 21, 14],
        'E': [54, 48],
        'F': [31, 29],
        'G': [1, 8],
        'H': [44, 41],
        'I': [47, 71],
        'J': [8],
        'K': [4, 1],
        'L': [36, 42],
        'M': [33],
        'N': [25, 19],
        'O': [58, 60],
        'P': [30, 32, 28, 27],
        'Q': [4],
        'R': [35],
        'S': [11, 40, 38, 39],
        'T': [23, 21, 22, 24, 18, 16],
        'U': [68, 51, 52],
        'V': [37],
        'W': [37],
        'X': [11],
        'Y': [34, 13, 71, 48],
        'Z': [11],
    }

    result = []

    for char in input_string:
        if char in letter_to_numbers:
            numbers = letter_to_numbers[char]
            if len(numbers) > 1:
                result.append(f"({' '.join(map(str, numbers))})")
            else:
                result.append(str(numbers[0]))

    # Joining the results with a space and returning the output
    return ' '.join(result)
# เรียกใช้ฟังก์ชันและพิมพ์ผลลัพธ์
print(convert_letters_to_numbers(input_string = input().strip()))
