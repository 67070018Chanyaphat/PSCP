"""RemoveTag"""
def main():
    """RemoveTag"""
    word = input()
    result = []
    while ">" in word:
        word = word.split(">", 1)
        text = word[0].split("<")[0].strip()
        if text:
            result.extend(text.split())
        word = word[1] if len(word) > 1 else ""
    if word:
        result.extend(word.split())
    print(result)
main()
