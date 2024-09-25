import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email subject
subject = "Test Email - Time to submit your tax return!"

# Mailjet credentials
mailjet_api_key = "b050e1847bc69723a8c6eee96a12c43f"
mailjet_api_key = "b050e1847bc69723a8c6eee96a12c43f"
mailjet_secret_key = "93fac1633b701e57183d3b55231bc8d8"
mailjet_secret_key = "be5ada737830982e996e1ab45072ca96"
sender_email = "ahmed.orcho122@gmail.com"
receiver_email = "saad47258@gmail.com"

# Email content
html_template = """
<h1>Hello</h1>
<p>This is a test email.</p>
"""

# Create email message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

# Attach the email body
message.attach(MIMEText(html_template, 'html'))

try:
    # Set up SMTP server connection
    server = smtplib.SMTP('in-v3.mailjet.com', 587)
    server.starttls()  # Secure the connection
    server.login(mailjet_api_key, mailjet_secret_key)

    # Send the email and capture the response
    response = server.sendmail(sender_email, receiver_email, message.as_string())
    
    if response == {}:
        print("Email sent successfully!")
    else:
        print(f"Failed to deliver email, response: {response}")

    # Close the connection
    server.quit()

except Exception as e:
    print(f"Error: {e}")
