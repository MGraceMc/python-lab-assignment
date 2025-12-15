num = int(input("Enter a number: "))

is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

position = int(input("What position of Fibonacci number do you want to see? "))
print(fibonacci(position))

age = int(input("Enter the person's age: "))

if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")

while True:
    age_input = input("Enter your age (or type 'quit' to exit): ")
    if age_input.lower() == 'quit':
        break

    ticket_age = int(age_input)

    if ticket_age < 3:
        print("Your ticket is free!")
    elif ticket_age <= 12:
        print("Your ticket is $10")
    else:
        print("Your ticket is $15")

rows = 3
for i in range(1, rows + 1):
    for j in range(i):
        print(" ", end="")
    for k in range(i + 1):
        print("*", end="")
    print()