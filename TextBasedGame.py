# Nilaris Roberts


# Game art, define instructions
def display_intro():
    intro_art = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀beep⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠖⠒⠒⠦⡄⠀⢠⠄⠀⠀⠀⠀
⠀⠀⠀⠀⠒⠀⠠⠄⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⢠⣋⠂⢀⠀⠀⠀⠀⡠⠞⠀⠀⠀⠄⠀
⠂⠀⠀⠀⠀⠨⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡏⠀⣠⠔⠋⠀ ⠈⡇⠐⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⢀⠀⠀⠀⠀⠈⡣⣺⣥⣶⡀⠀ ⠄⣰⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠚⠉⠘⠮⢍⣝⡥⠞⠁⠀⠀⠀⠀⠐⠀⠀boop⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀
⠀⠁Alien Adventure Game⠀⠀⠄⠀⠀⠀⠀⠈⠀⠀⠀⠀⠄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⠀⠀⠀ . .⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠔⠋⢠⠔⠊⠁⠀⠀⠉⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⢀
⠀⠀⠀⠀⠀⠀⠎⠁⣠⠊⠀⢀⡤⠂⠊⠉⠉⠉⠻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠎⠀⠀⠀⠀⡐⠁⣠⠖⢦⠀⠸⡀⠀⠙⡄⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀
⠄⠀⠀⠀⡜⢠⠀⠀⠀⢐⠃⠀⡇⠀⢸⠀⠀⢸⠀⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢊⠘⡄⠀⠀⠘⢆⣀⣀⣠⠃⠀⢠⠏⠀⠀⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⣆⢳⡀⠀⠀⠀⠀⠀⣀⣀⡴⠊⠁⠀⠀⡆⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠂⠀⠀
⠀⠀⠠⠀⠀⠀⠘⠪⠑⠒⠀⠀⠀⠀⠀⠀⠀⢀⡠⠃ ...Welcome to the Space Station!⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠁⠈⠈⠈⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    print(intro_art)


# Call the display_intro function to show the artwork at the game start
display_intro()


# define instructions
def show_instructions():
    instructions = """
    🛰️ **Alien Adventure Game Instructions** 🛰️
    ------------------------------------------------
    Goal: Collect all the required items and access the escape pod **without encountering the alien**.

    **Move Commands:**
    - 'Go North', 'Go South', 'Go East', 'Go West' — move between rooms.

    **Inventory Commands:**
    - 'get [item name]' — add an item to your inventory.

    **Items to Collect:**
    1. Core and Generator (both in the **Engineering Room**).
       - Collect both items before leaving the room.
    2. Map
    3. Flashlight
    4. Supplies
    5. Key

    **Winning Condition:**
    - Collect **all items** before entering the Escape Pod Room.

    **General Tips:**
    - Type 'exit' anytime to quit the game.

    🚀 The game is starting. You are in the Cryo-Chamber with no items..  Good luck, and watch out for the alien!** 🚀
    """
    print(instructions)


# Show win art
def display_win():
    win_art = '''
⢸⡟⠳⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⡇⠀⠀⠙⠲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡇⠀⣀⠤⢊⠜⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢻⠭⠄⠂⠁⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠸⡇⠀⠀⠀⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣦⡤⠤⠤⠶⣦⡀⠀⠀⠀⠀
⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⡀⠀⠀⠈⢯⡉⠉⠀⠀⢳⡄⠀⠀⠀
⠀⠀⠀⠸⡆⠀⠀⠀⠰⣏⢹⡄⠀⠀⠀⢳⡀⠀⠀⠀⠹⣄⠀⠀
⠀⠀⠀⣠⢿⡄⠀⠀⠀⠹⣏⠹⣄⡠⠎⠁⣻⣤⣤⣀⣀⡘⢦⠀
⠀⢀⡴⡣⠃⢻⡀⠀⠀⣀⠼⣆⠹⣆⣠⠞⠋⠳⣄⠀⠀⠉⠉⠁
⠀⠀⢻⡀⠀⠀⢻⡉⠁⠀⣀⣸⣧⠘⣇⣠⢔⡿⠛⠀⠀⠀⠀⠀
⠀⠀⠀⢳⡀⠀⠀⡿⣞⠋⠁⣀⡬⣧⡘⣿⢋⡀⠙⠢⡀⠀⠀⠀
⠀⠀⠀⠀⢳⡀⣸⠃⠹⣶⠽⠖⢋⠉⠋⠁⠀⢈⣱⠀⠹⡄⠀⠀
⠀⠀⠀⠀⠀⢳⡟⠀⠀⠀⠀⡇⢈⠀⢀⡀⠐⡞⠃⠀⠀⣷⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠘⢴⠁⠑⢤⠇⠀⢰⠲⡿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⣀⡞⠓⠦⡄⠀⣸⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⢹⣴⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀
    '''
    print(win_art)
    print("Congrats! You've avoided the alien and collected all items. You Win!! ")


# Show loss art
def display_loss():
    loss_art = '''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡤⠶⠒⠒⠒⠒⠲⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠖⠉⠁⠀⠀⠀⠀⠁⠀⠐⠤⣄⠉⠓⢦⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠈⠣⣀⠀⠈⠳⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠈⠁⠀⠀⠉⠀⠀⠀⠁⠉⠉⠁⠀⠀⢀⡠⠀⣄⠀⠀⠘⢧⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⢠⠀⠀⠀⠒⠀⠈⠒⠀⠀⠀⠠⠤⠆⠀⠁⠀⠀⠀⠁⠀⢆⠈⣇
⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⡇⠀⠀⠀⠀⠈⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⢸
⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢀⣸
⠀⠀⠀⠀⠀⠀⠀⠀⠘⣟⣼⡆⠀⠀⠀⠀⣀⡀⠠⠤⢄⣀⠤⠄⠀⠀⠀⠀⠀⠀⠀⡎⣞⡏
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⢿⣇⣤⠄⠀⠀⢀⡉⠉⠓⠒⠒⠒⠋⠉⡁⠀⠀⠠⢤⣀⣿⢿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣟⣉⡤⢤⢤⢤⣀⡉⠲⡀⠀⠀⠀⡴⠊⣁⡠⡤⡤⠤⣈⡻⡟⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⣿⣿⠛⠛⢻⢷⣯⡂⠘⠀⠀⠚⢐⣮⠿⠿⣟⣿⣿⣿⡎⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣦⡘⣿⣿⣷⣿⣿⣿⣿⡄⠀⠀⢀⣾⣷⣤⣶⣿⣿⣿⡏⣠⡏⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣵⡙⢯⣻⢿⣿⣿⣿⣿⠀⠀⢸⢿⣿⣿⡿⣟⡿⢋⣼⠟⠀⠀
⢀⣠⣀⠀⠀⢠⠖⢲⡀⠀⠀⠈⢻⣄⠈⠉⠿⠿⠛⠋⠀⠀⠘⠛⠛⠿⠏⠉⢀⡽⠋⠀⠀⠀
⢸⡅⠹⡄⠀⢸⡄⢸⠇⠀⠀⠀⠀⢻⣑⡀⠀⠀⠀⠾⠖⠰⡾⡆⠀⠀⠀⣜⡽⠁⠀⠀⠀⠀
⠀⢳⡄⢷⠀⢰⠃⢻⠀⠀⠀⠀⠀⠀⠻⡷⣄⡀⠀⠀⠀⠀⠀⠀⠀⣠⣼⠟⠁⠀⠀⠀⠀⠀
⠀⠈⢧⡈⣧⢸⡀⣼⠀⠀⠀⠀⠀⠀⠀⠈⠻⣧⠈⠉⠭⠭⠍⢁⢰⡿⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⣇⠈⡿⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣄⠀⠁⢀⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡴⢺⠯⠤⠤⠖⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⡷⢶⣿⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠻⡞⠳⢶⣾⡶⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣼⢿⠁⠀⡝⣾⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠙⢦⠴⠁⠀⠀⣸⠀⠀⠀⢀⣀⣤⣠⠤⠾⢁⡀⣇⢠⠇⡅⠻⠦⣄⣀⣀⡀⠀⠀⠀⠀
⠀⠀⠀⠘⢷⣜⠒⠲⣏⠀⠀⡴⡿⠀⠀⠈⠁⠒⠋⠀⠈⠉⠀⠘⠒⠖⠁⠀⠀⠩⣳⡀⠀⠀
⠀⠀⠀⠀⠀⢹⡐⢧⢻⠀⠀⣷⠁⠀⢰⠀⠀⠀⠀⠀⠲⡶⠂⠀⠀⠀⠀⡇⠀⠀⢧⡇⠀⠀
⠀⠀⠀⠀⠀⠈⡇⠀⠈⣧⠀⣟⠀⠀⣨⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⣸⠀⠀⢩⡇⠀⠀
⠀⠀⠀⠀⠀⠀⢻⠀⠀⠘⡾⠁⠐⣾⡟⡷⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⢾⣿⠁⠀⠉⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠸⣆⠀⠀⠸⡀⢰⣿⠁⢿⢄⡀⠀⠀⠴⠷⠄⠀⠀⢀⣾⡏⠀⠀⠀⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣯⣆⠀⠀⢹⣟⡏⠀⢸⠦⠀⠀⠀⠀⡄⠀⠀⠀⠠⣧⣿⠀⠀⢸⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⣜⢦⣀⡜⡞⠀⠀⢸⡓⢀⡁⠀⠀⡇⠀⠀⡀⠐⣿⡇⠀⠀⠈⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢶⣥⡽⠁⠀⠀⢸⣅⣤⣄⣀⣀⣀⣀⣀⣤⣈⡿⢷⡀⣀⣸⠇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠀⠀⠀
    '''
    print(loss_art)
    print("ALIEN HIVE!! You've encountered the alien! Game over.")


# rubric 3: begin developing a main function code
# Show player status
def showStatus(currentRoom, inventory, rooms):
    print(f"\nYou are currently in the {currentRoom}.")
    print(f"Inventory: {inventory}")

    room_items = rooms[currentRoom]["items"]

    if room_items:  # Check if there are items in the room
        if isinstance(room_items, list):  # Multiple items in the room
            print("You see the following items:", ", ".join(room_items))
            for item in room_items:
                ascii_items_art(item)  # Display ASCII art for each item
        else:  # Single item in the room
            if room_items.lower() == "supplies":
                print(f"You see the {room_items}.")  # Use 'the' for supplies
            else:
                print(f"You see a {room_items}.")
            ascii_items_art(room_items)
    else:
        print("There is nothing here.")


# Movement function
def move(direction, currentRoom, rooms):
    if direction in rooms[currentRoom]["connections"]:
        return rooms[currentRoom]["connections"][direction]
    else:
        available_directions = ", ".join(rooms[currentRoom]["connections"].keys())
        print(f"Invalid direction! You can move in the following directions: {available_directions}")
        return currentRoom  # Stay in the same room if move is invalid

def collect_item(item_name, current_room, inventory, rooms):
    """Attempt to collect an item from the current room."""
    room_items = rooms[current_room]["items"]

    if isinstance(room_items, list) and item_name in room_items:
        inventory.append(item_name)
        room_items.remove(item_name)  # Remove collected item from the list
        print(f"You have collected the {item_name}.")
        ascii_items_art(item_name)  # Display the ASCII art for the item
    elif room_items == item_name:
        inventory.append(item_name)
        rooms[current_room]["items"] = None  # Remove the item from the room
        print(f"You have collected the {item_name}.")
        ascii_items_art(item_name)  # Display the ASCII art for the item
    else:
        print(f"There is no {item_name} in this room.")

def ascii_items_art(item_name):
    art_dict = {
        "Map": '''
       ⠀⠀⠀⠀⢀⣀⣀⣐⣀⣀⣀⣀⠀⠀⢀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⡤⣖⣛⢥⠀⠀⠘⠀⠀⠘⣿⠉⠁⠸⠓⠄⠀⠀⠀⠇⠒⠉⠙⣾⠻⢦⡉⠂⢄⡀⠀⠀⠀⠀
⢹⣄⡹⢜⡞⠀⠀⠀⠀⠀⠀⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⢻⣆⡔⣭⠆⠀⠀⠀
⢸⠀⠀⡼⠀⠀⠀⠀SpaceCraft Map⠀⠀⠀⠀⠀⠀⠉⡽⣍⠙⢶⠀⠀⠀⠀⠀
⠀⡇⡇⠀⠀⠀⠀|Legend:|         *      ⡇⢰
 ⡇⡇     | * = You|⠀⠀ ⡽⣍⠙⠀⠀⠀⠀⠀⠀⠀⡇⢰⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⠀⠀⠀⡽⣍⠙⠀⠀⠀⠀⠀⠀⠀..⠀.  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢘⠀⠀⠀⠀⠀⠀⠀
⠸⣶⣷⡧⠤⡄⣀⡟⠧⠤⠤⢤⠤⢤⡤⠤⢴⢿⣉⡐⠦⠤⡯⠦⢄⣀⡀⢀⣿⣆⣼⠀⠀⠀⠀

        '''
        ,
        "Core": '''
    ⡴⠊⠁⠀⠀⠀⠀⠀⠀⠀
⢀⡴⠁⠀⠀⠀⠀⣸⡆⠀⠀⠀⠀⠀⠀⠀
⡎⠀⠃⢀⢔⣤⠎⠚⠻⣆⡀⠀⠀⠀⠀⠀
⠈⠪⣀⣵⣿⣅⠀⠀⣀⠀⢞⣆⠀⠀⠀⠀
⠀⠀⠀⠀⠙⢿⡗⣠⠄⠙⢀⢨⢿⡟⠂⠀
⠀⠀⠀⠀⠀⠈⠻⢷⣷⣔⣁⡨⠫⡀⠁⣠
⠀⠀⠀⠀⠀⠀⠀⠀⡭⠿⠋⡀⠀⡈⢲⠔
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠪⣡⣨⣀⠜⠁⠀

        '''
        ,
        "Generator": '''
         ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀             ⣀⣼⢿⡄⠀⠀⠀
⢀⣀⣿⠉⣉⣉⣉⣉⡉⣉⡉⢉⣾⢣⡬⢿⣄⠀⠀
⢸⣿⣿⠀⣉⣉⣉⡉⠁⠙⢁⡿⠃⣻⠗⠀⢻⣆⠀
⢸⣿⣿⠀⢺⣶⣾⡂⠀⠀⠿⠷⠶⠷⠶⢶⠶⠿⠆
⠈⠛⣿⡀⠘⠛⠛⠂⠀⠀⠀⠀⠀⠀⢀⣿⠄⠀⠀
⠀⠀⠈⢻⡿⣿⠛⠛⠛⠛⠛⠛⣿⢿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

        '''
        ,
        "Flashlight": '''⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⣻⡄
⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⡾⣿⣯⢿⣷⡿⠟⠀
⠀⣠⣴⣶⣶⣶⡿⣿⣻⣽⣽⣷⡿⠛⠁⠀⠀⠀
⢸⡇⣴⣬⠿⣻⣹⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀
⠀⢯⢶⢒⣧⢹⣿⣿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠻⣎⣱⣹⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        '''
        ,
        "Supplies": '''
        ⣠⣀⣀⣄⠀⠀⠀⠀⠀⠀⠀
⡠⠒⠒⠐⠒⠒⠒⠓⠒⠒⠚⠓⠒⠒⠒⠒⠒⢄
⡇⠀⠀⠀⠀⠀⠀⢀⠀⢀⡀⠀⠀⠀⠀⠀⠀⢸
⡇⠀⠀⠀⠀⠀⡌⠀⢰⡆⠈⢣⠀⠀⠀⠀⠀⢸
⡇⠀⠀⠀⠀⠸⡅⠿⢿⡿⠿⢠⡇⠀⠀⠀⠀⢸
⡇⠀⠀⠀⠀⠀⠑⢤⣘⣓⡤⠎⠀⠀⠀⠀⠀⢸
⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸
 ⠀⠐⠒⠒⠒⠓⠒⠒⠚⠓⠒⠒⠒⠒⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

        '''
        ,
        "Key": '''

  ⠀⠀⠀⠀⠀      ⡀⣀⠉⠣⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⠰⡄⠐⠺⣥⠀⠱⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠺⡀⠀⡄⠀⡀⠚⠀⣴⠆
 ⠀⠀⠀⠀⠀⠀⠀⠀⣬⠞⢦⡀⣀⡀⣀⢞⠇⠀
 ⠀⠀⠀⠀⠀⠀⢀⡾⠁⢀⡾⠛⠛⠛⠛⠀⠀⠀
 ⠀⠀⠀⠀⢠⢞⠁⢀⡰⠉⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⣠⠖⠙⢴⡕⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⡴⠋⠁⡠⠠⠏⠲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠳⢶⢤⢎⠀⠐⣢⡶⠶⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⢛⢦⠆⠀⠀⠀      

        '''

    }
    # Check if the item has ASCII art
    if item_name in art_dict:
        print("\n" + "-" * 50)  # Add a separator for better clarity
        print(art_dict[item_name]) # Display ASCII art
        print("-" * 50)  # Another separator
    else:
        print(f"No ASCII art available for {item_name}.")

# Collect Item Function
def collect_item(item_name, currentRoom, inventory, rooms):
    """Handles item collection logic."""
    room_items = rooms[currentRoom]["items"]

    if isinstance(room_items, list):  # Multiple items in the room
        if item_name in room_items:
            inventory.append(item_name)
            room_items.remove(item_name)
            print(f"You have collected the {item_name}.")
            ascii_items_art(item_name)
        else:
            print(f"{item_name} is not in this room!")
    elif room_items == item_name:  # Only one item in the room
        inventory.append(item_name)
        rooms[currentRoom]["items"] = None
        print(f"You have collected the {item_name}.")
        ascii_items_art(item_name)
    else:
        print(f"{item_name} is not in this room!")

# rubric: decision branching to handle different commands and control the program flow
# Main game loop
def main():
    currentRoom = "Cryo-Chamber"
    inventory = []
    alienRoom = "Alien Hive Room"
    itemsCollected = 0
    totalItems = 6  # Total items needed to win
    gameOver = False

    # Rooms dictionary: Combining items and connections
    rooms = {
        "Cryo-Chamber": {"items": None, "connections": {"North": "Navigation Room", "East": "Control Room", "South": "Living Quarters", "West": "Storage Room"}},
        "Navigation Room": {"items": "Map", "connections": {"South": "Cryo-Chamber", "East": "Engineering Room"}},
        "Engineering Room": {"items": ["Core", "Generator"], "connections": {"West": "Navigation Room"}},
        "Living Quarters": {"items": "Flashlight", "connections": {"North": "Cryo-Chamber", "East": "Escape Pod Room"}},
        "Storage Room": {"items": "Supplies", "connections": {"East": "Cryo-Chamber"}},
        "Control Room": {"items": "Key", "connections": {"West": "Cryo-Chamber", "North": "Alien Hive Room"}},
        "Alien Hive Room": {"items": None, "connections": {"South": "Control Room"}},
        "Escape Pod Room": {"items": None, "connections": {"West": "Living Quarters"}}
    }

    # Show instructions
    show_instructions()

    # Game loop
    while not gameOver:
        showStatus(currentRoom, inventory, rooms)

        command = input("Enter your move (go [direction], get [item], or type 'exit' to quit): ").split()
        if not command:
            print("You must enter a command!")
            continue

        if command[0].lower() == "exit":
            print("Thanks for playing! Goodbye.")
            break

        elif command[0].lower() == "go":
            if len(command) < 2:
                print("You must specify a direction! (e.g., 'go North')")
                continue
            direction = command[1].capitalize()  # Normalize input direction
            currentRoom = move(direction, currentRoom, rooms)  # Update room based on direction

        elif command[0].lower() == "get":
            if len(command) < 2:
                print("You must specify an item to collect!")
                continue

            item = command[1].capitalize()
            room_items = rooms[currentRoom]["items"]

            # Check if the item is already in the inventory
            if item in inventory:
                print(f"You've already collected the {item}.")
                continue

            # Handle case for multiple items in the room (like Engineering Room)
            if isinstance(room_items, list):
                if item in room_items:
                    inventory.append(item)
                    itemsCollected += 1
                    room_items.remove(item)  # Remove collected item from the room
                    print(f"You have collected the {item}.")
                    ascii_items_art(item)  # Display ASCII art for the collected item
                else:
                    print(f"{item} is not in this room!")

            # Handle case where only one item is in the room
            elif room_items == item:
                inventory.append(item)
                itemsCollected += 1
                rooms[currentRoom]["items"] = None  # Remove item from room after collecting it
                print(f"You have collected the {item}.")
                ascii_items_art(item)  # Display ASCII art for the collected item
            else:
                print(f"{item} is not in this room!")

        # Win or lose condition (after item collection logic)
        if itemsCollected == totalItems and currentRoom == "Escape Pod Room":
            display_win()
            gameOver = True
        elif currentRoom == alienRoom:
            display_loss()
            gameOver = True


# Run if meets all rubric requirements
if __name__ == "__main__":
    main()
