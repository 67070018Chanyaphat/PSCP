"""second"""
def main():
    """start"""
    k = int(input())
    s = int(input())
    m = int(input())
    h = int(input())
    k = k % (s*m*h)
    hour = k // ( s * m )
    k %= s * m
    minute = k // s
    k %= s
    print(f"{hour}:{minute}:{k}")
main()
