"""median"""
def median(num):
    """median put in list yeah omg"""
    locate = int((num+1)/2)
    list_num = [float(input()) for _ in range(num)]
    list_sort = sorted(list_num)
    if not num%2:
        median_num = (list_sort[locate-1]+list_sort[locate])/2
    else:
        median_num = list_sort[locate-1]
    print(f"{median_num:.3f}")
median(int(input()))
