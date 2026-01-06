import time

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


start_time = time.time()
count = 0
number = 2

while time.time() - start_time < 30:
    if is_prime(number):
        print(number)
        count += 1
    number += 1

print("\nTotal prime numbers found in 30 seconds:", count)
