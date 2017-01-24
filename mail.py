import smtplib

class sendMail():
    
    def __init__(self, username, password, fromaddr):
        self.username = username
        self.password = password
        self.fromaddr = fromaddr
        self.msg = " "
        
    def setMsg(self, subject, text):
        self.msg = "\r\n".join([ "Subject: "+ subject, text ])
        
    def resetMsg(self):
        self.msg = " "
        
    def sendMsg(self, toaddrs):
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(self.username,self.password)
        server.sendmail(self.fromaddr, toaddrs, self.msg)
        server.quit()
        self.resetMsg()