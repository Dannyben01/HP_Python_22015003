while True:
    command = input("Enter 'toss' to roll the dice or 'quit' to end the game: ")
    
    if command == 'toss':
        dice_roll = random.randint(1, 6)
        print("You rolled a", dice_roll)
        
    elif command == 'quit':
        print("Thanks for playing!")
        break
        
    else:
        print("Invalid input. Please enter 'toss' or 'quit'.")
