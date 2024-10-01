
  # try:
  #       password = "axer ouoh ldmd aocq"# my
  #       sender_email = "shad.taxsenselimited@gmail.com"
  #       server = smtplib.SMTP('smtp.gmail.com', 587)
  #       server.starttls()
  #       server.login(sender_email, password)
  #       print("Shad Logged In")
  # except Exception as e:
  #       print("Unsuccessful Login")
  #       print(e)
  #       # exit()
  
  # while p!=EmailsPerAccount:
  #     if column_data[c] in read_list:
  #       print("Already Sent ", column_data[c])
  #       c=c+1
  #       continue
  #     try:
  #       msg = MIMEMultipart()
  #       msg['From'] = sender_email
  #       msg['To'] = column_data[c]
  #       msg['Subject'] = subject
  #       msg.attach(MIMEText(html_template, 'html'))
  #       server.sendmail(sender_email,column_data[c], msg.as_string())
  #       n=n+1
  #       s=s+1
  #       p=p+1
  #       if n==1:
  #          print("Shad Logged In")
  #       print(f"Email sent: {n}  ", f"Shad {s}", " Email Sending Failed: ",f)
  #     except Exception as e:
  #       print(e)
  #       f=f+1
  #       print("Email Sending Failed: ",f)
  #       print(column_data[c])
  #       if "sending limits go" in e:
  #         break
  #       time.sleep(5)
  #       continue


  #     with open('sent.txt', 'a') as file:
  #       file.write(f"{column_data[c]}\n")
  #       print(column_data[c])
  #     c=c+1

   

  # server.quit()
  # print("Shad Logged out")
