"""Saint Seiya"""
def main(time, punch):
    """Saint Seiya"""
    result = 0
    for i in range(2, time+1, 2):
        if result >= punch:
            result += (12*(time-i+1))
            break
        if not i % 6:
            result += 1
        elif not i % 2:
            result += 165
    print(result)
main(int(input()), int(input()))
