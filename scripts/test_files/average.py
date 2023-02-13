# *arg

def avg(*list1):
    num = 0
    counter = 0
    for n in list1:
        num = num + n
        counter = counter + 1
    if num > 0:
        print(f"The average is {int(num / counter)}")
    else:
        print("The average is 0")

avg(2,3,4)
