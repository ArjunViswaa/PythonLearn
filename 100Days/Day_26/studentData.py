import pandas

student_data_frame = pandas.DataFrame({
    "student": ["Arjun", "Anu", "Farhan"],
    "scores": [50, 60, 70]
})

for (index, row) in student_data_frame.iterrows():
    print(row.student)