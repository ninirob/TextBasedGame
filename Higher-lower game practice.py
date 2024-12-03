import random

# Step 1: Seed the random number generator
seedVal = int(input("What seed should be used? "))
random.seed(seedVal)

# Step 2: Get lower and upper bounds
while True:
    lower = int(input("What is the lower bound? "))
    upper = int(input("What is the upper bound? "))
    if lower < upper:
        break
    print("The lower bound must be less than the upper bound.")

# Step 3: Generate the random target number
target = random.randint(lower, upper)

# Step 4: Game loop
print(f"Great, now guess a number between {lower} and {upper}.")
while True:
    # Step 5: Get and validate the user's guess
    guess = int(input("What is your guess? "))
    if guess < lower or guess > upper:
        print(f"Please enter a number between {lower} and {upper}.")
        continue

    # Step 6: Provide feedback
    if guess < target:
        print("Nope, too low.")
    elif guess > target:
        print("Nope, too high.")
    else:
        print("You got it!")
        break
