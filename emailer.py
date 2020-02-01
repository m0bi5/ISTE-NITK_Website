import importlib
class EmailHandler():
	def __init__(self):
		self.MIMEMultipart=importlib.import_module('email.mime.multipart').MIMEMultipart
		self.MIMEText=importlib.import_module('email.mime.text').MIMEText
		self.imaplib=importlib.import_module('imaplib')
		self.smtplib=importlib.import_module('smtplib')

	def send_email(self,to_id,subject,body,from_id='mobits.bot@gmail.com',from_pass='mobits123'):
		server = self.smtplib.SMTP(host='smtp.gmail.com', port=587)
		server.starttls()
		server.login(from_id, from_pass)

		msg = self.MIMEMultipart()
		msg['From'] = from_id
		msg['To'] = to_id
		msg['Subject'] = subject

		msg.attach(self.MIMEText(body, 'plain'))

		server.sendmail(from_id, to_id, msg.as_string())
		server.quit()

	def read_email(self,from_email,from_pwd,smtp_server,search_filter,smtp_port=993):

		mail = self.imaplib.IMAP4_SSL(smtp_server)
		mail.login(from_email,from_pwd)
		mail.select('inbox')
		result, data = mail.search(None, search_filter)
		mail_ids = data[0]
		id_list = mail_ids.split()
		first_email_id =id_list[0]
		latest_email_id = id_list[-1] #most recent email
		result,data = mail.fetch(latest_email_id, "(RFC822)")
		raw_email = data[0][1].decode('utf-8')

		#read the email
		email_message = email.message_from_string(raw_email)

		return str(email_message)
