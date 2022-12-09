# Additional Functions to make the code looks neater

# import only system from os
from os import system, name
from time import sleep
 
# define our clear function
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def opening():
    a = 'System is Booting Up'
    for i in range(3):
        clear()
        a += '.'
        print(a)
        sleep(1)