"""cookie run"""
def total_distance(positions_list):
    """Calculate the total distance to collect items on a straight line."""
    if not positions_list:
        return 0

    total_dist = abs(positions_list[0])  # Distance from start to the first position
    for i in range(1, len(positions_list)):
        total_dist += abs(positions_list[i] - positions_list[i - 1])

    return total_dist

def main():
    """Read input and calculate the total running distance."""
    # Read positions as a list of integers
    positions = list(map(int, input().split()))

    # Calculate the total distance
    result = total_distance(positions)

    # Print the result
    print(result)

if __name__ == "__main__":
    main()
