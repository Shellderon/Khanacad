def calc(mean, std, xxx, why, steps):
    result_m = mean
    for i in range(5):
        steps += 1
        result_m += std
        if round(result_m, 1) == round(xxx, 1):
            if steps == 1:
                print("Winners")
            break  # Exit the loop once a match is found
    else:
        print("No match found in first loop.")

    result_m = mean  # Reset result_m for the next loop
    for i in range(5):
        steps += 1
        result_m -= std
        if round(result_m, 1) == round(xxx, 1):
            if steps == 1:
                print("Hi")
            break  # Exit the loop once a match is found
    else:
        print("No match found in second loop.")
    
    return steps  # Return steps so that it can be updated in the main function

def main():
    try:
        print("1. less than x")
        print("2. more than x")
        print("3. in between x and y")
        choice = input("Please choose: ")

        mean = float(input("mean= "))
        std = float(input("std= "))
        xxx = float(input("x= "))
        why = float(input("y= "))

        steps = 0  # Initialize steps in main

        if choice == '1':
            print("Good choice")
            steps = calc(mean, std, xxx, why, steps)  # Pass steps to calc and update it

        elif choice == '2':
            # You can add more functionality for choice 2 if needed
            print("More than x option selected.")

        elif choice == '3':
            # Add logic for choice 3 if needed
            print("In between x and y option selected.")

        print(f"Total steps: {steps}")  # Print the total steps at the end

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
