"""LetterFrequency"""
import string
def main():
    """LetterFrequency"""
    word = input().lower().replace(" ", "")
    ans = list(filter(lambda x: x in string.ascii_letters, word))
    ans = max(set(ans), key=ans.count)
    print(ans)
main()
