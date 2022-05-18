# This file makes a receipt pdf for the customer of the books he bought
# Necessary imports
import random
from datetime import datetime
from fpdf import FPDF

# Connecting to the server
#SalesDb = mysql.connector.connect(host="localhost", user="root", password="Book@123", database="SalesDatabase") 

#mycursor = SalesDb.cursor()

# Selecting the rows of the Table "Sale"
#mycursor.execute("SELECT * FROM Sale")

#myresult = mycursor.fetchall()


Date = datetime.now()
formatted_date = Date.strftime('%d-%m-%Y %H:%M:%S')


# Creating a class of FPDF


class PDF(FPDF):
    def lines(self):
        self.set_line_width(0.0)
        self.line(0, 62.0, 210, 62.0)
        self.line(0, 35.0, 210, 35.0)

    def titles(self):
        self.set_xy(0.0, 0.0)
        self.set_font('Arial', 'B', 16)
        self.set_text_color(220, 50, 50)
        self.cell(w=210.0, h=40.0, align='C', txt="Biblio Home", border=0)

    # Adding Customer details to the pdf
    def CustD(self, name, ContactNum):
        text1 = "     Receipt No.: %s" % (random.randint(1200, 9999))
        text2 = "     Name : %s" % (name)
        text3 = "     Date & Time: %s" % (formatted_date)
        text4 = "     Contact No.: %s" % (ContactNum)

        self.set_text_color(0,0,0)
        self.set_xy(0.0, 40.0)
        self.set_font('Arial', '', 12)
        self.cell(w=210.0, h=5.0, align='L', txt=text1, border=0)

        self.set_xy(0.0, 45.0)
        self.set_font('Arial', '', 12)
        self.cell(w=210.0, h=5.0, align='L', txt=text2, border=0)

        self.set_xy(0.0, 50.0)
        self.set_font('Arial', '', 12)
        self.cell(w=210.0, h=5.0, align='L', txt=text3, border=0)

        self.set_xy(0.0, 55.0)
        self.set_font('Arial', '', 12)
        self.cell(w=210.0, h=5.0, align='L', txt=text4, border=0)

    def makeTable(self, abcd):
        sum = 0
        self.set_xy(10.0, 65.0)
        self.set_font('Arial', 'B', 12)

        # Headings of the table
        self.set_fill_color(193, 229, 252)
        self.cell(120, 10, 'Book Details', 1, 0, 'C', True)
        self.cell(15, 10, 'Copies', 1, 0, 'C', True)
        self.cell(40, 10, 'Price per Copy', 1, 0, 'C', True)
        self.cell(20, 10, 'Price', 1, 1, 'C', True)

        self.set_font('Arial', '', 10)

        for a in abcd:
            self.cell(120, 10, a[0], 1, 0, 'C', False)
            self.cell(15, 10, str(a[1]), 1, 0, 'C', False)
            self.cell(40, 10, str(a[2]), 1, 0, 'C', False)
            self.cell(20, 10, str(a[1] * int(a[2])), 1, 1, 'C', False)
            sum += (a[1] * int(a[2]))

        self.cell(175, 10, 'Total Amount (in Rupees)', 1, 0, 'R', False)
        self.cell(20, 10, str(sum), 1, 1, 'C', False)

        self.set_line_width(0.0)
        self.line(150, 268, 200, 268)
        self.set_xy(150.0, 270.0)
        self.set_font('Arial', 'B', 12)
        self.cell(w=50.0, h=5.0, align='C',
                  txt="Authorised Signature", border=0)




def printReceipt(custName, phone, abcd):
    pdf = PDF()

    pdf.add_page()
    pdf.lines()
    pdf.titles()
    pdf.CustD(custName, phone)
    pdf.makeTable(abcd)

    i = random.randint(1200, 9999)
    pdf.output('receipt' + str(i) +'.pdf', 'F')
    return 'receipt' + str(i) +'.pdf'

#printReceipt("Mohan Kishore", "999999999",myresult)


#mycursor.close()
