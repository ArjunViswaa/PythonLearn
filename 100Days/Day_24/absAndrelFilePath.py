# Absolute file path...
with open("D:/Programming_Languages/PythonLearn/100Days/Day_24/my_file.txt") as file:
    contents = file.read()
    print(contents)

# Relative file path...
with open("../../my_file.txt") as file:
    contents = file.read()
    print(contents + " Relative")