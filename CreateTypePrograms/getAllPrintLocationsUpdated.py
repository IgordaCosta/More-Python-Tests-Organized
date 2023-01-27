from os import walk
import pandas
import pprint


def DeleteFromLIstIFCharacterInText(ListToToCheck, characterToCheck):
    
    if len(ListToToCheck) == 0:
        return ListToToCheck

    else:

        finalLineList = []
        for lineToCheck in ListToToCheck:

            if characterToCheck in lineToCheck:
                pass
            
            else:
                finalLineList.append(lineToCheck)


    return finalLineList



def DeleteCharacterListIfNotInText(ListToRemoveCharacters, characterList):

    ListChanging = ListToRemoveCharacters

    for characterTOCheck in characterList:

        ListChanging2 = DeleteFromLIstIFCharacterInText(ListToToCheck=ListChanging, characterToCheck=characterTOCheck)

        ListChanging = ListChanging2


    return ListChanging



def FilterTxtFileIntoList(FolderLocation = '', filenameCheked = '', ListOfLiines= [], CheckValuesList= [], CheckIfIN=True ):

    mypath0 = FolderLocation

    if mypath0 == '':
        mypath = mypath0
    
    else:
        mypath = mypath0 + '\\'

    continueON = False

    try:
        file1 = open(mypath + filenameCheked, 'r')
        Lines = file1.readlines()
        continueON = True

    except:
        pass       

    if len(ListOfLiines)>0:
        Lines = ListOfLiines
        continueON = True 
       
    if continueON:
        LIstOfLInes = []

        TrueContinueList = []
        for line0 in Lines:
                line = [ord(character) for character in line0]
                
                checkAllList = []
                for ValueUsed0 in CheckValuesList:
                    ValueUsed = ord(ValueUsed0)
                                        
                    if CheckIfIN:
                        for item in line:
                            if item == ValueUsed:
                                TrueContinueList.append(line0)
                                break
                    
                    else:
                        ItemInList = False
                        for item in line:
                            if item == ValueUsed:
                                ItemInList = True

                            checkAllList.append(ItemInList)

                                    
                checkused = all(ItemInList)
                if checkused:
                    pass

                else:
                    TrueContinueList.append(line0)

        TrueContinueList2 = list(set(TrueContinueList))
        
        return TrueContinueList2



def ListOfLinesIntoOrdCodeString(ListOfLiines):

    ListOfLiines2 = str(ListOfLiines).replace('[', '').replace("'", '').replace('"', '').replace(',', '').replace(']', '')

    OrdList = [ord(item) for item in ListOfLiines2]

    OrdList2 = str(OrdList).replace('[', '').replace(']','').replace('32', "DDD").replace(', ' ,'')


    return OrdList2



def CheckIfTextInOrNot(TextToCheck, TextLine, InText=True):

    OrdListOfLiines = ListOfLinesIntoOrdCodeString(TextLine)

    OrditemToCheck= ListOfLinesIntoOrdCodeString(TextToCheck)

    if InText:
        Result = OrditemToCheck in OrdListOfLiines
    
    else:
        Result = OrditemToCheck not in OrdListOfLiines

    return Result



def InAndNotInTextLine(TextLine, ToCheckInText='', toCheckNOTinText = ''):

    IsInText = ''

    IsNOTInText = ''

    AddToText = ''

    if ToCheckInText == '':
        pass

    else:
        InText = True
        IsInText = CheckIfTextInOrNot(TextToCheck= ToCheckInText, TextLine= TextLine, InText=InText)

    if toCheckNOTinText == '':
        IsNOTInText = True
    
    else:
        InText2 = False

        IsNOTInText =CheckIfTextInOrNot(TextToCheck= toCheckNOTinText, TextLine=TextLine, InText=InText2)

    if IsInText:
        if IsNOTInText:
            AddToText = True
        else:
            AddToText = False
    
    else:
        AddToText = False


    return AddToText




def AppendnAndNotInTextLineList(ListOfTextLInes,ToCheckInText='', toCheckNOTinText=''):

    AllowedLines = []
    for lineToCheck in ListOfTextLInes:
        ToAppend = False
        
        ToAppend = InAndNotInTextLine(TextLine= lineToCheck, ToCheckInText=ToCheckInText, toCheckNOTinText = toCheckNOTinText)

        if ToAppend:
            AllowedLines.append(lineToCheck)

    
    return AllowedLines




def LIstOfInOrNOtTextAppendTextLineGroup(ListOfTextLInes,ToCheckInTextList, toCheckNOTinTextList ):


    if len(ToCheckInTextList) == 0:
        LisofOfLInesAppended2 = []

    else:

        LisofOfLInesAppended = []
        toCheckNOTinText = ''
        for ToCheckInText in ToCheckInTextList:
            NewListTOAdd = AppendnAndNotInTextLineList(ListOfTextLInes,ToCheckInText=ToCheckInText, toCheckNOTinText=toCheckNOTinText)

            LisofOfLInesAppended = LisofOfLInesAppended + NewListTOAdd




    LisofOfLInesAppended2 = list(set(LisofOfLInesAppended))

    LisofOfLInesAppended3 = DeleteCharacterListIfNotInText(ListToRemoveCharacters = LisofOfLInesAppended2, characterList = toCheckNOTinTextList)



    return LisofOfLInesAppended3




def AppendnAndNotInTextLineListFromTxt(Location,filenameCheked, ToCheckInText, toCheckNOTinText, outputtxtPath):

    OutputFileName = 'UniqueImportsShort.txt'
    
    file1 = open(Location + filenameCheked, 'r')
    ListOfTextLInes = file1.readlines()

    AcceptedLineList = LIstOfInOrNOtTextAppendTextLineGroup(ListOfTextLInes,ToCheckInTextList= ToCheckInText, toCheckNOTinTextList=toCheckNOTinText )

    file1 = open(outputtxtPath + OutputFileName, 'w')
    file1.writelines(AcceptedLineList)
    file1.close()
       

    return AcceptedLineList
    

# Location = r'C:\Users\Tigereye\Desktop\PythonJSImportFiles' + '\\'


# filenameCheked = 'JSuniqueImports.txt'

# toCheckNOTinText = ['<', '>', '(', ')', '{', '}', '[', ']', '//', "'", '"', 'jquery', 'bootstrap', 'BACKUP']

# ToCheckInText = ['+']

# outputtxtPath = Location




# pprint.pprint(AppendnAndNotInTextLineListFromTxt(Location,filenameCheked, ToCheckInText, toCheckNOTinText, outputtxtPath))