import sys

GoodChoice = 0

def TranslateGate():
    print("I see, what language are you planning to translate into? Please do not include spaces.")
    translatorLanguage = raw_input()
    Translate(translatorLanguage)

def Translate(_lang):
    #WIP
    currentTranslation = open(_lang+"Translation.txt","a")
    terms = []
    for i in open("originTranslation.txt","r").readlines():
        i = i.replace(",\n","")
        terms.append(i)
    while (len(terms) > 0):
        print("Please translate the following:")
        currentTermTranslated = raw_input(terms[0]+" > ")
        currentTranslation.write(currentTermTranslated+",\n")
        terms.pop(0)


def UpdateMasterFile():
    finished = 0
    while finished == 0:
        goodChoice = 0
        while goodChoice == 0:
            print("Would you like to add a new term ('1') or start over ('2')? Type 'quit' to exit.")
            userChoiceUpdate = raw_input()
            if userChoiceUpdate == "1" or userChoiceUpdate == "2":
                goodChoice = 1
                if int(userChoiceUpdate) == 1:
                    update = raw_input("New Term: ")
                    masterFile = open("originTranslation.txt","a")
                    masterFile.write(update+",\n")
                else:
                    print("Master file wiped.")
                    masterFile.close()
                    masterFile = open("originTranslation.txt","w")
                    masterFile.write('')
            else:
                if userChoiceUpdate == "quit":
                    sys.exit()
                print("Sorry, please enter '1' or '2'.")



# INITIALIZATION, KEEP BELOW EVERYTHING ELSE

while GoodChoice == 0:
    print("Hello there brave translator. Dare ye to translate (Type '1') or doth ye dare to edit the master translation file (Type '2')?")
    userChoice = input()
    if userChoice == 1 or userChoice == 2:
        GoodChoice = 1
        if userChoice == 1:
            TranslateGate()
        else:
            UpdateMasterFile()
    else:
        print("Good sir, it seems that your hand has slipped. Type '1' or '2'.")
