# Password generation tool
# Author: Ben J. C. Reeve (BlueNexus)

import random
import string
import os
import math
from appJar import gui

user = []
len_secure_seed = 1024
output_file = ""
app = gui("PyPass", "550x300")
valList = []

def load_configuration():
    configuration = app.getAllEntries()
    configuration['password length'] = int(configuration['password length'])
    configuration['password count'] = int(configuration['password count'])
    return configuration

def parse_radio(rb):
    global valList
    if app.getRadioButton("seclevel") == "characters":
        valList = list(string.ascii_letters)
    elif app.getRadioButton("seclevel") == "chars/digits":
        valList = list(string.ascii_letters + string.digits)
    elif app.getRadioButton("seclevel") == "all printable":
        valList = list(string.ascii_letters + string.digits + string.punctuation)

def file_browser(rb):
    global output_file
    output_file = app.directoryBox(title=None, dirName=None)

def show_config(rb):
    app.showSubWindow("config")

def generate(valList, length):
    password = []
    for char in range(1, length + 1):
        password.append(str(valList[random.randint(1, len(valList) - 1)]))
    return("".join(password))

def start(rb):
    parse_radio("")
    if app.getCheckBox("Use secure seed") is True:
        seed = os.urandom(len_secure_seed)
        random.seed(seed)
    if(load_configuration()['password length'] == 0 or (app.getRadioButton("mode") == "bulk_generation" and load_configuration()['password count'] == 0)):
        app.addListItem("output", "Error: Invalid password generation parameters")
        return
    if app.getRadioButton("mode") == "single password":
        pword = generate(valList, load_configuration()['password length'])
        current = {pword}
        app.addListItem("output", current)
    else:
        for password in range(1, load_configuration()['password count']+1):
            pword = generate(valList, load_configuration()['password length'])
            current = {password: pword}
            user.append(current)
        try:
            with open(output_file + "/output.csv", "w+") as res:
                for item in user:
                    for field, field2 in item.items():
                        res.write(str(field) + ", " + str(field2) + "\n")
                app.addListItem("output", "Done.")
        except:
            app.addListItem("output", "ERROR: FILE ERROR")
            return

### AppJar ###
app.startFrame("config", 0, 0)
app.startLabelFrame("security level",1,0)
app.addRadioButton("seclevel", "characters", 2,0)
app.addRadioButton("seclevel", "chars/digits",3,0)
app.addRadioButton("seclevel", "all printable",4,0)
app.setRadioButtonChangeFunction("seclevel", parse_radio)
app.stopLabelFrame()
app.startLabelFrame("mode",5,0)
app.addRadioButton("mode", "single password", 6,0)
app.addRadioButton("mode", "bulk generation", 7,0)
app.setRadioButtonChangeFunction("mode", parse_radio)
app.stopLabelFrame()
app.addButton("Output location", file_browser, 8, 0)
app.addCheckBox("Use secure seed", 9, 0)
app.stopFrame()
app.startFrame("main", 0, 1)
app.addNumericEntry("password length", 0, 0)
app.addNumericEntry("password count", 0, 1)
app.setEntryDefault("password length", "password length")
app.setEntryDefault("password count", "password count")
app.addButton("Generate", start, 1, colspan=2)
app.setFont(12)
app.addListBox("output", rowspan=2, colspan=2)
app.stopFrame()
app.go()
### AppJar end ###
