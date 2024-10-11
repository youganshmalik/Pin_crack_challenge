import random

# Step 1: Define the function to simulate cracking the PIN
def crack_pin():
    # Generate a random 6-digit PIN to simulate the unknown target
    target_pin = str(random.randint(0, 999999)).zfill(6)
    
    print(f"Simulating cracking the device's PIN. The target PIN is unknown (hidden).")
    
    # For demonstration, we'll print the target PIN (in a real scenario, you wouldn't know this)
    print(f"(Hidden) Target PIN: {target_pin}")

    # Step 2: Try brute-force guessing
    attempts = 0
    while True:
        # Generate a random 6-digit PIN to guess
        guess = str(random.randint(0, 999999)).zfill(6)
        attempts += 1
        
        # Display the guess
        print(f"Attempt {attempts}: Trying PIN {guess}")
        
        # Check if the guess is correct
        if guess == target_pin:
            print(f"Success! The correct PIN is {guess}, found after {attempts} attempts.")
            break

# Step 3: Call the function to crack the PIN
crack_pin()
