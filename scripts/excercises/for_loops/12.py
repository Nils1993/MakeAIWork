# Use a for loop to print a triangle like the one below. Allow the user to specify how high the triangle should be.

# *
# **
# ***
# ****

triangle_height = int(input('How high would you like the triangle to be?'))

for i in range(triangle_height):
    print('*' * (i + 1))