#Use a for loop to print a box like the one below. Allow the user to specify how wide and how high the box should be.
# *******************
# *                 *
# *                 *
# *******************

# box with 10*10
# print:
# 10 * '*'
# loop (10-2) times: (1 * '*') + (8 * ' ') + (1 * '*')
# 10 * '*'

box_width = int(input("How wide do you want the box?"))
box_height = int(input("how high do you want the box?"))

for i in range(box_height):
    if i < 1:
        print('*' * box_width)
    elif i == (box_height - 1):
        print('*' * box_width)
    else:
        print('*' + (' ' * (box_width - 2)) + '*')