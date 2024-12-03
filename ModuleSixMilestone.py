#Nilaris Roberts


# Room dictionary defining the connections between rooms
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}

# Initialize game state variables
currentRoom = 'Great Hall'  # Starting room

# Display Welcome message, current room and instructions
print("Welcome to the simplified text game!")
print("You are currently in the", currentRoom)
print("You can move between rooms using North, South, East, or West commands.")
print("Type 'exit' to quit the game.")

# Main game loop, include exit
while currentRoom != 'exit':
    # Display the current room
    print(f"You are in the {currentRoom}.")

    # Ask for the player's next move
    playerInput = input("Where would you like to go next? ").strip()

    # Check for valid move commands
    if playerInput.lower() == 'exit':
        print("Now exiting the game...Goodbye!")
        currentRoom = 'exit'  # End the game by setting room to 'exit'

    elif playerInput in ['North', 'South', 'East', 'West']:
        # Check if the move is valid for the current room
        if playerInput in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][playerInput]  # Move to the new room
            print(f"You moved to the {currentRoom}.")
        else:
            print("Invalid direction! Try another.")

    else:
        print("Invalid command! Please use 'North', 'South', 'East', 'West' to move or 'exit' to quit.")

# End of game