# Import QR Code library
import qrcode
import xlrd 


def qrfun(idno):
    # Create qr code instance
    qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4,
    )



    loc = ("details.xlsx") 
    wb = xlrd.open_workbook(loc) 
    sheet = wb.sheet_by_index(0) 
    sheet.cell_value(0, 0) 
   
    print(idno)

    # Add data
    qr.add_data(idno)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image()

    img.save("image.jpg")

    return img