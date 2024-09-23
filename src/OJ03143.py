x = int(input())

prime_numbers = [2, 3, 5, 7, 11]
for number in range(13, 2000, 2):
    check = True
    for prime in prime_numbers:
        if number % prime == 0:
            check = False
    if check:
        prime_numbers.append(number)

if not(x % 2 == 0 and x >= 6):
    print("Error!")
else:
    first_factor = [prime for prime in prime_numbers
                    if (prime <= x/2 and (x - prime in prime_numbers))]
    for factor in first_factor:
        print(f"{x}={factor}+{x-factor}")


