def fibonacci(n):
    if n < 0:
        return "Incorrect input"
    a, b = 0, 1
    for _ in range(n):
        a,b = b, a+b
    return a
print(fibonacci(9))