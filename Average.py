def calculate_average(student_scores):
    total_score = sum(student_scores)
    average_score = total_score / len(student_scores)
    return average_score
# Example usage
print(calculate_average([85, 90, 78, 92, 88]))

