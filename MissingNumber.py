"""missing Number"""
def find_number(num):
    """number what we find"""
    number = set()
    number_left = set()
    while num:
        num_inp = int(input())
        if not num_inp:
            break
        number.add(num_inp)
    for i in range(1, num+1):
        if i not in number:
            number_left.add(i)
        else:
            continue
    sort_leftnum = sorted(number_left)
    for i in sort_leftnum:
        print(int(i))

find_number(int(input()))
