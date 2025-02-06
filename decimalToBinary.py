def convert(n):
    binary = ''
    if n == 0:
        return 0

    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2 # quotient for current iteration but will become dividend for next iteration
    
    return binary
