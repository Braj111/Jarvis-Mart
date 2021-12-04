from datetime import datetime
import pywhatkit
import time



def send_msg(phone, msg):
    result = time.localtime()
    pywhatkit.sendwhatmsg(phone, msg, result.tm_hour, result.tm_min+2)



