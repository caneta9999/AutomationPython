#Credits and Thanks
#https://pypi.org/project/pywhatkit/
#https://github.com/Ankit404butfound/PyWhatKit/wiki/Sending-WhatsApp-Messages
#https://www.pythontutorial.net/python-basics/python-check-if-file-exists/
#https://www.pythontutorial.net/python-basics/python-read-text-file/

import pywhatkit
from os.path import exists
import pandas as pd

class WhatsappMsg:
    def text(self, identification, msg, receiver="contact", instantly=True,hour=0, minute=0, wait_time=15, tab_close=False, close_time=3):
        if instantly:
            if receiver == "contact":
                pywhatkit.sendwhatmsg_instantly(identification, msg, wait_time=wait_time, tab_close=tab_close, close_time=close_time)
            elif receiver == "group":	
                pywhatkit.sendwhatmsg_to_group_instantly(identification, msg, wait_time=wait_time, tab_close=tab_close, close_time=close_time)
        else:
            if receiver == "contact":
                pywhatkit.sendwhatmsg(identification,msg,time_hour=hour,time_min=minute, wait_time=wait_time, tab_close=tab_close, close_time=close_time)
            elif receiver == "group":
                pywhatkit.sendwhatmsg_to_group(identification,msg,time_hour=hour,time_min=minute, wait_time=wait_time, tab_close=tab_close, close_time=close_time)            
    def img(self, identification, img, caption="", wait_time=15, tab_close=False, close_time=3):
            pywhatkit.sendwhats_image(identification, img, caption, wait_time=wait_time, tab_close=tab_close, close_time=close_time)
    def export_previous_messages(self, fileName="PyWhatKit_DB.txt", output="whatsappmsgs.csv"):
        if exists(fileName):
            with open(fileName) as file:
                dictMessages = {'Date': [],'Time': [], 'Receiver': [],'Identification': [], 'Type': [], 'Message': []}
                for line in file.readlines():
                    if "Date" in line:
                        dictMessages['Date'].append(line[6:].replace("\n", ""))
                    elif "Time" in line:
                        dictMessages['Time'].append(line[6:].replace("\n", ""))
                    elif "Phone Number" in line:
                        dictMessages['Receiver'].append("Phone")
                        dictMessages['Identification'].append(line[14:].replace("\n", ""))
                    elif "Group ID" in line:
                        dictMessages['Receiver'].append("Group")
                        dictMessages['Identification'].append(line[10:].replace("\n", ""))
                    elif "Message" in line:
                        dictMessages['Type'].append("Message")
                        dictMessages['Message'].append(line[9:].replace("\n", ""))
                    elif "Image" in line:
                        dictMessages['Type'].append("Image")
                        dictMessages['Message'].append(line[7:].replace("\n", ""))
                pd.DataFrame(dictMessages).to_csv(f".\{output}")
                print("Done")
        else:
            print("There are no previous messages")

whatsapp = WhatsappMsg()
#whatsapp.text(input("Phone number: "),input("Msg: "))
#whatsapp.text(input("Group: "),input("Msg: "), receiver="group")
#whatsapp.text(input("Phone number: "),input("Msg: "),instantly=False,hour=int(input("Hour: ")),minute=int(input("Minute: ")))
#whatsapp.text(input("Group: "),input("Msg: "), receiver="group",instantly=False,hour=int(input("Hour: ")),minute=int(input("Minute: ")))
#whatsapp.img(input("Phone number: "), input("Img path: "), caption=input("Caption: "), wait_time=10, tab_close=True, close_time=5)
#whatsapp.img(input("Group: "),input("Img path: "))
