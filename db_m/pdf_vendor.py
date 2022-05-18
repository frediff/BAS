# This file makes a requirement pdf for the vendors for the books which are in demand
# Necessary imports
from fpdf import FPDF


class PDF(FPDF):
    def lines(self):
        self.set_line_width(0.0)
        self.line(0, 50.0, 210, 50.0)
        self.line(0, 35.0, 210, 35.0)

    def titles(self):
        self.set_xy(0.0, 0.0)
        self.set_font('Arial', 'B', 16)
        self.set_text_color(220, 50, 50)
        self.cell(w=210.0, h=40.0, align='C', txt="Biblio House", border=0)

    def others(self, bookname, isbn, copy):
        self.set_xy(0.0, 40.0)
        self.set_font('Arial', '', 12)
        self.set_text_color(0,0,0)
        self.cell(w=210.0, h=5.0, align='C', txt="These are the books which you need to procure", border=0)

        self.set_xy(10.0, 65.0)
        self.set_font('Arial', 'B', 12)

        # Headings of the table
        self.set_fill_color(193, 229, 252)
        self.cell(120, 10, 'Book Name', 1, 0, 'C', True)
        self.cell(50, 10, 'ISBN', 1, 0, 'C', True)
        self.cell(20, 10, '#copies', 1, 1, 'C', True)

        self.set_font('Arial', '', 10)

        # Different rows of the table
        self.cell(120, 10, bookname, 1, 0, 'C', False)
        self.cell(50, 10, str(isbn), 1, 0, 'C', False)
        self.cell(20, 10, str(copy), 1, 1, 'C', False)

pdf = PDF()

pdf.add_page()
pdf.lines()
pdf.titles()

def pdfvendor(bookName, Isbn, COpy):
    pdf.others(bookName, Isbn, COpy)
    pdf.output('Demands.pdf', 'F')

#pdfvendor("Mohan Ki radha", 9876543120, 21)
