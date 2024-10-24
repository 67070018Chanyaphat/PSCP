"""lift"""
def main(people,limit):
    """safe or not safe"""
    twelve_kid = 0
    all_weight = 0
    if people > 0:
        for _ in range(1,people+1):
            age = int(input())
            weight = float(input())
            if age < 12:
                twelve_kid += 1
            all_weight += weight
        if twelve_kid >= people:
            print("Not Safe")
        else:
            if all_weight > limit:
                print("Not Safe")
            else:
                print("Safe")
    else:
        print("Safe")
main(int(input()),float(input()))
