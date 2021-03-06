import json

quote = {}    #This is the dictionary 'memory buffer' if you will. Quotes are written to here before they are appended to the data list.
data = []    #The data list that the program reads and writes to from the data.txt file.


def inputInt(prompt):    #This function repeatedly prompts for input until an integer is entered.
    keepGoing = True
    while keepGoing:
        something = input(prompt)
        if something.isdigit() == True:   #Prompts the user to enter the value specified in the parameters, and confirms that it is a digit.
            keepGoing = False
    return int(something)    #Required function #1. Subtract 1 to account for lists beginning at 0.


def inputSomething(prompt):    #This function repeatedly prompts for input until something (not just whitespace) is entered.
    keepGoing = True
    while keepGoing:
        something = input(prompt).strip()    
        if something:    #If, after stripping the whitespace, the string contains 'value' of True,
            keepGoing = False   
    return str(something)    #Return the value that it was testing for value. Required function #2


def saveChanges(dataList):    #This function opens "data.txt" in write mode and writes dataList to it in JSON format.
    f = open('data.txt', 'w')    #Open the file in write mode.
    json.dump(dataList, f)    #Take the data list, and dump the data into data.txt using JSON format. #Requirement #3.
    f.close() 


def formatQuoteAbb(enumerator, quoteText, quoteAuthor, quoteYear):    #This function formats the quote appropriately for Abbreviated form.
    if len(quoteText) > 40:    #If the length of the quote is greater than 40 characters,
        quoteText = quoteText[:40] + "..."    #then cap it at 40 characters and add "...".
    if quoteYear == "u":    #If the year is 'unknown',
        yearString = ''   
    else: yearString = ', ' + quoteYear

    print(enumerator, ') "', quoteText, '" - ', quoteAuthor, yearString, sep='')    #If the year is known, print the string like this.
        

def formatQuoteFull(quoteText, quoteAuthor, quoteYear):    #This function formats the quote appropriately for Full form.
    print('"', quoteText,'"', sep='')
    if quoteYear == "u":
        yearString = ''
        #print('  - ', quoteAuthor, sep='')
    else: yearString = ', ' + quoteYear
    
    print('  - ', quoteAuthor, yearString, sep='')

    
###############################################################################################################################################################
    

try:
    f = open('data.txt', 'r')    #Open the file in read mode and assigns information to variable 'f'.
    data = json.load(f)    #Read the json data from 'f' into the 'data' varaible(list). Requirement #1.
    f.close()    
    print ("\nLoaded data from file")
    
except: 
    print("\nFailed to load data.txt. Writing data to list.")
    

print ("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-(*)-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print ("\n\tWelcome to the QuoteMaster Admin Program!")
print ("\n\t      A Program by Brandon Gordon")
print ("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-(*)-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

while True: 
    print('\nChoose from the following menu options: \n\t[A]dd\n\t[L]ist\n\t[S]earch\n\t[V]iew\n\t[D]elete\n\t[Q]uit.')    #Menu options. Requirement #2.
    choice = input('> ').upper()    #The input line required for users to choose options and STORES AS CAPITAL LETTER.
        
    if choice == 'A':    #If user chooses [A]dd. Requirement #3.
        quote['Quote'] = inputSomething("Enter the quote: ")
        quote['Author'] = inputSomething("Enter the author's name: ")
        quote['Year'] = inputSomething("Enter the year (enter 'u' if unknown): ").lower()
        data.append(quote.copy())    #Append a COPY of the quote dictionary to the data list. A copy is required else a pointer would be appended and you would get a list of the same thing over and over again!
        print ("Quote added!")
        saveChanges(data)

    
    elif choice == 'L':    #If the user chooses [L]ist. Requirement #4.
        if len(data) == 0:    #Check if user has input any quotes
            print ("There are no quotes saved.")
        else:
            print ("List of quotes: ")
            for quotenum, quoteInfo in enumerate(data, 1):
                formatQuoteAbb(quotenum, quoteInfo['Quote'], quoteInfo['Author'], quoteInfo['Year'])



    elif choice == 'S':    #If the user chooses [S]earch. Requirement #5.
        search = inputSomething("Enter a search term: ").lower()
        for quotenum, quoteInfo in enumerate(data, 1):
            checker1 = str(quoteInfo['Quote']).lower()    #get the lowercase information about the quote and the author and then combine it into "checkstring" to compare against search query
            checker2 = str(quoteInfo['Author']).lower()
            checkstring = checker1 + checker2
            if search in checkstring:
                formatQuoteAbb(quotenum, quoteInfo['Quote'], quoteInfo['Author'], quoteInfo['Year'])



    elif choice == 'V':    #If the user chooses [V]iew. Requirement #6.
        view = inputInt("Quote number to view: ")-1    #Assign the int value that inputInt() will return. Subtract 1 to account for list starting at index 1, not 0.
        try:
            formatQuoteFull(data[view]['Quote'], data[view]['Author'], data[view]['Year'])
        except IndexError:
            print("Invalid index number")

        

    elif choice == 'D':    #If the user chooses [D]elete. Requirement #7.
        delet = inputInt("Quote  number to delete: ")-1
        try:
            del data[delet]    #Delete  the list index number as specified by "delet"
            print ("Quote deleted!")
            saveChanges(data)
        except IndexError:
            print ("Invalid index number")

        

    elif choice == 'Q':    #If the user chooses [Q]uit. Requirement #8.
        print ("Goodbye!")
        break



    else:    #If the user inputs anything other than the sepcified menu options. Requirement #9.
        print ("Invalid Choice")

