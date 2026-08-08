# Building off of yesterdays lesson, I am going to recap and review outer loop vs inner loop.
# I am also going to outline how yesterdays problem works.

# The problem is, using a list of numbers, compare the numbers and outline
# which numbers occur multiple times.

# numbers = [4, 7, 2, 7, 9, 2]

# for i in range(0, len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         # print(numbers[i], numbers[j])
#         if numbers[i] == numbers[j]:
#             print(f'Duplicate observed!')
#         else:
#             continue


# Your goal is to use nested loops and indexes to identify the names that appear more than once.\

names = ["Nick", "Sarah", "Mike", "Sarah", "John", "Mike"]

for n in range(0, len(names)):
    for n2 in range(n + 1, len(names)):
        # print(names[n], names[n2])
        if names[n] == names[n2]:
            print(f'Duplicate found! The name {names[n]} occures more than once in the list!')


