"""fever"""
def are_you_ok(fever):
    """like a fever fever fever"""
    if 36 <= fever < 38:
        status = "No Fever"
    elif 38 <= fever < 39:
        status = "Mild Fever"
    elif 39 <= fever < 40:
        status = "High Fever"
    else:
        status = "Very High Fever"
    return status
print(are_you_ok(float(input())))
