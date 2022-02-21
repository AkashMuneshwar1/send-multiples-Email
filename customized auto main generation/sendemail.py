import smtplib
import csv

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    message_template = read_template('template.txt')
    MY_ADDRESS = '@gmail.com' #Email of sender
    PASSWORD='*****'   #Password of sender Email

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)


    with open('details.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for lines in csv_reader:

            msg = MIMEMultipart()
            message = message_template.substitute(PERSON_NAME=lines[0],MATH=lines[2],ENG=lines[3],SCI=[4])
            print(message)

            msg['From'] = MY_ADDRESS
            msg['To'] = lines[1]
            msg['Subject'] = "mid term grades"

            msg.attach(MIMEText(message, 'csv'))

            s.send_message(msg)
        del msg
    s.quit()

if __name__ == '__main__':
    main()

