"""sequence"""
def main():
    """start"""
    size = int(input())
    for i in range( 1, size + 1 ):
        for j in range( 1, size + 1 ):
            if j in (1, size, i):
                print("*", end="")
            else:
                print(" ", end="")
        print()
main()
