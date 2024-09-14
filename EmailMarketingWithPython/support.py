import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# SMTP Server credentials (Sendinblue)
smtp_server = "smtp-relay.brevo.com"
port = 587
username = "7bfeac001@smtp-brevo.com"
password = "Jygkn1IfaFTRYSqc"

# Email details
sender_email = "shad.taxsenselimited@gmail.com"
receiver_email = "saad47258@gmail.com"
subject = "Test Email"
body = "<h1>Hello, World!</h1>"

# Create the message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'html'))

try:
    # Set up the SMTP server
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(username, password)

    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully!")

    # Close the connection
    server.quit()

except Exception as e:
    print(f"Failed to send email. Error: {e}")
