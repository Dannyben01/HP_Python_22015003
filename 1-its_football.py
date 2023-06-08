def count_down(time_input):
    try:
        time_input = int(time_input)
    except ValueError:
        print("wrong input. Please enter a valur.")
        return
    
    if time_input < 60:
        print("Warning: set time is less than 1 minute.")
    
    while time_input > 0:
        if time_input == int(0.2 * int(time_input)):
            print("Warning: almost finished.")
        print("Time remaining: " + str(time_input))
        time.sleep(1)
        time_input -= 1
    
    print("Completed.")
