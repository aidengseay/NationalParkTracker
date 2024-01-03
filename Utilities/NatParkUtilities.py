################################################################################
# NATIONAL PARK TRACKER UTILITIES
# =========================================
# This program keeps track of all the national parks we have been to!
# Created by Aiden and Stef, Winter 2023
################################################################################
# IMPORTS

################################################################################
# CONSTANTS
MIN = 1

################################################################################
# SUPPORTING FUNCTIONS

def getProgramChoiceInput(maxChoice):
    
    inputCorrect = False
    print("")

    while not inputCorrect:

        choice = input("Enter Number: ")
        if( choice.isdigit() and int(choice) >= MIN and int(choice) <= 
                                                                     maxChoice):
            inputCorrect = True
        else:
            print(f"Error: input must be int between {MIN} and {maxChoice}")

    return int(choice)

################################################################################