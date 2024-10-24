"""difference"""
def main():
    """difference"""
    a = set()
    b = set()
    a_b = set()
    n = int(input())
    m = int(input())
    for _ in range(n):
        a.add(int(input()))
    for _ in range(m):
        b.add(int(input()))
    for item in a:
        if not item in b:
            a_b.add(item)
    for number in sorted(a_b):
        print(number, end=" ")
main()
