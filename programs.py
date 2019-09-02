#!C:\Python27\python.exe
import smtplib
import cgi
print "Content-type: text/html\n"

form = cgi.FieldStorage()
c_name = form.getvalue('firstname' , '')

to = 'nvishnukiran222@gmail.com'
gmail_user = 'chandu.vardhan007@gmail.com'
gmail_pwd = 'cricket@1'
smtpserver = smtplib.SMTP("smtp.gmail.com" , 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(gmail_user , gmail_pwd)
msg = "%s"%(c_name)
smtpserver.sendmail(gmail_user , to , msg)
print "done"
smtpserver.quit()