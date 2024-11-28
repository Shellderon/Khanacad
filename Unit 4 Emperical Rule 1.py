def calc(mean, std, xxx, why):
    steps = 0
    results_m = mean
    steps_to_right = 0  # Track steps to the right

    for i in range(5):
        results_m += std
        steps += 1 
        
        if round(results_m, 2) == round(xxx, 2):
            steps_to_right = steps
            break  # Once you find the right step, break the loop

    steps = 0  # Reset steps for the left side
    results_m = mean
    steps_to_left = 0  # Track steps to the left

    for i in range(5):
        results_m -= std
        steps += 1
        
        if round(results_m, 2) == round(xxx, 2):
            steps_to_left = steps
            break  # Once you find the left side, break the loop

    # Return a tuple of both steps
    return steps_to_right, steps_to_left

def main():
    try:
        print("1.less than x") 
        choice = input("please choose: ")

        mean = float(input("mean= "))
        std = float(input("std= "))
        xxx = float(input("x= "))
        why = float(input("y= "))

        if choice == '1':
            steps_to_right, steps_to_left = calc(mean, std, xxx, why)  # Get steps to both right and left
            
            # Handle messages based on steps to the right
            if steps_to_right == 1:
                print("hellow")
            elif steps_to_right == 2:
                print("hii")
            
            # Handle messages based on steps to the left
            if steps_to_left == 1:
                print("hellow to the left")
            elif steps_to_left == 2:
                print("hii to the left")
            
    except ValueError:
        print("what the heck are you doing? ")

if __name__ == "__main__":
    main()
