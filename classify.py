"""Classify"""
def main():
    """Classify student IDs by year and department, counting occurrences."""
    student_ids = []

    while True:
        st_id = input()
        if st_id == "END":
            break
        student_ids.append(st_id)

    student_ids.sort()
    year_dict = {}

    for st_id in student_ids:
        year = st_id[:2]
        department = int(st_id[2:4])
        if year not in year_dict:
            year_dict[year] = {}
        if department not in year_dict[year]:
            year_dict[year][department] = 0

        year_dict[year][department] += 1

    for year in sorted(year_dict.keys()):
        departments = sorted(year_dict[year].keys())
        print(year, departments[0], year_dict[year][departments[0]])
        for dept in departments[1:]:
            print("--", dept, year_dict[year][dept])

main()
