import itertools
import os

# Function to generate combinations of password hints
def generate_combinations(hints):
    combinations = []
    <
    # Generate combinations of varying lengths from 1 to the total number of hints
    for i in range(1, len(hints) + 1):
        for combo in itertools.permutations(hints, i):
            combo_str = ''.join(combo)  # Join hints without spaces
            
            # Append the original and variations of casing to the list
            combinations.append(combo_str)  # original combination
            combinations.append(combo_str.lower())  # lowercase
            combinations.append(combo_str.upper())  # uppercase
            combinations.append(combo_str.capitalize())  # first letter capitalized

    return list(set(combinations))

# Function to try unlocking USB using a password
def try_password(password):
    device_path = "/dev/sda1"  # Your BitLocker device path
    mount_point = "/mnt/bitlocker"  # Directory to mount BitLocker drive

    # Command to unlock the BitLocker drive
    command_unlock = f"sudo dislocker -u{password} {device_path} -- /mnt/bitlocker"

    # Execute the command to unlock
    result = os.system(command_unlock)

    # Check if the unlocking was successful
    if result == 0:
        print(f"Password found: {password}")
        return True  # Return True if the password was correct
    else:
        print(f"Password failed: {password}")
        return False

# Main function to input hints and try combinations
def main():
    input_hints = input("Enter your password hints, separated by commas: ").split(',')
    
    combinations = generate_combinations(input_hints)
    print(f"Generated {len(combinations)} combinations.")
    
    for password in combinations:
        if try_password(password):
            print(f"Unlock successful with password: {password}")
            return
    
    print("Password not found in combinations.")

if __name__ == "__main__":
    main()
