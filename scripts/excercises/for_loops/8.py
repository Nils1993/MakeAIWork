#Write a program that asks the user for their name and how many times to print it. The program should print out the user's name the specified number of times.

name = input("What's your name?")
print_name = int(input("How many times would you like to print your name?"))

for i in range(print_name):
    print(name)
