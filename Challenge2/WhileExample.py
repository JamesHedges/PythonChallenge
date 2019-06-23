import time
import random

tired = time.perf_counter()

def GettingTired():
    return (tired + 1) < time.perf_counter()

lookingCounter = 0

def LookForSomething():
    global lookingCounter
    lookingCounter += 1
    myRandom = random.randint(1, 100)
    print(myRandom)
    return myRandom > 100

start = time.perf_counter()

def TimeIsUp():
    return (start + 5) < time.perf_counter()

notFound = True
while notFound:
     if TimeIsUp():
        print("Time is up :(")
        break  # done with the loop        
     if GettingTired():
        print ("Getting Tired, resting...")
        time.sleep(1)
        tired = time.perf_counter()
        continue  # do the next iteration            
     if LookForSomething():
        print (f"Found It! in {lookingCounter} tries")
        notFound = False  # when something is found, end the loop