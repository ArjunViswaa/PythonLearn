import random

numbers = [1, 2, 3]
new_nums = [num + 1 for num in numbers]
# print(new_nums)

name = "Angela"
new_name = [letter for letter in name]
print(new_name)

range_list = [2 * num for num in range(1, 5)]
print(range_list)

names = ["Arjun", "Anu", "Viji", "Remya", "Gomathi"]
short_names = [name for name in names if len(name) < 5]
# print(short_names)

cap_long_names = [name.upper() for name in names if len(name) >= 5]
# print(cap_long_names)

student_score = {student: random.randint(1, 100) for student in names}
passed_students = {student:mark for (student, mark) in student_score.items() if mark > 40}
print(student_score)
print(passed_students)