from email.message import EmailMessage
import smtplib
import os
import  sys
#reading file 
#my_file_obj = open("/home/shubharthak/Desktop/myip.txt", "r+")
#read_file = my_file_obj.readline(29)
#print(read_file)
#extracting ip and port
#seperator = read_file.split('/')[2].split(':')
#myip = seperator[0]
#myport = seperator[1]
#message to send
#mymessage = f'ssh -X -L 5900:localhost:5900 shubharthak@{myip} -p {myport}'
#print(mymessage)
#authlogin
username = os.environ.get('mymail2')
password = os.environ.get('mypass2')
print(f'Name: {sys.argv[1]}')
print(f'Email: {sys.argv[2]}')
msg = ""
for i in range(3, len(sys.argv)):
    msg+= sys.argv[i] + " "
print(f'Message: {msg}')

with open("contact.txt", 'a') as f:
    f.write(sys.argv[1] + "\t" + sys.argv[2] + "\t" + msg + "\n")

def sendEmail(to, content, name):
    msg = EmailMessage()
    msg['Subject'] = f'Mail from {name}'
    msg['From'] = username
    msg['To'] = to
    msg.set_content(content)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(username, password)
        #smtp.sendmail(username,username,msg)
        smtp.send_message(msg)

content="""
Hello There, 

you just recieved a contact form.

Name: {}
Email: {}
Message: {}

regards,
ApsaraAI
""".format(sys.argv[1], sys.argv[2], msg)

sendEmail(to='shubharthaksangharsha@gmail.com', content=content, name=sys.argv[1])
