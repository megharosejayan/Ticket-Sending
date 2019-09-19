from PyPDF2 import PdfFileWriter, PdfFileReader
import io
import xlrd 


from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from create_certificate import createpage,createpdf

# Adding custom fonts. 1st parm is the name of the font and 2nd is the path to the ttf font file.
pdfmetrics.registerFont(TTFont('Roboto', 'RobotoMono-Medium.ttf'))
pdfmetrics.registerFont(TTFont('RobotoL', 'RobotoMono-Light.ttf'))

#from create_certificate.py import createpage

print("asvdgfdt")

createpdf()