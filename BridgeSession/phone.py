import time
import lock  

def check_app_lock(pin):
    attempts_left = 3 
    while attempts_left > 0:
        try:
            usr_pin = int(input("Enter the PIN to unlock the app: "))
        except ValueError:
            print("Invalid input. Please enter a numeric PIN.")
            continue

        if usr_pin == pin:
            print("App unlocked!")
            return True
        else:
            attempts_left -= 1
            print(f"Incorrect PIN. Attempts left: {attempts_left}")
            
            if attempts_left == 0:
                print("Too many failed attempts. Please wait 30 seconds.")
                for i in range(30, 0, -1):
                    print(f"Wait for {i} seconds", end="\r")
                    time.sleep(1)
                print("\nYou can try again now.")
                attempts_left = 3 
    return False

lock.is_unlocked() 

print("\nAPPS:")
print("1. Settings\n2. Phone\n3. Block Clash\n4. Phone Book\n5. Music Player")

choice = int(input("Enter a number to open an app: "))

app_pins = {
    1: 1234,  # Settings
    2: 5678,  # Phone
    3: 9101,  # Block Clash
    4: 1121,  # Phone Book
    5: 3141   # Music Player
}
match choice:
    case 1:
        print("Opening Settings...")
        if check_app_lock(app_pins[1]):
            print("Settings: You can now adjust system configurations.")
    case 2:
        print("Opening Phone...")
        if check_app_lock(app_pins[2]):
            print("Phone: You can now make a call.")
    case 3:
        print("Opening Block Clash...")
        if check_app_lock(app_pins[3]):
            print("Block Clash: Game is loading...")
    case 4:
        print("Opening Phone Book...")
        if check_app_lock(app_pins[4]):
            print("Phone Book: You can now view your contacts.")
    case 5:
        print("Opening Music Player...")
        if check_app_lock(app_pins[5]):
            print("Music Player: You can now listen to your songs.")
    case _:
        print("Invalid choice. Please select a valid app number.")
