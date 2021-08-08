# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

# https://www.youtube.com/watch?v=25ovCm9jKfA

# Write function to compute 3x + 1

def f(x):
    return 3*x + 1

print(f(2))

# Anonymous Functions = Lambda Expressions (they mean the same thing)

lambda x: 3*x + 1
g = lambda x : 3*x + 1
print(g(2))

# Combine first name and last name into a single "Full Name"

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("   Thomas", "GERTRUD"))

scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthur C. Clarke", "Frank Herbert", "Orson Scott Card", "Douglas Adams", "H. G. Wells", "Leigh Brackett"]

# help(scifi_authors.sort)

scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
print(scifi_authors)