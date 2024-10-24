""" Left Arrow """
def main():
    """ Main """
    k_width = int( input() )
    n_lines = int( input() )
    n_start = int((n_lines + 1) / 2 - 1)
    for i in range(-n_start, n_start + 1):
        i = n_start - abs(i)
        print(" "*abs(i) + "*"*k_width)

main()
