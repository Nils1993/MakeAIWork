# create a function which counts the vowels in an int.
def count_vowels():
    a = input("please enter a sentence and press ENTER:")
    counter = 0
    for char in a:
        if char == 'a' or char =='i' or char == 'o' or char == 'e' or char =='u':
            counter = counter + 1
    print(f"The amount of vowels inside your input is {counter}")

count_vowels()
