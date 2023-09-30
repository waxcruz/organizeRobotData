from multiprocessing import freeze_support
import sys

def main():
    print("Robot Data Collection")
    myArgs = getArgs()
    for i, myArg in enumerate(myArgs):
        print(f"{i+1}. {myArgs[i]}")
    if isValidArguments(myArgs):
        runIt(myArgs)

def isValidArguments(checkArgs):
    print("Kev adds edit code")
    return True

def runIt(myArgs):
    print("Kev add code")

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def getArgs():
    #
    # User provides arguments for program
    #    1. path to source data folder (where on computer the data is located)
    #    2. data location (where data was collected)
    #    3. start date (yyyy-mm-dd)
    #    4. end date (yyyy-mm-dd)
    #    5. destination folder path
    
    if len(sys.argv) == 6:
        sourceDataPath = sys.argv[1]
        videoLocation = sys.argv[2]
        startDate = sys.argv[3]
        endDate = sys.argv[4]
        runFolderPath = sys.argv[5]
        return (sourceDataPath, videoLocation, startDate, endDate, runFolderPath)
    else: 
        print("Invalid command. main sourceDataFolderPath videoLocation startDate endDate runFolderPath")
        return None
    
    
if __name__ == '__main__':
    # Add freeze support so that sub-processes
    # are created correctly in exe file
    freeze_support()
    # Run program
    main()