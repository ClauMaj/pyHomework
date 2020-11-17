
# 1.  Fibonacci recursive

# def recur_fibo(n):
#     if n <= 0:
#         print("Please enter a number > 0")
#         exit()
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return(recur_fibo(n-1) + recur_fibo(n-2))

# print(recur_fibo(10))


# 2. Fibonacci if

def fibonacci(n):
    a = 0
    b = 1
    if n <= 0:
        print("Please enter a number > 0")
        exit()
    elif n == 1:
        return b
    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
    return c

print(fibonacci(10))
