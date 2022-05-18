# Sending mail with attached PDFs
# from Gmail account

# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def SendMailToCustomer(emailID, name):

    fromaddr = "selabprojectkumar@gmail.com"
    toaddr = emailID

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Receipt of Your Orders"

    # string to store the body of the mail
    body1 = "Dear %s, \nThank you for shopping with us. The Receipt of your Orders have been attached."%(name)
    body2 = "\n\n\nWith Regards\nBiblio House"

    body = body1 + "\n" + body2

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    filename = "Receipt.pdf"
    attachment = open("receipt.pdf", "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "SElab4thsem")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()


def SendMailToVendor(EmailID, NAME):

    fromaddr = "selabprojectkumar@gmail.com"
    toaddr = EmailID
    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr

    msg['Subject'] = "Requests for the Books"

    # string to store the body of the mail
    body1 = "Dear %s,\nThe following books are in high demands. Please procure these books as soon as possible."%(NAME)
    body2 = "\n\n\nWith Regards\nBiblio House"

    body = body1 + "\n" + body2

    msg.attach(MIMEText(body, 'plain'))
    filename = "Demand.pdf"
    attachment = open("Demands.pdf", "rb")

    p = MIMEBase('application', 'octet-stream')

    p.set_payload((attachment).read())

    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()

    s.login(fromaddr, "SElab4thsem")

    text = msg.as_string()

    s.sendmail(fromaddr, toaddr, text)

    s.quit()

SendMailToVendor("chilukurevasu1234@gmail.com", "John ")