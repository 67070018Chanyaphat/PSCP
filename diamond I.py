"""Diamond I"""
def column_sum(lst, col, num_m):
    """calculate the sum of a given column."""
    if not num_m:
        return 0
    return int(lst[num_m - 1][col]) + column_sum(lst, col, num_m - 1)

def max_column_sum(lst, num_m, num_n):
    """find the maximum column sum."""
    if not num_n:
        return float('-inf')
    current_sum = column_sum(lst, num_n - 1, num_m)
    return max(current_sum, max_column_sum(lst, num_m, num_n - 1))

def main():
    """input"""
    num_m = int(input())
    num_n = int(input())
    lst = [input().split() for _ in range(num_m)]
    print(max_column_sum(lst, num_m, num_n))
main()
