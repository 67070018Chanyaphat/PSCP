"""Digit V2"""
def words_to_number(words):
    """Convert English words representing a number to its numeric form."""
    number_dict = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
        "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
        "eighteen": 18, "nineteen": 19, "twenty": 20,
        "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
        "seventy": 70, "eighty": 80, "ninety": 90,
        "hundred": 100, "thousand": 1000
    }

    words = words.split()
    total = 0
    current = 0

    for word in words:
        if word in number_dict:
            number = number_dict[word]
            if number in (100, 1000):  # Merge comparisons
                current *= number
                if number == 1000:
                    total += current
                    current = 0
            else:
                current += number

    total += current
    return total

def count_digits(number):
    """Return the number of digits in a number."""
    return len(str(number))

# Input from the user
input_words = input().strip()

# Convert words to number
numeric_value = words_to_number(input_words)

# Count and output the number of digits
if not numeric_value:  # Simplified condition
    print(1)  # Special case for zero
else:
    print(count_digits(numeric_value))
