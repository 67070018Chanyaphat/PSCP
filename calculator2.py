"""cal cu lus หรือ cal cu lator"""
def calculator():
    """buy cal เถอะ อย่าเขียนเองเลย"""
    n = int(input().strip())

    if n == 1:
        print(1)  # Only pressing '1'
        return

    # Initialize key press count
    total_keypresses = 0

    # For each digit length (1 to the length of n)
    digit_length = 1
    current_range_start = 1

    while current_range_start <= n:
        # Determine the end of the current range
        current_range_end = min(n, current_range_start * 10 - 1)

        # Count how many numbers are in this range
        count_in_range = current_range_end - current_range_start + 1

        # Each number in this range has `digit_length` digits
        total_keypresses += count_in_range * digit_length

        # Move to the next range
        current_range_start *= 10
        digit_length += 1

    # Add '+' signs (n - 1)
    total_keypresses += (n - 1)

    # Add '=' sign
    total_keypresses += 1

    print(total_keypresses)
calculator()
