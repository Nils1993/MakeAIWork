# Use a for loop to print an upside down triangle like the one below. Allow the user to specify how high the triangle should be.

# ****
# ***
# **
# *

triangle = int(input("How hight would you like the triangle to be"))

for i in range(triangle):
    print('*' * triangle)
    triangle = triangle - 1