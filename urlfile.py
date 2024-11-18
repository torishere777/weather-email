#toritimedate
from datetime import datetime
import urllib.request
import smtplib
import time


def getweather():
    contents = urllib.request.urlopen("https://weather.gc.ca/en/location/index.html?coords=49.279,-122.868").read()
    contentstr = str(contents)
    position = (contentstr.find(">Today</strong></a></td><td data-v"))
    position2 = position + 44
    endposition = (contentstr.find("</td></tr><tr cl", position2))
    return contentstr[position2:(endposition):1]

weather = getweather()
print(weather)

from email.message import EmailMessage
def send_mail(to_email, subject, message, server='192.168.1.10',
              from_email='tori-weather@miraline.com'):
    
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = ', '.join(to_email)
        msg.set_content(message)
        print(msg)
        server = smtplib.SMTP(server)
        server.set_debuglevel(1)
        server.send_message(msg)
        server.quit()
        print('successfully sent the mail.')
        

#send_mail(to_email=['vkyrychenko27@gmail.com'],
         # subject='weather forecast ', message = "Today's weather forecast is " + weather)

    

'''while True:
    now = datetime.now()
    timedate = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time is:",  timedate)
    time.sleep(1)
    x = timedate.endswith("00")
    if x is True:
        send_mail(to_email=['vkyrychenko27@gmail.com'], subject='weather forecast ', message = "Today's weather forecast is " + weather)'''

