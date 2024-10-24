"""why don't buy new one keyboard"""
def true_key():
    """Change bad characters to good"""
    input_text = input()
    new_text = ''
    for char in input_text:
        if char == 'i':
            new_text += 'o'
        elif char == 'o':
            new_text += 'i'
        elif char == 'I':
            new_text += 'O'
        elif char == 'O':
            new_text += 'I'
        else:
            new_text += char
    print(new_text)
true_key()
