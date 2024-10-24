"""missing Number"""
def find_number(num):
    """number what we find"""
    number = []
    number_left = []
    while num:
        num_inp = int(input())
        if not num_inp:
            break
        number.append(num_inp)
    for i in range(1, num+1):
        if i not in number:
            number_left.append(i)
        else:
            continue
    sort_leftnum = sorted(number_left)
    for i in sort_leftnum:
        print(int(i))

find_number(int(input()))
