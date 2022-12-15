import testSystem as ts
import getpass
import os

file="ff_1309217756"

def getFileName():
    """Gets all filenames in directory as a list"""
    fileNames = []

    for file in os.listdir(getPath()):
        f = os.path.join(getPath(), file)
        if os.path.isfile(f):
            file = os.path.basename(f)
            fileNames.append(file)
    return fileNames

def getPath():
    """Gets whole path of source directory"""
    # test to see which system we are in, and get base dir
    baseDir = ts.switch_system()

    # Get User
    try:
        user = getpass.getuser()
    except Exception as error:
        print("Error", error)

    # Combine BaseDir + User + SourceDir
    SOURCE_DIR = "Python_Data\\filesToSort\\"
    PATH = baseDir[1] + '\\' + user + '\\' + SOURCE_DIR

    return PATH

def fileSystem(filename):
    """Recusively creates folders based on first line of file and then move the file"""
    try:
        f = open(getPath() + filename, "r")

    except FileNotFoundError as error:
        print('File not found', error)
        exit()
    else:
        # Get first line of file
        first_line = f.readline()

        # Seperate the date into a list of 3 elements, only digits i.e ['2015','03','20']
        first_line = first_line.strip().split('-')

        # Close so it doesnt throw error later, when moving file
        f.close()
        
        # temporary path, Holds our path when creating subdirectories
        tempPath = getPath()
        count = 0
        for date in first_line:
            
            path = os.path.join(tempPath, date) 
 
            try:
                # Create Year Folder
                os.mkdir(path)


            except FileExistsError as error:
                # if Year  already exist:
                print("File already exist", error)

                # Update path and continue to make Month Folder
                try:
                    tempPath = tempPath + '\\' + date
                    print("2.")
                
                except FileExistsError as error:
                    print("File already exist", error)

                
            else:
                # Update file path
                tempPath = tempPath + '\\' + date

            # Move file, when reached the last elemnt of first_line
            count += 1
            if date == first_line[-1] and count == 3:
                print('3.',tempPath)
                os.rename(getPath() + filename, tempPath + '\\'+ filename)
            
        

def main():
    getPath()
    fileNameList = getFileName()
    #fileSystem(file)

    for file in fileNameList:
        fileSystem(file)

if __name__ == "__main__":
    main()