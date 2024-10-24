"""home run"""
def homerun():
    """compare between length of ground and length of hit"""
    num_ground = int(input())
    batter_hit = float(input())
    times_hit = 0
    for _ in range(num_ground):
        length_ground = float(input())
        if length_ground < batter_hit:
            times_hit+=1
    print(times_hit)
homerun()
