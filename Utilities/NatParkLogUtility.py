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

def mainLogUtility(natParks):

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
                getPercentage(natParks)
            case 2:
                getParksToDo(natParks)
            case 3:
                getParksDone(natParks)
            case 4:
                choiceRuns = False


################################################################################
# SUPPORTING FUNCTIONS
                
def getParksDone(df):
    print(df)

    parksCompleted = df.loc[(df['stef']) & (df['aiden'])]

    print(parksCompleted)
    

    input()

def getParksToDo(df):
    ...
                
def getPercentage(df):
    
    parksCompleted = df.loc[(df['stef']) & (df['aiden'])]

    percent = ( len(parksCompleted) / len(df) ) * 100


################################################################################