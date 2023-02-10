#Verminder het getal elf met drie​
#totdat het resultaat op nul uitkomt of niet​

# Define the number eleven​
num = 11
num2 = 3


# As long as result is larger than zero:​
while num > 0:
    # Subtract three​
    num = num - num2
# Check if number is zero or not​
if num == 0:
    # print result​
    print(f"Number is divisible by {num2}.")

else:
    print(f"Number is NOT divisible by {num2}")
    