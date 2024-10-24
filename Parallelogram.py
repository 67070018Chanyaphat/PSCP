"""pararogram"""
def parallelogram():
    """Create a parallelogram"""
    text = input()
    num_text = len(text)
    for i in range(num_text):
        print(" " * (num_text - i - 1), end="")
        print(text[:i + 1])
    for i in range(1, num_text):
        print(text[i:])
parallelogram()
