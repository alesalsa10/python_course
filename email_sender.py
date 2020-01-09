import smtplib  # this is needed to send emails
from email.message import EmailMessage
from string import Template
from pathlib import Path  # similar to os.path to acceess another file

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Alexander Medina'
email['to'] = 'alexandersalsa10@gmail.com'
email['subject'] = 'You won 1,000,000 dollars'

email.set_content(html.substitute({'name': 'alex'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # starts the server
    smtp.starttls()  # this is the encryption
    smtp.login('alexandersalsa10@gmail.com', 'Am0955667')
    smtp.send_message(email)
    print('all good boss')
