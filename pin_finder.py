import random

def crack_pin():
    # Generate a random 6-digit PIN to simulate the unknown target
    target_pin = str(random.randint(0, 999999)).zfill(6)
    
    print(f"Simulating cracking the device's PIN. The target PIN is unknown (hidden).")
    
    print(f"(Hidden) Target PIN: {target_pin}")

    # Step 2: Try brute-force guessing
    attempts = 0
    while True:
        # Generate a random 6-digit PIN to guess
        guess = str(random.randint(0, 999999)).zfill(6)
        attempts += 1
        
        print(f"Attempt {attempts}: Trying PIN {guess}")
        
        if guess == target_pin:
            print(f"Success! The correct PIN is {guess}, found after {attempts} attempts.")
            break

crack_pin()
