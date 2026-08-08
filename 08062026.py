# Write a program that finds the smallest number within a list.

# numbers = [42, 18, 91, 7, 33, 15]
# smallest_num = numbers[0]

# for i in numbers:
#     if i < smallest_num:
#         smallest_num = i
# print(smallest_num)

# We outline a variable set to the first number within our list.
# We then use a for loop to scan through the numbers within our list and if the number is smaller
# we set that number as our smallest number.
# The function iterates and replaces the value of smallest_num witht he smallest number from our list.


# Print the shortest word within a lsit of words.

# animals = ["elephant", "cat", "hippopotamus", "dog", "bear"]
# shortest_word = animals[0]

# for animal in animals:
#     if len(animal) < len(shortest_word):
#         shortest_word = animal
# print(shortest_word)


# tracker = starting_value

# for item in collection:
#     if item is better than tracker:
#         tracker = item

# print(tracker)

# Find and print the student with the highest score.

students = [
    {"name": "Nick", "score": 87},
    {"name": "Sarah", "score": 95},
    {"name": "Mike", "score": 78}, 
    {"name": "Emma", "score": 91}
]

score = 0
counter = -1

# print(students[0]["name"])

for student in students:
    if students[counter + 1]["score"] > score:
        score = student["score"]
        counter += 1
print(f'{student["name"]} scored the highest with {student["score"]}')