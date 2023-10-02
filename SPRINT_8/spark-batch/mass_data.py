from random import randint

random_numbers = []

for n in range(250):
    number = randint(1, 1000)
    random_numbers.append(number)

print(random_numbers)

reverse_numbers = []

for rev in reversed(random_numbers):
    reverse_numbers.append(rev)

print(reverse_numbers)