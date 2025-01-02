#Metadata Scraper
#02 January 2025
#dailypythonprojects@substack.com

import os                                   #For reading directories and files
import csv                                  #For exporting as CSV
import time                                 #For converting os operations to a usable time
import inputVal                             #Custom input validation

def getDir():                               #Get file directory as a str
    while True:                             #Loop
        fileDir = inputVal.inputStr("Enter your filepath: ")    #Custom fx to check if a valid str is used
        try:
            if os.path.isdir(fileDir):      #Check that the directory exists
                readDir(fileDir)            #If it does, continue to next fx
                return
            else:
                print("Please enter a valid file directory: ")
                      
        except Exception as e:              #Generic exception handling
            print(f"An exception has occured: {e}. Try again.")
            getDir()


def readDir(dirIn):                         #Use os library to read contents of directory
    try:
        dirCont = os.listdir(dirIn)         #Append directory to a list
        filesList = []                      #List will be used for optional exporting to CSV
        print("Metadata for all files:")
        
        for n in range(len(dirCont)):       #Iterate over each file in the list
            filePath = os.path.abspath(os.path.join(dirIn, dirCont[n]))  #Get full path

            if os.path.isfile(filePath):     #Verify we have a file before gathering metadata
                fileSize = os.path.getsize(filePath)      #Get size in bytes
                createTime = os.path.getctime(filePath)   #Get ctime
                modTime = os.path.getmtime(filePath)      #Get mtime
                fileType = os.path.splitext(dirCont[n])[1]  #Get filetype

                createTimeF = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(createTime))    #Convert the seconds to something readable
                modTimeF = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(modTime))          #Same thing for modification time
            
                print(f"Path: {filePath}, Size: {fileSize} bytes, Created: {createTimeF}, Modified: {modTimeF}, Type: {fileType}")  #Output per file
            
                filesList.append({'filePath': filePath, 'fileSize': fileSize,
                                  'creationTime': createTimeF, 'modificationTime': modTimeF,
                                  'fileType': fileType})    #Append to the list per file
                
        while True:
            exportCsv = input("Do you want to export the metadata as a CSV file? (y/n):")
            try:
                if exportCsv == 'n':
                    return                  #Exit program if they don't want to export
                elif exportCsv == 'y':
                    exportCSV(filesList)    #Continue to next fx
                    return                  #Return after
                else:
                    print("Please enter a valid arg (y/n)")
                    
            except Exception as e:
                print(f"An exception has occured: {e}. Try again.")
                
        
    except Exception as e:                  #Generic exception handling
        print(f"An exception has occured: {e}. Try again.")


def exportCSV(dictIn):                      #Gets our list with the dictionary inside it
    metaDict = dictIn                       #Store list within fx
    outputName = inputVal.inputStr("Enter the output CSV file name (e.g., metadata.csv): ") #Get an output name

    if not outputName.endswith('.csv'):     #Check if the filename doesn't have a valid extension
        outputName += '.csv'                #Add it if it needs it

    try:
        with open(outputName, 'w', newline='') as csvOut:   #Create/write to new custom file name
            writer = csv.DictWriter(csvOut, fieldnames = ['filePath', 'fileSize', 'creationTime', 'modificationTime', 'fileType'])
            writer.writeheader()
            writer.writerows(metaDict)
            print(f'File successfuly exported as {outputName}.')

    except Exception as e:
        print(f"An exception has occured: {e}. Try again.")

def main():
    getDir()

if __name__ == "__main__":
    main()

    
                         
    
