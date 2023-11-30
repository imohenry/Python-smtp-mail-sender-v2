import smtplib
import getpass

HOST = "smtp.mail.yahoo.com"
PORT = 587

FROM_EMAIL = "henry_imoh@yahoo.com"
TO_EMAIL = "henryimoh2@gmail.com,"
PASSWORD = getpass.getpass("Enter password: ")

MESSAGE = """Subject: test mail pls
this is another test mail, I hope this works, this is for kelvin

"""

smtp = smtplib.SMTP(HOST, PORT)

status_code, response = smtp.ehlo()
print(f"[*] Echoing the server: {status_code} {response}")

status_code, response = smtp.starttls()
print(f"[*] Starting TLS connection: {status_code} {response}")

status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
print(f"[*] Logging in: {status_code} {response}")

smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)

smtp.quit()