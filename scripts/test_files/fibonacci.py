# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)

# print(factorial(5))
# 5*4*3*2*1 -> 5*4 -> 20*3 -> 60*2 -> 120*1 = 120



# fibonacci reeks van 10:

# 1-1-2-3-5-8-13-21-34-55
# 1+1 = 2
# 1+2 = 3
# 2+3 = 5
# 3+5 = 8
# 5+8 = 13
# 8+13 = 21
# 13+21 = 34
# 21+34 = 55


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(10))