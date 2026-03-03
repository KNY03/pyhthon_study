def factorial(n):
    # res = 1
    # for i in range (n, 0, -1):
    #     res *= i
    # return res
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))