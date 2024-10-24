""" Christmas Tree """
def main():
    """ Main """
    n_size = int(input())
    k_body = int(input())

    for i in range(1, n_size + 1):
        print(" "*(n_size - i) + "*"*(2 * i - 1))
    for j in range(k_body):
        j += 1
        num = int( ( ( ( 2 * n_size - 1 ) -3 ) / 2 ) )
        print(" "*num + "---")

main()
