student_scores = [123,142,121,156,211,234,151,167,656]

sum = sum(student_scores)
print(sum)

sum = 0
for num in student_scores : 
    sum += num

print(sum)

max = max(student_scores)
print(max)

max = 0
for num in student_scores : 
    if max < num : 
        max = num

print(max)