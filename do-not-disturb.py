#Version beta-01

import os
import sys
import time
from time import gmtime,strftime
import tkinter as tk
#from flask import Flask, request, render_template
#from array import *

customColor = "#c43737"
version = "beta-02"
password = 'Pebble'

def convertTime(hour):
    hourNum = int(hour)
    hourReturn = "0"
    if hourNum > 12:
        hourNum = hourNum - 12
    hourReturn = str(hourNum)
    return hourReturn

def getMeridiem(hour):
    hourNum = int(hour)
    meridiem = "AM"
    if hourNum >= 12:
        meridiem = "PM"
    return meridiem
    
class ClassInfo:
    __name = None
    __dayStart = None
    __hourStart = "0"
    __minuteStart = "00"
    __dayEnd = None
    __hourEnd = "0"
    __minuteEnd = "00"
    __identifier = 0

    def __init__(self, name, dayStart, hourStart, minuteStart, dayEnd, hourEnd, minuteEnd, identifier):
        self.__name = name
        self.__dayStart = dayStart
        self.__hourStart = hourStart
        self.__minuteStart = minuteStart
        self.__dayEnd = dayEnd
        self.__hourEnd = hourEnd
        self.__minuteEnd = minuteEnd
        self.__identifier = identifier

    def setName(self, name):
        self.__name = name

    def setDay(self, dayStart):
        self.__dayStart = dayStart

    def setHour(self, hourStart):
        self.__hourStart = hourStart

    def setMinute(self, minuteStart):
        self.__minuteStart = minuteStart

    def setDayStart(self, dayEnd):
        self.__dayEnd = dayEnd

    def setHourStart(self, hourEnd):
        self.__hourEnd = hourEnd

    def setMinuteStart(self, minuteEnd):
        self.__minuteEnd = minuteEnd
        
    def setIdentifier(self, identifier):
        self.__identifier = identifier

    def setState(self, state):
        self.__state = state

    def getName(self):
        return self.__name

    def getDayStart(self):
        return self.__dayStart

    def getHourStart(self):
        return self.__hourStart

    def getMinuteStart(self):
        return self.__minuteStart

    def getDayEnd(self):
        return self.__dayEnd

    def getHourEnd(self):
        return self.__hourEnd

    def getMinuteEnd(self):
        return self.__minuteEnd
    
    def getIdentifier(self):
        return self.__identifier

    def returnString(self):
        return "Class is in session! \n Day: {} \n Class: {} \n Start Time: {}:{} \n End Time: {}:{}".format(self.__dayStart, self.__name, self.__hourStart, self.__minuteStart, self.__hourEnd, self.__minuteEnd)

class Data():
    #Class Initialization
    WORK_W    = ClassInfo('Work',    'Wednesday', '07', '30', 'Wednesday', '18', '00', 0)
    WORK_Th   = ClassInfo('Work',    'Thursday' , '07', '30', 'Thursday' , '18', '00', 1)
    WORK_F    = ClassInfo('Work',    'Friday'   , '07', '30', 'Friday'   , '18', '00', 2)
    WORK_S    = ClassInfo('Work',    'Saturday' , '07', '30', 'Saturday' , '18', '00', 3)
    CST211    = ClassInfo('CST 211', 'Tuesday'  , '14', '00', 'Tuesday'  , '21', '20', 4)

    def getName(self, ClassInfo):
        return ClassInfo.__name

    def getDayStart(self, ClassInfo):
        return ClassInfo.__dayStart

    def getHourStart(self, ClassInfo):
        return ClassInfo.__hourStart

    def getMinuteStart(self, ClassInfo):
        return ClassInfo.__minuteStart

    def getDayEnd(self, ClassInfo):
        return ClassInfo.__dayEnd

    def getHourEnd(self, ClassInfo):
        return ClassInfo.__hourEnd

    def getMinuteEnd(self, ClassInfo):
        return ClassInfo.__minuteEnd
    
    def getIdentifier(self, ClassInfo):
        return ClassInfo.__identifier

class App():
    __active = False
    currentDay = ""
    currentHour = ""
    currentMinute = ""
    currentSecond = ""
    Data()
    #flask_ = Flask(__name__)
    #flask_.run()

    def __init__(self):
        self.root = tk.Tk()
        
        #Display Day
        self.showDay = tk.Label(text="")
        self.showDay.pack()
        self.showDay.config(font=("Courier", 75), background=customColor, fg="white")
        
        #Display Clock
        self.clock = tk.Label(text="")
        self.clock.pack()
        self.clock.config(font=("Courier", 75), background=customColor, fg="white")
        
        #Class Title
        self.info = tk.Label(text="")
        self.info.pack()
        self.info.config(font=("Courier", 50), background=customColor, fg="white")
        
        #Version Number
        self.version = tk.Label(text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nversion {}".format(version))
        self.version.pack()
        self.version.config(font=("Courier", 12), background=customColor, fg="white", justify="right")
        
        self.updateClock()
        self.root.title("Do Not Disturb")
        self.root.configure(background=customColor)
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(),
                                                self.root.winfo_screenheight()))  

    #@flask_.route('/')
    #def my_form(self):
    #    return render_template('partymode.html')

    #@flask_.route('/', methods=['POST'])
    #def clubPebble(self):
    #    text = request.form['p']
    #    mode = request.form['activate']
    #
    #    if (mode == 'on' and text == password):
    #        return True
    #    else:
    #        return False

    #@flask_.route('/', methods=['POST'])
    #def getPartyColors(self):
    #    partyColors = array('i', [
    #        request.form('first'),
    #        request.form('second'),
    #        request.form('third'),
    #        request.form('fourth')
    #        ])
    #    return partyColors

    def updateClock(self):
        self.currentDay = time.strftime("%A")
        self.currentHour = time.strftime("%H")
        self.currentMinute = time.strftime("%M")
        self.currentSecond = time.strftime("%S")
        output = ""
        day = "\n\n\nToday is: {}".format(self.currentDay)
        now = time.strftime("Current Time: {}:{}:{} {}".format(convertTime(self.currentHour),
                                                                  self.currentMinute,
                                                                  self.currentSecond,
                                                                  getMeridiem(self.currentHour)))
        if (self.check(Data.WORK_W) == True) and (self.currentDay == Data.WORK_W.getDayStart()):
            output = "\nMark is at {}\n\nfrom {}:{}{} to {}:{}{}".format(Data.WORK_W.getName(),
                                                                    convertTime(Data.WORK_W.getHourStart()),
                                                                    Data.WORK_W.getMinuteStart(),
                                                                    getMeridiem(Data.WORK_W.getHourStart()),
                                                                    convertTime(Data.WORK_W.getHourEnd()),
                                                                    Data.WORK_W.getMinuteEnd(),
                                                                    getMeridiem(Data.WORK_W.getHourEnd()))
        elif (self.check(Data.WORK_Th) == True) and (self.currentDay == Data.WORK_Th.getDayStart()):
            output = "\nMark is at {}\n\nfrom {}:{}{} to {}:{}{}".format(Data.WORK_Th.getName(),
                                                                    convertTime(Data.WORK_Th.getHourStart()),
                                                                    Data.WORK_Th.getMinuteStart(),                                                                    
                                                                    getMeridiem(Data.WORK_Th.getHourStart()),
                                                                    convertTime(Data.WORK_Th.getHourEnd()),
                                                                    Data.WORK_Th.getMinuteEnd(),
                                                                    getMeridiem(Data.WORK_Th.getHourEnd()))
        elif (self.check(Data.WORK_F) == True) and (self.currentDay == Data.WORK_F.getDayStart()):
            output = "\nMark is at {}\n\nfrom {}:{}{} to {}:{}{}".format(Data.WORK_F.getName(),
                                                                    convertTime(Data.WORK_F.getHourStart()),
                                                                    Data.WORK_F.getMinuteStart(),
                                                                    getMeridiem(Data.WORK_F.getHourStart()),
                                                                    convertTime(Data.WORK_F.getHourEnd()),
                                                                    Data.WORK_F.getMinuteEnd(),
                                                                    getMeridiem(Data.WORK_F.getHourEnd()))
        elif (self.check(Data.WORK_S) == True) and (self.currentDay == Data.WORK_S.getDayStart()):
            output = "\nMark is at {}\n\nfrom {}:{}{} to {}:{}{}".format(Data.WORK_S.getName(),
                                                                    convertTime(Data.WORK_S.getHourStart()),
                                                                    Data.WORK_S.getMinuteStart(),
                                                                    getMeridiem(Data.WORK_S.getHourStart()),
                                                                    convertTime(Data.WORK_S.getHourEnd()),
                                                                    Data.WORK_S.getMinuteEnd(),
                                                                    getMeridiem(Data.WORK_S.getHourEnd()))
        elif (self.check(Data.CST211) == True) and (self.currentDay == Data.CST211.getDayStart()):
            output = "\nMark is in {}\n\nfrom {}:{}{} to {}:{}{}".format(Data.CST211.getName(),
                                                                    convertTime(Data.CST211.getHourStart()),
                                                                    Data.CST211.getMinuteStart(),
                                                                    getMeridiem(Data.CST211.getHourStart()),
                                                                    convertTime(Data.CST211.getHourEnd()),
                                                                    Data.CST211.getMinuteEnd(),
                                                                    getMeridiem(Data.CST211.getHourEnd()))

        else:
            output = "Mark is not at work!"
        
        #if (self.clubPebble == True):
        #    partyColor = array(self.getPartyColors)
        #    #partyColor = self.getPartyColors
        #    i = 0
        #    while (self.clubPebble == True):
        #        self.root.configure(background=partyColor[i])
        #        self.showDay.config(font=("Courior", 75), background=partyColor[i], fg="white")
        #        self.clock.config(font=("Courior", 75), background=partyColor[i], fg="white")
        #        self.info.config(font=("Courior", 50), background=partyColor[i], fg="white")
        #        self.version.config(font=("Courior", 12), background=partyColor[i], fg="white")
        #        i = i + 1
        #        if (i > 4):
        #            i = 0
        if(self.version == version):
            if (self.currentHour == "22"):
                self.root.configure(background="black")
                self.showDay.config(font=("Courier", 75), background="black", fg="black")
                self.clock.config(font=("Courier", 75), background="black", fg="black")
                self.info.config(font=("Courier", 50), background="black", fg="black")
                self.version.config(font=("Courier", 12), background="black", fg="black")
            elif (self.currentHour == "06"):
                self.root.configure(background=customColor)
                self.showDay.config(font=("Courier", 75), background=customColor, fg="white")
                self.clock.config(font=("Courier", 75), background=customColor, fg="white")
                self.info.config(font=("Courier", 50), background=customColor, fg="white")
                self.version.config(font=("Courier", 12), background=customColor, fg="white")
        
        #Day
        self.showDay.configure(text=day)
        
        #Clock
        self.clock.configure(text=now)
        
        #Class Title
        self.info.configure(text=output)

        self.root.after(1000, self.updateClock)
        
    def getState(self):
        return self.__active
    
    def check(self, schedule):
        if (self.currentHour > schedule.getHourStart()) and (self.currentHour < schedule.getHourEnd()):
            return True
        elif (self.currentHour == schedule.getHourStart()):
            if (self.currentMinute < schedule.getMinuteStart()):
                return False
            else:
                return True
        elif (self.currentHour == schedule.getHourEnd()):
            if (self.currentMinute > schedule.getMinuteEnd()):
                return False
            else:
                return True
        else:
            return False        

app=App()

