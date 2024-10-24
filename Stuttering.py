"""i hate phee"""
def stuttering(old):
    """Delete repeated words that are next to each other."""
    words = old.split()
    result = []
    length = len(words)
    for i in range(length):
        if not i or words[i] != words[i - 1]:
            result.append(words[i])

    return " ".join(result)

print(stuttering(input()))
