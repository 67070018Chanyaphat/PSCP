"""game"""
def equal_time():
    """count times of equal"""
    total_point_a = int(input())
    total_point_b = int(input())
    time_a_win = total_point_a//3
    remain_time_a = total_point_a-(time_a_win*3)
    time_b_win = total_point_b//3
    remain_time_b = total_point_b-(time_b_win*3)
    if remain_time_b == remain_time_a:
        print(remain_time_a)
    else:
        print("Error")
equal_time()
