# Wrapper program to simplify lock and unlocking

from DoorControl import lock_door, unlock_door
import time

while True:
    # Ask user for input
    usr_input = input('What do? lock(l), unlock(u), or quit(q)?\n')
    if (usr_input == 'lock') or (usr_input == 'l'):
        lock_door()
    elif (usr_input == 'unlock') or (usr_input == 'u'):
        unlock_door()
    elif (usr_input == 'quit') or (usr_input == 'q'):
        break
    time.sleep(1)
