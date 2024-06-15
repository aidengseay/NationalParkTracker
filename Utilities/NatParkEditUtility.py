################################################################################
# NATIONAL PARK TRACKER EDIT UTILITIES
# ====================================
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
# MAIN EDIT FUNCTION

def mainEditUtility(NatParks):

    choiceRuns = True

    while choiceRuns:
    
        os.system('cls' if os.name == 'nt' else 'clear')
        print("National Park Tracker - Edit")
        print("============================\n")

        print("[1] Update National Park Log - Add")
        print("[2] Update National Park Log - Remove")
        print("[3] Add New National Park")
        print("[4] Quit Edit")

        choice = NatParkUtilities.getProgramChoiceInput(CHOICES)

        match choice:
            case 1:
                updateLogAdd()
            case 2:
                updateLogRemove()
            case 3:
                addNatPark()
            case 4:
                choiceRuns = False

################################################################################
# SUPPORTING FUNCTIONS
                
def addNatPark():
    ...

def updateLogAdd():
    ...

def updateLogRemove():
    ...


################################################################################