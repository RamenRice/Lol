myWordLength = ''
keepGoing = True
while keepGoing == True:
    theWord = str(input('input word : '))
    myWordLength = theWord
    print(len(myWordLength))
    myWordLength = ''
    wouldKeepGoing = input('Would you like to keep going? : ').lower()
    if wouldKeepGoing == 'y' or wouldKeepGoing == 'yes':
        keepGoing = True
    else:
        keepGoing = False
