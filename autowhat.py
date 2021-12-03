from datetime import datetime
import pywhatkit
import time







def send_msg(phone, msg):
    result = time.localtime()
    pywhatkit.sendwhatmsg(phone, msg, result.tm_hour, result.tm_min+1)

send_msg("+916200771718", "what")

