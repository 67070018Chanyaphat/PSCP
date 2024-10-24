"""WordSequence II"""
def main():
    """WordSequence II"""
    word1 = input()
    word2 = input()
    for i in range(0, max(len(word1), len(word2))+1):
        print(word2[:i]+word1[i:])
main()
