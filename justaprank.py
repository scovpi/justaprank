import os
import time
import sys

running = True

#def cdrive():                    # WORK IN PROGRESS
#    b = 1
#    global running

#    while running:
#        b += 1
#        f = open("C:\hacked" + str(b) + ".txt", 'w')
#        f.write("You thought you had escaped...")
#	f.close()

#        if b >= 5: # 45 max
#            running = False

#    sys.exit()

def main():
    a = 1            # defining a counter for how many files i want to create
    global running   # globalizing the running variable outside of function

    while running:   # while loop
        a += 1       # interating the counter
        f = open("hacked" + str(a) + ".txt", 'w')
        f.write("you have been hacked HAHAHAHAHAHAAHAHA")
        f.close()

        if a >= 45: # 45 maximum : once it reaches this number it will exit
            running = False

    sys.exit()

main()
