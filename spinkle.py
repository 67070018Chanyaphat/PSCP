"""spinkle"""
def eat():
    """cal distance potato from finger"""
    lid1 = input()
    potato = input()
    lid2 = input()
    count = 0
    left_count = 0
    status = "There are still some left."
    finger = int(input())
    for i in range(finger):
        for eating in potato[i]:
            if eating == ")":
                count+=1
                potato = potato.replace(")"," ",1)
            else:
                count+=0
                potato = potato.replace(" "," ",1)
    for left in potato:
        if left == ")":
            left_count+=1
        else:
            left_count+=0
    if left_count > 0:
        status = "There are still some left."
    else:
        status = "None."
    print(count)
    print(status)
    print(lid1)
    print(potato)
    print(lid2)
eat()
