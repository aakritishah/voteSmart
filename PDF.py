### Sophie Hasara, Aakriti Shah, James McIntyre, Alex Hernandez ###
### class for generating pdf if user is logged in ###

from fpdf import FPDF

def generatepdf():
    pdf = FPDF(orientation = 'P', unit = 'mm', format = 'A4')
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, 'Hello World!')
    pdf.output('userresults.pdf', 'F')