def calculate(n):
    if n == 0 or n == 1:
        return 1
    return n * calculate(n - 1)
