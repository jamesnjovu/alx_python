for first_digit in range(0, 9):
    for second_digit in range(first_digit + 1, 10):
        print(f"{first_digit}{second_digit}".format(), end=", ")