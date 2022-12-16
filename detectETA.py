#!/usr/bin/env python3
#!/usr/bin/env python2

import sys
import os
import smtplib,ssl
import psutil
import img
import math
from PyQt6.QtWidgets import QApplication,QMainWindow
from PyQt6 import uic
from scapy.all import Dot11,Dot11Deauth,sniff
from tkinter import messagebox
from scipy.stats import pearsonr


global myApp
class App(QMainWindow):
    sameSSIDMacAddr = []
    tempPktaddr,deauthAddr,wifi_name = "","",""
    tempSignal = -101
    count=0
    
    def __init__(self):
        super().__init__()
        uic.loadUi('Home.ui',self)
        self.setWindowTitle('Evil Twin Detection')

        self.home_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.home_page))
        self.contact_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.contact_page))
        self.detectpg_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.detected_Page))
        self.sendEmail.clicked.connect(self.send_Email)
        self.detectButton.clicked.connect(self.result)

    def send_Email(self):

        recipient=self.lineEdit.text()
        email=self.textEdit_2.toPlainText()

        #sms port using 465, and password using the google two autho generate password 
        port = 465
        smtp_server = "smtp.gmail.com"
        sender = "leejy-wm19@student.tarc.edu.my"
        password = "rtnodgwqylxqecez" 

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server,port,context=context) as smtp:
            smtp.login(sender,password)
            if(len(email)>10):
                smtp.sendmail(sender,recipient,email)
            else: 
                messagebox.showinfo("Info","Must More then 10 word")
                pass

    #Find the current OS avalable Wi-Fi adaptor
    def analysisWiFiAdaptor(self):
        addresses = psutil.net_if_addrs()
        stats = psutil.net_if_stats()
        
        available_networks = []
        for intface, addr_list in addresses.items():
            if any(getattr(addr, 'address').startswith("169.254") for addr in addr_list):
                continue
            elif intface in stats:
                available_networks.append(intface)
        
        return available_networks
    
    def find_SSID(self):
        #revSSID is to find the same SSID address
        allSSID = {}
        revSSID={}

        #32512 is the terminal error
        if os.system("airmon-ng") == 32512:
            if messagebox.askokcancel("Remider","You don't have the airmon-ng package, click Ok to auto download the airmon-ng package"):
                os.system("pip install airmon-ng -y")
            else: return

        if self.count != 1:
            os.system("airmon-ng start wlan0")
            os.system("airmon-ng check kill")
            os.system("ifconfig wlan0 up")
            

        def PacketHandler (pkt):
           if pkt.haslayer(Dot11):
                #addr2 AP Mac, type 0 management, 1 control and 2 data
                if pkt.type == 0 and pkt.subtype == 8:
                    if pkt.addr2 not in allSSID:
                        allSSID[pkt.addr2] = pkt.info
       
        sniff(iface='wlan0',monitor = True, prn=PacketHandler,timeout = 40)
        if self.count != 1:
            os.system("apt install sox -y")
            self.count += 1
        #To make the sound remind user progress done    
        os.system("play -nq -t alsa synth 0.2 sine 700")

        #print(allSSID)
        #allSSID {"1":"2"}=> revSSD {"2":"1"}. "" to avoid the empty wifi SSID scanning 
        for key,value in allSSID.items():
            if key != "":
                revSSID.setdefault(value,set()).add(key)
        
        #{"ex":["1","2"]} check for same SSID and store to new array
        for key,value in revSSID.items():
            if len(value) > 1 and key.decode() != "":

                #make set become list
                modString = ','.join(value)
                self.sameSSIDMacAddr = modString.split(',')

                #print(self.sameSSIDMacAddr)
                self.wifi_name = key.decode()
                return messagebox.askokcancel("Remind", "There are nearby Wi-Fi with the same name called " + self.wifi_name + ". Do you want to continue Scanning?")
        messagebox.showinfo("Remind", "No nearby Wi-Fi with the same name, Your Are not under Evil Twin Attack")

    def detectDeauth(self):
        
        def dectPack(pkt):
            if pkt.haslayer(Dot11Deauth):
                self.deauthAddr = pkt.addr2
                return True

        sniff(iface="wlan0",stop_filter=dectPack,timeout=40)
        os.system("play -nq -t alsa synth 0.2 sine 700")


        if self.deauthAddr in self.sameSSIDMacAddr:
            messagebox.showwarning("Warning", "WiFi MAC address '" + self.deauthAddr + "' existence deauthentication attack, meaning that " + 
            "the legal AP has been attack. If Currenly connecting in " + self.wifi_name + ", Now will disconnect your Wi-Fi to protect your personal imformation")
        else:
            messagebox.showinfo("Remind", "No nearby Wi-Fi with the same name, Your Are not under Evil Twin Attack")

    def result(self):
        AP1Ux, AP2Ux, finalPearsonrAP1, finalPearsonrAP2, finalResult,tempAdrr = {}, {},{},{},{},{} #dictionary MAC : AP MAC
        sumAP1,sumAP2=[],[]

        #check for the wifi adaptor, default is wlan0
        if "wlan0" not in self.analysisWiFiAdaptor():

            messagebox.showwarning("Remind", "Don't have wlan0 in your computer")
            return 

        #fing the another nearly legal AP, will use later
        if self.find_SSID():
            def findSignal(pkt):
                if pkt.haslayer(Dot11):
                    if pkt.type == 0 and pkt.subtype == 8:
                        if (pkt.dBm_AntSignal > self.tempSignal) and (pkt.addr2 not in self.sameSSIDMacAddr) and (pkt.info != ""):
                            self.tempSignal = pkt.dBm_AntSignal
                            self.tempPktaddr = pkt.addr2

            #sniff package 
            def PacketHandler(pkt):

                #avoid retranmission package
                if pkt.haslayer(Dot11) and pkt.FCfield.retry == False:

                    #addr1 AP Mac addr2 U MAC, pkt.Rate to avoid the None variable
                    if (pkt.addr1 in self.sameSSIDMacAddr or pkt.addr1 == self.tempPktaddr) and pkt.Rate != None:                       
                        #print("!!!!!!!!!!!!")
                        #print(pkt.addr1)
                        #print(pkt.addr2)
                        #print("-----------")
       
                        
                        temp = pkt.addr1
                        if temp == self.tempPktaddr:
                            temp = AP1Ux
                        else: 
                            temp = AP2Ux
                            
                        #40 package per second for one use
                        if len(temp) == 0 or pkt.addr2 not in temp:
                            temp[pkt.addr2] = [pkt.Rate]
                        elif len(temp[pkt.addr2]) < 40:                          
                            temp[pkt.addr2].append(pkt.Rate)
                        elif len(temp[pkt.addr2]) == 40:
                            if  pkt.addr2 not in tempAdrr:
                                tempAdrr[pkt.addr2] = temp[pkt.addr2]
                                #print(tempAdrr)
                                #print(AP1Ux)
                                #print(AP2Ux)
                        
                        #when recive sufficient user data rate will exit sniff, for avoid long processing, set 6min auto exit for sniff in the sniff function 
                        if tempAdrr == {**AP1Ux,**AP2Ux} and (len(AP1Ux) > 0 and len(AP2Ux) > 0):
                            return True

            def calculateSum(AP,sumAP):
                temp = []

                #avoid the array not same error
                try:
                    #array will same so just simply put 0 to get the len of array
                    for x in range(len(list(AP.values())[0])):

                        #To get the all dictionary specific values position. Exp = {"exp1":[1,2,3],"exp2":[4,5,6]},get the 1 and 4, next will get 2 and 5 and so on
                        for y in range(len(list(AP.values()))):
                            temp.append(list(AP.values())[y][x])
                            #print(temp)
                            if y+1 == len(list(AP.values())):

                                #after that add to sumAP and clear the temp and again until end of array
                                sumAP.append(sum(temp))
                                temp = []
                except:
                    pass
    
            def apPearsonResult(AP,sumAP,pAP):
                for key,value in AP.items():
                    #print("=============")  
                    #print(sumAP)
                    #print(value)   
    
                    try:
                        corr,_=pearsonr(sumAP,value)
                        if not (math.isnan(corr)):
                            pAP[key] = corr

                    except:
                        pass
                #print(pAP)
                #print("////////////////////")
                return pAP
            
            def findMacValue(AP):
                maxV=-100
                for value in AP.values():
                    if len(value) > maxV:
                        maxV = len(value)
                
                for key,value in AP.copy().items():
                    if len(value)<maxV:
                        del AP[key]


            sniff(iface="wlan0", monitor = True,prn = findSignal,timeout=40)
            #print(self.tempPktaddr)
            sniff(iface="wlan0", monitor = True,filter="not type mgt and not type ctl",stop_filter=PacketHandler,timeout=360)

            #Cooperate with sniff timeout=360 to avoid array nor diferrent, remove all the array didn't hit the target package data rate
            findMacValue(AP1Ux)
            findMacValue(AP2Ux)

            os.system("play -nq -t alsa synth 0.2 sine 700")

                           
            #print(AP1Ux)
            #print(AP2Ux)
            
            
            calculateSum(AP1Ux,sumAP1)
            calculateSum(AP2Ux,sumAP2)
            
            #print("------------")
            #print(sumAP1)
            #print(sumAP2)

            #calculate final result
            finalPearsonrAP1 = apPearsonResult(AP1Ux,sumAP2,finalPearsonrAP1)
            finalPearsonrAP2 = apPearsonResult(AP2Ux,sumAP1,finalPearsonrAP2)

            #print(finalPearsonrAP1)
            #print(finalPearsonrAP2)

            #both more than 1 to get more accurate about the result, and here is find the bigger pearsonr to know have evil twin or not
            if len(finalPearsonrAP1) > 1 and len(finalPearsonrAP2) > 1:
                fValueAP1,fValueAP2 = {},{}

                for key, value in finalPearsonrAP1:
                    if value > fValueAP1:
                        fValueAP1[key] = value

                for key, value in finalPearsonrAP2:
                    if value > fValueAP2:
                        fValueAP2[key] = value

                
                if fValueAP1 > fValueAP2:
                    finalResult = fValueAP1
                else:
                    finalResult = fValueAP2
                
                # if less then 0.4 will detect the Deauth to confirm is that have someone use Deauth attack to attack the legal AP
                if list(finalResult.values())[0] > 0.4:
                    messagebox.showwarning("Warning", "WiFi MAC address " + list(finalResult.keys())[0] + 
                " probability that it could be a Evil Twin Attack is '"+round(list(finalResult.values())[0]*100,2)+"%'." + 
                "Now will disconnect your Wi-Fi to protect your personal imformation")
                else:
                    self.detectDeauth()
            else:
                self.detectDeauth()        

if __name__ == '__main__':
    app = QApplication(sys.argv)

    myApp = App()
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Closing Window...")
