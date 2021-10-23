def send_email(str):
	import smtplib
	import getpass
	smtp_object = smtplib.SMTP('smtp.gmail.com',587)
	smtp_object.starttls()
	
	email = "*********23@gmail.com"
	email2 = "*********bert@gmail.com"
	password = "***APP PASSWORD***"
	
	smtp_object.login(email,password)
	subject = "IT IS HERE!!!!"
	message = str
	msg = "Subject: " + subject + '\n' + message
	
	smtp_object.sendmail(email,email,msg)
	smtp_object.sendmail(email,email2,msg)
	smtp_object.quit()
	