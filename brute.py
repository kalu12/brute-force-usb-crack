import itertools
import os

# Function to generate combinations of password hints
def generate_combinations(hints):
    combinations = []
    
    # Generate combinations of varying lengths from 1 to the total number of hints
    for i in range(1, len(hints) + 1):
        # Use itertools.permutations to create different orderings of hints
        for combo in itertools.permutations(hints, i):
            combo_str = ''.join(combo)  # Join hints without spaces
            
            # Append the original and variations of casing to the list
            combinations.append(combo_str)  # original combination
            combinations.append(combo_str.lower())  # lowercase
            combinations.append(combo_str.upper())  # uppercase
            combinations.append(combo_str.capitalize())  # first letter capitalized

    # Remove duplicates by converting the list to a set and back to a list
    return list(set(combinations))

# Function to try unlocking USB using a password
def try_password(password):
    # Simulate password testing (replace this with actual USB unlocking logic)
    print(f"Trying password: {password}")
    # Simulate the correct password for demonstration purposes
    correct_password = "CorrectPassword"
    return password == correct_password

# Main function to input hints and try combinations
def main():
    # Input password hints
    input_hints = input("Enter your password hints, separated by commas: ").split(',')
    
    # Generate all possible combinations of hints
    combinations = generate_combinations(input_hints)
    
    # Print the total number of combinations to test
    print(f"Generated {len(combinations)} combinations.")
    
    # Iterate through each combination and try as password
    for password in combinations:
        if try_password(password):
            print(f"Password found: {password}")
            return
    
    print("Password not found in combinations.")

if __name__ == "__main__":
    main()
