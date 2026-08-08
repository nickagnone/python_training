# Find and print the student with the highest score.

def print_highest_score():
    students = [
        {"name": "Nick", "score": 87},
        {"name": "Sarah", "score": 95},
        {"name": "Mike", "score": 99},
        {"name": "Emma", "score": 91}
    ]

    highest_score = 0
    counter = 0

    for student in students:
        if students[counter]["score"] > highest_score:
            highest_score = students[counter]["score"]
            best_student = students[counter]["name"]

        counter += 1

    print(f'The highest score belongs to {best_student} with a score of {highest_score}!')


# Find the average score and print every student who scored above the average.

def print_above_average():
    students = [
        {"name": "Nick", "score": 87},
        {"name": "Sarah", "score": 95},
        {"name": "Mike", "score": 99},
        {"name": "Emma", "score": 91}
    ]

    total_score = 0
    counter = 0
    counter2 = 0

    # Calculate total score.
    for student in students:
        total_score += students[counter]["score"]
        counter += 1

    # Calculate average.
    average_score = total_score / len(students)

    print(f'Average score: {average_score}')

    # Find students above average.
    for student in students:
        if students[counter2]["score"] > average_score:
            student_name = students[counter2]["name"]
            print(f'{student_name} scored above the average!')

        counter2 += 1


# Call the functions.
print_highest_score()
print_above_average()