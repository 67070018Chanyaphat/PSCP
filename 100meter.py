"""100 meter"""
def runfast():
    """find who win"""
    first_time = None
    first_number = None
    second_time = None
    second_number = None
    third_time = None
    third_number = None

    for number in range(1,9):
        order = float(input())
        if first_time is None:
            first_time = order
            first_number = number
        elif order < first_time:
            third_time = second_time
            third_number = second_number
            second_time = first_time
            second_number = first_number
            first_time = order
            first_number = number
        elif second_time is None:
            second_time = order
            second_number = number
        elif order < second_time:
            third_time = second_time
            third_number = second_number
            second_time = order
            second_number = number
        elif third_time is None:
            third_time = order
            third_number = number
        elif order < third_time:
            third_time = order
            third_number = number
    print(f"{first_number} {second_number} {third_number}")
runfast()
