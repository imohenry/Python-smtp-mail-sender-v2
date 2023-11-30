import smtplib
import getpass

HOST = "" #preferred smtp host server
PORT =  #port

FROM_EMAIL = "" #sender mail
TO_EMAIL = "" #receiver mail
PASSWORD = getpass.getpass("Enter password: ") #getpass makes sure your password is secure

MESSAGE = """Subject: test mail pls
this is another test mail. 

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
