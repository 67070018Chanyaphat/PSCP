"""AndAgainAndAgain"""
def count_vowels(word):
    """Count the vowels in a word."""
    vowels = set("aeiou")
    return sum(1 for char in word if char in vowels)

def main():
    """Main function to filter and sort words based on vowel count."""
    txt = input().replace(".", "").lower().split()
    words_with_vowels = [word for word in txt if count_vowels(word) >= 2]

    words_with_vowels.sort()

    if words_with_vowels:
        print("\n".join(words_with_vowels))
    else:
        print("Nope")

main()
