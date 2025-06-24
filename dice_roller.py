import random
import time
import sys

def roll_die():
    input("Press 'Enter' to roll the die...")
    print("Rolling", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
        sys.stdout.flush()
    print("\n")
    result = random.randint(1, 6)
    print(f"You rolled a {result}!\n")


while True:
    roll_die()
    again = input("Roll again? (y/n): ").strip().lower()
    if again != 'y':
        print("Goodbye!")
        break
