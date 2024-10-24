"""numday"""
def days_in_month(month):
    """Return the number of days in a given month for the year 2560."""
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # Index 0 is unused
    return days[month]

def is_valid_date(day, month):
    """Check if the date is valid."""
    return 1 <= month <= 12 and 1 <= day <= days_in_month(month)

def calculate_day_difference(first_day, first_month, second_day, second_month):
    """Calculate the absolute difference in days between two valid dates."""
    # If either date is invalid, return "Impossible"
    if not is_valid_date(first_day, first_month) or not is_valid_date(second_day, second_month):
        return "Impossible"

    # Convert both dates to a single "day of year" format
    first_total_days = 0
    for m in range(1, first_month):
        first_total_days += days_in_month(m)
    first_total_days += first_day

    second_total_days = 0
    for m in range(1, second_month):
        second_total_days += days_in_month(m)
    second_total_days += second_day

    # Return the absolute difference in days
    return abs(first_total_days - second_total_days)

# Input
day1 = int(input().strip())
month1 = int(input().strip())
day2 = int(input().strip())
month2 = int(input().strip())

# Calculate and print the result
result = calculate_day_difference(day1, month1, day2, month2)
print(result)
