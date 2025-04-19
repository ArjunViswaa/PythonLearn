# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# Even simpler syntax for file open()
# with open("my_file.txt", mode="w") as file:
#     contents = file.read()
#     print(contents)
#     file.write("New text.")

# Append text to file.
with open("my_file.txt", mode="a") as file:
    file.write("Added a new line.")

# Create new file and write
with open("new_file.txt", mode="w") as file:
    file.write("Newly added file.")