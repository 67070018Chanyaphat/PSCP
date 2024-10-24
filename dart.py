"""dart"""
def calculate_dart_score():
    """งง"""
    # First line is the number of darts
    N = int(input().strip())

    total_score = 0

    # Define score zones based on distance squared
    score_zones = [
        (2 ** 2, 5),  # Distance squared = 4, Score = 5
        (4 ** 2, 4),  # Distance squared = 16, Score = 4
        (6 ** 2, 3),  # Distance squared = 36, Score = 3
        (8 ** 2, 2),  # Distance squared = 64, Score = 2
        (10 ** 2, 1)  # Distance squared = 100, Score = 1
    ]

    # Process each dart
    for _ in range(N):
        x, y = map(int, input().strip().split())
        distance_squared = x * x + y * y

        # Determine score based on the distance
        for radius_squared, score in score_zones:
            if distance_squared <= radius_squared:
                total_score += score
                break  # Found the scoring zone, no need to check further

    # Output the total score
    print(total_score)
calculate_dart_score()
