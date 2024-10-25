"""Point Sorting"""
def puls(num):
    """X+Y"""
    return int(num[0]) + int(num[1])

def sort_y(num):
    """sort y"""
    return int(num[1])

def main():
    """Point Sorting"""
    count = int(input())
    for _ in range(count):
        count_n = int(input())
        lst = [input().split() for _ in range(count_n)]
        lst.sort(key=sort_y, reverse=True)
        lst.sort(key=puls)
        for i in lst:
            print(i[0], i[1])
main()
