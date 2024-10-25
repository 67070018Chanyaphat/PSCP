"""BookWorm"""
def book():
    """BookWorm"""
    count = int(input())
    for _ in range(count):
        read_time = float(input())
        books_count = int(input())
        time_lst = sorted([float(input()) for _ in range(books_count)])
        books_read = 0
        for time in time_lst:
            if read_time < time:
                break
            read_time -= time
            books_read += 1

        print(books_read)
book()
