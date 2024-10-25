"""BreachTheDoor"""
def clean_word(word):
    """Removes non-alphabetic characters from a word."""
    return ''.join(char for char in word if char.isalpha())

def main():
    """Main function to process input and print words longer than 6 letters."""
    txt = input().replace(",", "").split()

    for word in txt:
        cleaned_word = clean_word(word)
        if len(cleaned_word) > 6:
            print(cleaned_word, end=" ")

main()
