
# Fibonacci recursive

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

# Fibonacci array

# Fibonacci if

def fibonacci(n):
    a = 0
    b = 1
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return b
    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
        return c

print(fibonacci(9)
