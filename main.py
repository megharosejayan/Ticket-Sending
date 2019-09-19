
import xlrd 

from create_certificate import createpage
from send import mail
from qr import qrfun


loc = ("details.xlsx") 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 
for i in range (1,6):
    print(sheet.cell_value(i,2))
    print(sheet.cell_value(i,0))
    print(sheet.cell_value(i,5))

    name=sheet.cell_value(i,2)
    seat=sheet.cell_value(i,0)
    food=sheet.cell_value(i,5)
    cusat=sheet.cell_value(i,4)
    idno=sheet.cell_value(i,6)   #idno is a unique id which will be showed when the qr code is scanned
    #rmail=sheet.cell_value(i,1) #rmail is the receiver's mail
    body= "Hi "+name+" Wassup"
    print(body)

    image = qrfun(idno)         #calling function to generate qr code. Return the QR code image 

    createpage(name,seat,food,cusat,image)   #calling function to create pdf
    #mail(rmail,body)        
    #mail("jyothisp52@gmail.com",body)                
    mail("megharose15@gmail.com",body)       #calling function to send mail

