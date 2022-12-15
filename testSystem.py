from platform import system
import os

# When importing your own modules, make sure that you select File->Add Folder to Workspace 
# to add the folder where you have placed ALL of your code (including testSystem [this module])

def switch_system():
    """determine which system (Windows or Mac) is in use and sets the base path
       the system type determines what the base path must be
       (Module 4B)
    """
    systemType = system()
    #for Mac, it will say "Darwin"
    if systemType == 'Windows':
        basePath='C:'
        basePath=os.path.join(basePath,os.sep)
        os.chdir(basePath)
        usersPathPiece = "Users"
        # Join the new path with the existing path
        usersPath = os.path.join(basePath,usersPathPiece)
        # Move to the new location and verify it
        os.chdir(usersPath)

    else:
        basePath='Users'
        usersPath=os.path.join(os.sep, basePath)
        os.chdir(usersPath)
        
    return systemType, usersPath
    
def main():
    """main() calls the switch_system function
       This is an example of using the switch_system function - notice the call to the function!
       When you are calling this function in your own code, don't forget to add the name
       of the module - i.e. not just "switch_system()" but "testSystem.switch_system"
       just like you would for the os module 
    """
    print("main")
    systemType, usersPath = switch_system()
    print("System type is: ", systemType, "and new_path is:", usersPath)
    print("Current directory contents: ",os.listdir())

if __name__ == "__main__":
    main()
    

