"""line sorting"""
def line_sort(num):
    """line sort from num of input"""
    line_list = [input() for _ in range(num)]
    list_sort = sorted(line_list, key=len)
    for i in list_sort:
        print(i)
line_sort(int(input()))
