# think of nested loops like a clock

# for hour in range(60):
#     for minute in range(60):
#         print(f' Hour = {hour}, minute = {minute}')

# Find the matching pairs
list1 = [12, 1, 2, 3, 4]
list2 = [3, 5, 1, 7, 12]


for num in list1:
    for num2 in list2:
        print(num, num2)
        if num == num2:
            print (f'Duplicate detected! {num} and {num2} are the same!')
        else:
            continue

# In order to compare two lists, we utilize nested for loops.
# In the above example, we iterate through both lsits utilizing nested for loops.
# Our first for loop iterates through the first list, while the second iterates through the secodn list.
# One execution will iterate through the first number in list1 and compare to the first number of list 2.
# We then utilize an if statement to compare the two numbers, if they match, we print to the user that we have a match.
# We then continue until all numbers from both lists have been compared.