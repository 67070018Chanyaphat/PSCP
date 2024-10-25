"""AlmostMean"""
def main(num):
    """AlmostMean"""
    people = []
    total_score = 0
    for _ in range(num):
        student_id, score = input().split("\t")
        score = float(score)
        people.append((student_id, score))
        total_score += score
    average = total_score / num
    valid_students = [p for p in people if p[1] <= average]
    closest_student = max(valid_students, key=lambda x: x[1])
    print(f"{closest_student[0]}\t{closest_student[1]}")
main(int(input()))
