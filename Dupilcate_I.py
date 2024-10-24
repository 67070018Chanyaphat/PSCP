"""duplicate I"""
def main():
    """duplicate"""
    a = set()
    b = set()
    n = int(input())
    m = int(input())
    for _ in range(n):
        a.add(input())
    for _ in range(m):
        b.add(input())
    if not a&b:
        print("Nope")
    else:
        for student in sorted(a&b, reverse=True):
            print(student)
main()
