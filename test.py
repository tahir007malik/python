def main():
    # start coding from here ...
    def isPrime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def findPrimeFactors(n):
        factorsList = []
        primeFactorsList = []
        for i in range(1, n + 1):
            if n % i == 0:
                factorsList.append(i)
                if isPrime(i):
                    primeFactorsList.append(i)
        return factorsList, primeFactorsList

    n = int(input('enter n: '))
    factors, primeFactors = findPrimeFactors(n)
    print('factors:', factors)
    print('prime factors:', primeFactors)
if __name__ == '__main__':
    main()