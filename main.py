import csv

file_name = 'Document.csv'
text_menu = '\n***********************************\n***\tPICK UP MY TRASH v0.1\t***\n***********************************\n(1) - Load file\n(2) - Quit\n'

#=========================================================
def getFileName():                  #Takes users input and returns file_name

    file_name = str(input('Filnamn: '))
    
    return file_name

def readRawFile(fileName):          #Returns a list with the raw CSV-file

    csv_list = []

    with open(fileName, encoding='UTF-8') as f:
        csv_reader = csv.reader(f, delimiter=';')

        for i in csv_reader:
            csv_list.append(i)

    return csv_list

def modifyRawFile(raw_list):        #Returns a rearranged list with 3 cols. Servidnumber, DriverID, Addres. Takes the output from readRawFile as input

    modified_list = []
    row =[]
    service_number = None
    driver_id = None
    adress = None
    
    for i in range(len(raw_list)):

        if len(raw_list[i][0]) == 6 and raw_list[i][0].isdigit():   #Sök ut Tjänstnr som innehåller 6st siffror och testa även om det är siffror. Lägg till i modified_list
            service_number = raw_list[i][0]                         #Kolumn 0 Tjänstnummer
            driver_id = raw_list[i][4]                              #Kolumn 5 Förare
            adress = raw_list[i][6]                                 #Kolumn 7 Adress
        
            row = [service_number, driver_id, adress]
            modified_list.append(row)
        
    return modified_list
    
def writeModifiedFile():            #Writes modified_list to a CSV-file. Takes the output from modifyRawFile as input
    pass
#==========================================================

def mainLoop():
    
    print(text_menu)
    user_chooise = int(input('> '))

    if(user_chooise == 1):
        getFileName()
    
    if(user_chooise == 2):
        SystemExit()
        

#TESTING/////////////////////////////////////////////////////////
#raw_list = readRawFile(file_name)

#new_list = modifyRawFile(raw_list)

#print(new_list[9][2])
#for i in range (101):
#    print(new_list[i]) 

mainLoop()
