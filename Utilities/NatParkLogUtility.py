################################################################################
# NATIONAL PARK TRACKER LOG UTILITIES
# ===================================
# This program keeps track of all the national parks we have been to!
# Created by Aiden and Stef, Winter 2023
################################################################################
# IMPORTS
import Utilities.NatParkUtilities as NatParkUtilities
import os

################################################################################
# CONSTANTS
CHOICES = 4

################################################################################
# MAIN LOG FUNCTION

def mainLogUtility(NatParks):

    choiceRuns = True

    while choiceRuns:
    
        os.system('cls' if os.name == 'nt' else 'clear')
        print("National Park Tracker - Log")
        print("============================\n")

        print("[1] Get Percentage")
        print("[2] Get Parks To Do")
        print("[3] Get Parks Done")
        print("[4] Quit Log")

        choice = NatParkUtilities.getProgramChoiceInput(CHOICES)

        match choice:
            case 1:
                getPercentage()
            case 2:
                getParksToDo()
            case 3:
                getParksDone()
            case 4:
                choiceRuns = False


################################################################################
# SUPPORTING FUNCTIONS
                
def getParksDone():
    ...

def getParksToDo():
    ...
                
def getPercentage():
    ...


################################################################################