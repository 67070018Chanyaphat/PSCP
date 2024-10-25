"""Runner"""
def main():
    """Runner"""
    distance = int(input())
    count = int(input())
    win = []

    for i in range(count):
        speed, position = map(int, input().split())
        time = (distance - position) / speed

        if not win:
            win = [i + 1, time, speed]
        elif time < win[1]:
            win = [i + 1, time, speed]
        elif time == win[1] and speed > win[2]:
            win = [i + 1, time, speed]

    print(win[0])

main()
