# -*- coding: utf-8 -*-

#last change - October 20th 2022

import tkinter as tk
from datetime import datetime
from os import getenv, startfile

# assigning the basic variables
Login = getenv('username').lower()
lines = "---"*10
reps = []

#tk setup
master = tk.Tk()
master.configure(background='#f2f2f2')
master.title("Global Shift Reports Widget - (Updated Nov 22)")

#initial buttons setup
pixel = tk.PhotoImage(width=1, height=1)
fsrButton = tk.Button(master, padx=0, pady=0, text = "FSR", bg="lightyellow", image=pixel, width=70, height=70, compound="c", command = lambda: select_team("FSR"))
cnButton = tk.Button(master, padx=0, pady=0, image=pixel, width=70, height=70, compound="c", text = "Chinese", bg="lightyellow", command = lambda: select_team("China"))
euButton = tk.Button(master, padx=0, pady=0, image=pixel, width=70, height=70, compound="c",text = "EU ", bg="lightyellow", command = lambda: select_team("EU"))
apacButton = tk.Button(master, padx=0, pady=0, image=pixel, width=70, height=70, compound="c",text = "APAC", bg="lightyellow",  command = lambda: select_team("APAC"))
auButton = tk.Button(master, padx=0, pady=0, image=pixel, width=70, height=70, compound="c",text = "AU", bg="lightyellow",  command = lambda: select_team("AU"))
quitButton = tk.Button(master, padx=0, pady=0, image=pixel, width=70, height=70, compound="c", text="Quit", bg="pink", command=master.quit)

#input boxes setup
foo = tk.StringVar()
foo2 = tk.StringVar()
foo3 = tk.StringVar()
srEntry = tk.Entry(master, textvariable=foo, width=100)
countryEntry = tk.Entry(master, textvariable=foo2)
accountEntry = tk.Entry(master, textvariable=foo3)

#label setup
srLabel = tk.Label(master, text="Shift Report", background='#f2f2f2', font=("Helvetica", 12))
countryLabel = tk.Label(master, text="Country", background='#f2f2f2', font=("Helvetica", 12))
accountLabel = tk.Label(master, text="Account", background='#f2f2f2', font=("Helvetica", 12))
label_noAccess = tk.Label(master, text="The widget could not find the Shift Report file to log your Shift Report.\nPlease make sure you are connected to the X folder since the Shift Report file is stored there.\n"
						  "You may have to open the X folder first in order to connect to it before using the Shift Report Widget", background='#f2f2f2', font=("Helvetica", 11))
label_noCountry = tk.Label(master, text="Please enter a Country or an Account.", background='#f2f2f2', font=("Helvetica", 12))
label_noSR = tk.Label(master, text="Please enter a Shift Report!", background='#f2f2f2', font=("Helvetica", 12))


#this function clears the GUI
def clear_buttons():
	slaves = master.grid_slaves()
	for s in slaves:
		s.grid_forget()

#this function clears the text in the labels
def clear_text():
	foo.set("")
	foo2.set("")
	foo3.set("")

#laying first content (the team selector)
def first_screen():
	clear_buttons()
	
	lblInst = tk.Label(master, text="Global Shift Reports Widget", background='#f2f2f2', font=("Helvetica", 12)).grid(column=1,row=1, columnspan=3)
	fsrButton.grid(column=1, row=2)
	cnButton.grid(column=2, row=2)
	euButton.grid(column=3, row=2)
	apacButton.grid(column=1, row=3)
	auButton.grid(column=2, row=3)
	quitButton.grid(column=3, row=3)

#defining the team that is using the shift report
def select_team(foo):
	global repsLocation, srLocation, team
	repsLocation = "X:\\Sales\\Shortcuts\\!Shift_Reports_Folder\\reps" + str(foo) + ".txt"
	srLocation = "X:\\Sales\\Shortcuts\\!Shift_Reports_Folder\\ShiftReports" + str(foo) + ".txt"
	team = foo
	main_function()

#this function gets the most updated date and time
def getDate():
		now = datetime.now()
		NiceNow = now.strftime("%Y-%m-%d at %H:%M:%S")
		return NiceNow

#this function recreates the GUI
def recreate_buttons():
	clear_buttons()
	srEntry.grid(row=1, column=2, columnspan=4, sticky=tk.W)
	srEntry.focus_set()
	srLabel.grid(row=1, column=1)
	
	countryEntry.grid(row=2, column=2, sticky=tk.W)
	countryEntry.focus_set()
	countryLabel.grid(row=2, column=1)

	accountEntry.grid(row=3, column=2, sticky=tk.W)
	accountEntry.focus_set()
	accountLabel.grid(row=3, column=1)

	sendButton.grid(row=2,column=3)
	quitButton.grid(row=4,column=3)
	optionsButton.grid(row=3,column=3)
	#clear_text()

#this function sets up all the buttons and labels for the main shift report layout
def laying_content(team):
	clear_buttons()
	lblInst = tk.Label(master, text="Using %s team's file" % team, background='#f2f2f2', font=("Helvetica", 12))
	lblInst.grid(row=0, column=3)
	srEntry.grid(row=1, column=2, columnspan=4)
	srEntry.focus_set()
	srLabel.grid(row=1, column=1)

	countryEntry.grid(row=2, column=2, sticky=tk.W)
	countryLabel.grid(row=2, column=1)

	accountEntry.grid(row=3, column=2, sticky=tk.W)
	accountLabel.grid(row=3, column=1)

	sendButton.grid(row=2,column=3)
	quitButton.grid(row=4,column=3)
	optionsButton.grid(row=3,column=3)

#this function is used when user clicks on "Send"
def Write():  
	NiceNow = getDate() #gets the date
	lblInst = tk.Label(master, text="Shift Report Logged, on %s." % NiceNow, background='#f2f2f2', font=("Helvetica", 12))
	typedSR = srEntry.get()
	typedCountry = countryEntry.get() #assigns whatever the user wrote to typedCountry
	typedAccount = accountEntry.get() #assigns whatever the user wrote to typedAccount
	if not typedSR: #if empty
		laying_content(team) #recreate GUI
		label_noSR.grid(row=5, column=3)
		return
	if not typedCountry and not typedAccount: #if both are empty
		laying_content(team) #recreate GUI
		label_noCountry.grid(row=5, column=3)
		return
		
	try:
				with open(srLocation, 'a', encoding="utf8",  errors='ignore') as file: #note that srLocation is the one we got in select_team()
						file.write("New Shift Report \nLogged by: " + str(Login) + "\nDate Logged: " + str(NiceNow) + "\nCountry: " + typedCountry.capitalize() + "\nAccount Number: " + typedAccount + "\nReport: " + typedSR + "\n" + lines + "\n")
	except FileNotFoundError:
		laying_content(team)
		label_noAccess.grid(row=5, column=3)
		return
			
	clear_text()

	lblInst.grid(row=5, column=3)
	
#this function counts the number of reports logged by the user running the file
def Count():
	clear_buttons() 
	more_options() #just recreates the GUI
	count = 0
	try:
		with open(srLocation, 'r', encoding="utf8",  errors='ignore') as f:
			for line in f.readlines(): #takes every single line in the file
				words = line.lower().split() #takes every single word in the file
				for word in words: 
					if word == Login: #checks if each word is the same as the user's login
						count += 1 #if so, add one to "count"
		lblInst = tk.Label(master, text="Number of reports you have submitted this quarter: %s" % count, background='#f2f2f2', font=("Helvetica", 12))
		lblInst.grid(row=8, column=2)
	except FileNotFoundError:
		layout_content(team)
		label_noAccess.grid(row=6, column=2)
		return
		
			

#this function opens the text file
def OpenFile():
	clear_buttons()
	more_options()
	label_opened = tk.Label(master, text="The Shift Reports file has opened successfully.", background='#f2f2f2', font=("Helvetica", 11))
	try:
		startfile(srLocation)
		label_opened.grid(row=6, column=2)
		return
		
	except FileNotFoundError:
		clear_buttons()
		more_options()
		label_noAccess.grid(row=6, column=2)
		return
			


#this function creates the sub-GUI when user clicks on More Options
def more_options():
	clear_buttons()
	homeButton.grid(row=1,column=2)
	countButton.grid(row=2,column=2)
	openButton.grid(row=3,column=2)
	exportButton.grid(row=4,column=2)
	quitButton.grid(row=5,column=2)


#this function exports the shift reports into a CSV
def export():
	rep_counts = {rep: 0 for rep in reps}
	label_nop = tk.Label(master, text="The widget does not have permissions to the CSV file.\nPlease make sure you close the Results.CSV file before trying to export the results again.", background='#f2f2f2', font=("Helvetica", 11))
	label_ok = tk.Label(master, text="Results.csv has been exported successfully.", background='#f2f2f2', font=("Helvetica", 11))
	now = datetime.now().strftime("%Y-%m-%d")
	resultsFile = "Results " + str(now) +".csv"
	while True:
		try:
			more_options()
			clear_text()
			with open(srLocation, 'r', encoding="utf8",  errors='ignore') as f:
				for line in f.readlines():
					for rep in rep_counts:
						if rep in line.lower():
							rep_counts[rep] += 1

			with open(resultsFile,"w",newline='', encoding="utf8",  errors='ignore') as m:
				for key in rep_counts.keys():
					m.write("%s,%s\n" % (key, rep_counts[key]))

			f.close()
			m.close()
			startfile(resultsFile)
			label_ok.grid(row=6, column=2)
			return

		except (FileNotFoundError):
			more_options()
			clear_text()
			label_noAccess.grid(row=6, column=2)
			return
		
		except PermissionError:
			more_options()
			clear_text()
			label_nop.grid(row=6, column=2)
			return



#secondary buttons setup
sendButton = tk.Button(master, text = "Send", bg="lightyellow", command = Write)
openButton = tk.Button(master, text = "Open Shift Reports File", bg="lightyellow", command = OpenFile)
countButton = tk.Button(master, text = "Count Your Reports", bg="lightyellow", command = Count)
quitButton = tk.Button(master, text="Quit", bg="pink", command=master.quit)
optionsButton = tk.Button(master, text="More Options", command=more_options)
homeButton = tk.Button(master, text="Go Back",command=lambda: laying_content(team))
exportButton = tk.Button(master, text="Export Shift Reports", bg="lightyellow", command=export)

def main_function():
	with open (repsLocation, 'rt') as repsFile:
		reps = repsFile.read().split(',')
	laying_content(team)
    
	




first_screen()
tk.mainloop()

