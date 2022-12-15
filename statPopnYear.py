import makeStructure_zys 
import os

SOURCE_PATH = makeStructure_zys.getPath()

class InvalidYearError(Exception):
    """Custom exception"""
    def __init__(self, value):
        self.value = value


class InvalidKeyWordError(Exception):
    """Custom exception"""
    def __init__(self, value):
        self.value = value


def selection():
    """Selects specific user input keyword and user input year"""
    running = True
    dateList = []
    keyWord = ['sum','average','minimum','maximum']

    # Present Year number from list of folders
    dirs = os.listdir(SOURCE_PATH) 

    # Above line returns list of all filenames, only want numeric numbers for the date
    [dateList.append(fileName) for fileName in dirs if fileName.isnumeric()]
    
    try:
        print("Select a date from the following list: ", dateList)
        inputYear = input("Select Year number: ")
        if inputYear not in dateList:
            raise InvalidYearError("The year number does not correspond to one of the folders listed")
            exit()

        print("Select a Keyword from the following list ", keyWord)
        inputKey = input("Select a Keyword: ")
        if inputKey not in keyWord:
            raise InvalidKeyWordError("The keyword is not one of those listed")
            exit()   

    except InvalidKeyWordError as ike:
        print(ike)

    except InvalidYearError as iye:
        print(iye)
    else:
        return inputYear, inputKey


def output(year, key):
    """Outputs answer based on user inputs"""
    # Get to the directory where files are stored
    YEAR_FOLDER = SOURCE_PATH + '\\' + year
    fileNames = []
    dirPath = []                             
    populationList = []
    longestDirPath = []

    for (dir_path, dir_names, file_names) in os.walk(YEAR_FOLDER):
        fileNames.extend(file_names)
        dirPath.append(dir_path)

    # Get the longest directory path
    longestLength = 49
    for filepath in dirPath:
        if len(filepath) == longestLength:
            longestDirPath.append(filepath)

    # For each file in filenames, output last line into populationList
    count = 0
    for file in fileNames:
        with open(longestDirPath[count] + '\\' + file,"r") as f:
            last_line = f.readlines()[-1].strip() # Get rid of \n
            populationList.append(int(last_line))
        count += 1
    

    # Based on user inputs
    if key == 'sum':
        popListSum = sum(populationList)
        print(f'The {key} population for the year {year} was {popListSum}')
    elif key == 'average':
        popListAve = round(sum(populationList) / len(populationList))
        print(f'The {key} population for the year {year} was {popListAve}')
    elif key == 'maxiumum':
        popListMax = max(populationList)
        print(f'The {key} population for the year {year} was {popListMax}')
    else: # minimum
        popListMin = min(populationList)
        print(f'The {key} population for the year {year} was {popListMin}')

    # this is for Phase 3A
    return fileNames, longestDirPath

def main():
    year = ""
    key = ""
    try:
        year, key = selection()
    except TypeError:
        print("Not in list", TypeError)
    else:
        output(year, key)
    

if __name__ == "__main__":
    main()