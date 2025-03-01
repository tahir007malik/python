def missingPositiveNumber(numbers):
    # Removing negative numbers
    numbers = [num for num in numbers if num > 0]

    # Making sure no duplicates
    set_numbers = set(numbers)

    minimum = 1
    while minimum in set_numbers:
        minimum += 1
    return minimum

l = [7, 7, 6, 9, 10]
print(missingPositiveNumber(l))