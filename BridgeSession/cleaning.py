import random 
import time 

for i in range (0,20):
    print()
    for j in range (0,10): 
        print(random.randint(10,99), end = " ")

print("\n Cleaning in progress")

for i in range (0,20):
    print()
    for j in range (0,10):
        time.sleep(1) 
        print(0, end = " ")

print("Cleaning done")