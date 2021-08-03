from tkinter import *

import sys

import os

import time

root = Tk()

root.geometry("900x600")

root.title("Linux Py Finder")

root.resizable(False, False)

root['bg'] =  "#808a8a"

FOUND = False

STARTING_DIR = "/home"

def search_linux(f, directory, r):
	global FOUND
	
	for i in os.listdir():

		if os.path.isdir(directory + "/" + i):

			try:
				os.chdir(directory + "/" + i)

				search_linux(f, directory + "/" + i, r)

				os.chdir("..")
			except:
				continue

		elif i.__contains__(f):
			r.append(f"File was located in {directory}")
			FOUND = True
			return
		elif i.lower().__contains__(f.lower()):
			r.append(f"File was located in {directory}")
			FOUND = True
			return
		elif i.upper().__contains__(f.upper()):
			r.append(f"File was located in {directory}")
			FOUND = True
			return
	os.chdir("..")
	return








def search(event = None):
	global file_entry, FOUND, Results_Label

	global root, STARTING_DIR

	STARTING_DIR = "/home"

	os.chdir(STARTING_DIR)

	

	Results_Label.delete('1.0', END)

	file = file_entry.get()

	file_entry.delete(0, 'end')

	results = []

	if sys.platform == "linux":
		Start_Time = time.time()
		search_linux(file, STARTING_DIR, results)
		End_Time = time.time()

		

		if FOUND == False:
			print("We could not find that file")
		else:
			file_entry.insert(0, f"{len(results)} results Found in {round(End_Time - Start_Time, 3)} Secs")
			for i in results:
				Results_Label.insert("end", i + "\n")
	FOUND = False


def clear_entry(event = None):
	global file_entry
	file_entry.delete(0, END)
	return None 

#the following are widgets
file_entry = Entry(root, font = ("Consolas", 14), width = 30)

file_entry.bind("<Button-1>", clear_entry)

file_button = Button(root, text = "Search", command = search, width = 28, font = ("Consolas", 12))

root.bind("<Return>", search)

file_entry.place(x = 275, y = 300)

file_button.place(x = 285, y = 350)

scroll = Scrollbar(root)

scroll.pack(side = RIGHT, fill = Y)

Results_Label = Text(root, height = 10, width = 100, yscrollcommand = scroll.set, font = ("Consolas", 10))

Results_Label.place(x = 50, y = 0)

scroll.config(command = Results_Label.yview)



root.mainloop()
