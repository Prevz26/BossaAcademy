def is_prime():
    for i in range(2, 51):
        is_prime_number = True  # Assume i is prime until proven otherwise

        for num in range(2, int(i**0.5) + 1):
            if i % num == 0:
                is_prime_number = False
                break

        if is_prime_number:
            print(f"{i} is a prime number")

is_prime()
