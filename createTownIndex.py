import testSystem as ts
import statPopnYear as pop
import getpass
import os


filename = "ff_3198409"


def getBaseDir():
    """Return path for base directory"""
    baseDir = ts.switch_system()
    # Get User
    try:
        user = getpass.getuser()
    except Exception as error:
        print("Error", error)
    # Combine BaseDir + User 
    
    PATH = baseDir[1] + '\\' + user
    return PATH


def indexFile():
    """Create text file to be edited"""
    # Create file in base directory
    f = open(getBaseDir() + "\\" +  "townFileIndex.txt","a")
    f.close()
    fileNames, longestDirPath = pop.output()
    print(fileNames)
    print(longestDirPath)

def main():
    indexFile()

if __name__ == "__main__":
    main()