"""lift"""
def lift():
    """cal weight for safe of lift"""
    num_people = int(input())
    safe_weight = float(input())
    age_twelve = 0
    all_weight = 0
    status = "Safe"
    if num_people > 0:
        for _ in range(1,num_people+1):
            age = int(input())
            weight = float(input())
            if age < 12:
                age_twelve+=1
            all_weight+=weight
        if age_twelve >= num_people:
            status = "Not Safe"
        else:
            if all_weight > safe_weight:
                status = "Not Safe"
            else:
                status = "Safe"
    print(status)
lift()
