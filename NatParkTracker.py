################################################################################
# NATIONAL PARK TRACKER
# =====================
# This program keeps track of all the national parks we have been to!
# Created by Aiden and Stef, Winter 2023
################################################################################
# IMPORTS
import Utilities.NatParkLogUtility as NatParkLogUtility
import Utilities.NatParkRecUtility as NatParkRecUtility
import Utilities.NatParkEditUtility as NatParkEditUtility
import Utilities.NatParkUtilities as NatParkUtilities
import os

################################################################################
# CONSTANTS
CHOICES = 4
US_CITIES_FILE_NAME = "USCities.csv"
NAT_PARKS_FILE_NAME = "NatParks.csv"

################################################################################
# MAIN FUNCTION
def main():

    programRuns = True

    USCities = NatParkUtilities.importCSVFile(US_CITIES_FILE_NAME)
    NatParks = NatParkUtilities.importCSVFile(NAT_PARKS_FILE_NAME)

    while programRuns:

        os.system('cls' if os.name == 'nt' else 'clear')
        print("National Park Tracker")
        print("=====================\n")

        print("[1] Look at National Park Log")
        print("[2] Edit National Park Log")
        print("[3] Get National Park Recommendations")
        print("[4] Quit Program")

        choice = NatParkUtilities.getProgramChoiceInput(CHOICES)

        match choice:
            case 1:
                NatParkLogUtility.mainLogUtility(NatParks)
            case 2:
                NatParkEditUtility.mainEditUtility(NatParks)
            case 3:
                NatParkRecUtility.mainRecommendUtility(USCities, NatParks)
            case 4:
                programRuns = False
            
    print("\nExit National Park Tracker")

################################################################################
if __name__ == "__main__":
    main()
