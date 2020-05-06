import smtplib
from email.mime.text import MIMEText
from email.header import Header
class Mail():
    def __init__(self):
        self.mail_host="smtp.qq.com"
        self.mail_user="785102880@qq.com"
        self.mail_pass="txnqdmpkusprbbif"
        self.message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
    def title(self,title):
        self.message['Subject'] = Header(title, 'utf-8')
    def log(self,str):
        self.message = MIMEText(str, 'plain', 'utf-8')
    def conn(self,people):
            sender = self.mail_user
            receivers = people.split()
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host,25)  # 25 为 SMTP 端口号
            smtpObj.login(self.mail_user, self.mail_pass)
            smtpObj.sendmail(sender, receivers, self.message.as_string())
if __name__=='__main__':
    a = Mail()
    a.log("hello my name is zhangkuoru")
    a.title("HELLO")
    try:
        a.conn('785102880@qq.com')
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


