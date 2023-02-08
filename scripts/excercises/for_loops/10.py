# Use a for loop to print a box like the one below. 
# Allow the user to specify how wide and how high the box should be. [Hint: print('*' * 10) prints ten asterisks.]

box_width = int(input("How wide do you want the box?"))
box_height = int(input("how high do you want the box?"))

for i in range(box_height):
    print("*" * box_width)
