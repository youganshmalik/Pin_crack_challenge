import random

def generate_pin():
    return str(random.randint(0, 999999)).zfill(6)

def crack_pin(target_pin):
    attempts = 0
    max_attempts = 10
    found_pin = False

    print(f"Target PIN is: {target_pin}")  

    while attempts < max_attempts and not found_pin:
        # Generate a random guess
        guess = str(random.randint(0, 999999)).zfill(6)
        attempts += 1
        
        print(f"Attempt {attempts}: Trying PIN {guess}")

        if guess == target_pin:
            found_pin = True
            print(f"Success! Found the PIN: {guess} in {attempts} attempts.")
        else:
            print(f"Attempt {attempts} failed.")

    if not found_pin:
        print("Failed to find the PIN within 10 attempts.")

# Main execution
if __name__ == "__main__":
    target_pin = generate_pin()  
    crack_pin(target_pin)  
