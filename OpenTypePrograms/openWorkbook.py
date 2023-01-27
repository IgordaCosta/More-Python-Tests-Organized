from win32com.client import Dispatch

import win32com.client as win32

import getTableData


def openWorkbook(xlfile, Invisable=True):
        
    noError=False
    try:
        # excel
        # xlapp

        # excel.Visible = False
          
        # excel.ScreenUpdating = False
        # excel.DisplayAlerts = False
        # excel.EnableEvents = False


        excel = win32.gencache.EnsureDispatch('Excel.Application')

        if Invisable:
            excel.Visible = False
        
            excel.ScreenUpdating = False
            excel.DisplayAlerts = False
            excel.EnableEvents = False

        else:
            excel.Visible = True
        
            excel.ScreenUpdating = True
            excel.DisplayAlerts = True
            excel.EnableEvents = True

        noError=True

    except TypeError:
        noError=False

        splitFile=xlfile.split("\\")

        FileThatisOpened=splitFile[-1]

        print(FileThatisOpened)

        print('FileThatisOpened above')

        # data=[FileThatisOpened]

        # dataName='ListofInlist'

        # getTableData.WriteDataDatabase(data=data,dataName=dataName)

        # save this file as ListofInList so it will be recognized by the program



        wb,excel,noError = '', '', False

        

        print('SheetIsOpenAndHasChanges')



    
    if noError:

        try:

            # excel.Visible = False
          
            # excel.ScreenUpdating = False
            # excel.DisplayAlerts = False
            # excel.EnableEvents = False


            # print("no eror 1")
            excel = win32.gencache.EnsureDispatch('Excel.Application')
            
            # excel.DisplayAlerts = False

            if Invisable:
                excel.Visible = False
            
                excel.ScreenUpdating = False
                excel.DisplayAlerts = False
                excel.EnableEvents = False

            else:
                excel.Visible = True
            
                excel.ScreenUpdating = True
                excel.DisplayAlerts = True
                excel.EnableEvents = True
                excel.WindowState = win32.constants.xlMaximized  # this works for me 

            # print("no eror 2")
            wb = excel.Workbooks.Open(xlfile)

            if Invisable==False:
                
                excel.WindowState = win32.constants.xlMaximized 

            print("AllOK")

            # print("no eror 3")

        except Exception as e:
            # print("no eror exception")
            print(e)
            
            # excel.DisplayAlerts = False
            # excel.Visible = False
          
            # excel.ScreenUpdating = False
            # excel.DisplayAlerts = False
            # excel.EnableEvents = False

            map(lambda book: book.Close(False), excel.Workbooks)
            excel.Quit()
            
            excel = win32.gencache.EnsureDispatch('Excel.Application') 
        
            if Invisable:
                excel.Visible = False
            
                excel.ScreenUpdating = False
                excel.DisplayAlerts = False
                excel.EnableEvents = False

            else:
                excel.Visible = True
            
                excel.ScreenUpdating = True
                excel.DisplayAlerts = True
                excel.EnableEvents = True
            
            # wb
            # xlwb
            wb = excel.Workbooks.Open(xlfile)

            if Invisable:
                excel.Visible = False
            
                excel.ScreenUpdating = False
                excel.DisplayAlerts = False
                excel.EnableEvents = False

            else:
                excel.Visible = True
            
                excel.ScreenUpdating = True
                excel.DisplayAlerts = True
                excel.EnableEvents = True
                excel.WindowState = win32.constants.xlMaximized  # this works for me 

            print("AllOK")
                       
                        
    return(wb,excel,noError)