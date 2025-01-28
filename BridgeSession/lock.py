import time

def is_unlocked():
    print("Lock System")

    pin = 6745
    attempts_left = 3

    while True:
        try:
            usr_pin = int(input("Enter your pin: "))
        except ValueError:
            print("Invalid input. Please enter a numeric PIN.")
            continue
        
        if usr_pin == pin:
            print("Access granted")
            break
        else:
            attempts_left -= 1
            print(f"Access denied. You have {attempts_left} attempts left.")
            
            if attempts_left == 0:
                print("You have exhausted all your attempts. Please wait 30 seconds.")
                for i in range(30, 0, -1):
                    print(f"Wait for {i} seconds", end="\r")
                    time.sleep(1)
                print("\nYou can try again now.")
                attempts_left = 3

