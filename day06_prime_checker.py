

# Day 6: Prime Number Checker
# Author: Janani Thaddi

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_in_range(start, end):
    """Return a list of prime numbers in a given range."""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


print("🔢 Welcome to Prime Number Checker 🔢")

while True:
    print("\n1️⃣ Check a single number")
    print("2️⃣ Find primes in a range")
    print("3️⃣ Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        num = int(input("Enter a number: "))
        if is_prime(num):
            print(f"✅ {num} is a prime number!")
        else:
            print(f"❌ {num} is not a prime number.")

    elif choice == "2":
        start = int(input("Enter start of range: "))
        end = int(input("Enter end of range: "))
        primes = prime_in_range(start, end)
        print(f"Prime numbers between {start} and {end}: {primes}")

    elif choice == "3":
        print("👋 Goodbye! See you tomorrow!")
        break

    else:
        print("⚠️ Invalid choice, please try again.")

