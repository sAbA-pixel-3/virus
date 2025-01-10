import smtplib
from email.mime.text import MIMEText
from config import *
import os



def send_message(message):
    sender = 'seconddonutbs@gmail.com'
    to_send = 'cocshbd@gmail.com'
    password_email = PASS

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender, password_email)
        msg = MIMEText(message)
        msg['Subject'] = 'Click Me'
        server.sendmail(sender, to_send, msg.as_string())
        return "Message sent"
    except Exception as e:
        return f"{e} ERROR"
    


def main():
    message = input("Your message: ")
    print(send_message(message))

if __name__ == "__main__":
    main() 