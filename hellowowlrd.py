def calculate_steps(mean, std, x, direction='left', max_steps=5, tolerance=1e-6):
    """
    Calculate the number of steps required to reach a target value 'x' by incrementing (or decrementing)
    the result based on 'mean' and 'std'.
    """
    result = mean
    steps = 0
    step_increment = -std if direction == 'left' else std  # Adjust step based on direction
    
    for i in range(max_steps):
        result += step_increment
        steps += 1
        if abs(result - x) < tolerance:  # Check if result is close enough to target 'x'
            return steps
    return steps

def print_steps(steps, direction):
    """
    Print a message based on the number of steps calculated.
    """
    messages = {
        1: f"\033[32m16% with 1 step to the {direction}\033[0m",
        2: f"\033[32m2.5% with 2 steps to the {direction}\033[0m",
        3: f"\033[32m0.15% with 3 steps to the {direction}\033[0m",
        4: f"\033[32m99.75% with 4 steps to the {direction}\033[0m",
        5: f"\033[32m100% with 5 steps to the {direction}\033[0m"
    }
    if steps in messages:
        print(messages[steps])
    else:
        print(f"\033[32mNo exact match within {steps} steps to the {direction}\033[0m")

def main():
    try:
        # User choices for calculation type
        print("\033[32m1. Less than x\033[0m")
        print("\033[32m2. More than x\033[0m")
        choice = input("Please choose: ").strip()

        # Taking input for mean, standard deviation, and target values
        mean = float(input("\033[31mMean = \033[0m"))
        std = float(input("\033[31mStandard deviation = \033[0m"))
        x = float(input("\033[31mTarget value (x) = \033[0m"))
        y = float(input("\033[31mAnother value (y) = \033[0m"))

        if choice == '1':  # Calculate steps for less than x (towards left)
            steps_left = calculate_steps(mean, std, x, direction='left')
            steps_right = calculate_steps(mean, std, x, direction='right')

            print(f"Steps to the left: {steps_left}")
            print_steps(steps_left, 'left')
            print(f"Steps to the right: {steps_right}")
            print_steps(steps_right, 'right')

        elif choice == '2':  # Calculate steps for more than x (towards right)
            steps_left = calculate_steps(mean, std, x, direction='left')
            
            steps_right = calculate_steps(mean, std, x, direction='right')

            print(f"Steps to the left: {steps_left}")
            print_steps(steps_left, 'left')
            print(f"Steps to the right: {steps_right}")
            print_steps(steps_right, 'right')

        else:
            print("Invalid choice. Please select 1 or 2.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
