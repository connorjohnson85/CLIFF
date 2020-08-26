# sets up the html interface for the workstation
import tkinter as tki
import os
import shutil

def goToProject():
	listIndex = projectList.curselection()
	if listIndex != ():
		projectName = os.listdir("/home/connor/CLIFF/CLIFF/projects/")[listIndex[0]]
	else:
		print("You Must Select a Project!")

def createNewProject(name, root):
	os.makedirs("/home/connor/CLIFF/CLIFF/projects/" + name)
	root.destroy()

def createProject():
	createPrompt = tki.Tk()
	label = tki.Label(createPrompt, text = "Name of Project").grid(row = 0)
	input = tki.Entry(createPrompt)
	input.grid(row = 0, column = 1)
	exitButton = tki.Button(createPrompt, text = "Cancel", command = createPrompt.destroy).grid(column = 1, sticky = "w")
	confirm = tki.Button(createPrompt, text = "Confirm", command = lambda: createNewProject(input.get(), createPrompt)).grid(row=1, column = 0, sticky = "e")
	createPrompt.mainloop()

def deleteSelectedProject(root, projectName):
	shutil.rmtree("/home/connor/CLIFF/CLIFF/projects/{}".format(projectName))

def deleteProject(selectedProject):
	deletePrompt = tki.Tk()
	projectName = os.listdir("/home/connor/CLIFF/CLIFF/projects/")[selectedProject[0]]
	label = tki.Label(deletePrompt, text = "Are you sure you want to delete project {}".format(projectName)).grid(row = 0)
	confirm = tki.Button(deletePrompt, text = "Confirm", command = lambda: deleteSelectedProject(deletePrompt, projectName)).grid(row=1, sticky ="e")
	cancel = tki.Button(deletePrompt, text = "Cancel", command = lambda: deletePrompt.destroy()).grid(row=1, column = 2, sticky = "w")
	deletePrompt.mainloop()


top = tki.Tk()
top.title("Work Station")
projectList = tki.Listbox(top)
lbl = tki.Label(top, text = "Projects currently in development")
button = tki.Button(top, text = "Go to current Project", command = goToProject)
button2 = tki.Button(top, text = "Create New Project", command = createProject)
button3 = tki.Button(top, text = "Delete Project", command = lambda: deleteProject(projectList.curselection()))
count = 0
for item in os.listdir("/home/connor/CLIFF/CLIFF/projects/"):
	count += 1
	projectList.insert(count, item.capitalize())
lbl.grid(row=0, sticky = "w")
projectList.grid(row=1, sticky="w")
button.grid(row=2, sticky = "w")
button2.grid(row=3, sticky = "w")
button3.grid(row=4, sticky = "w")
top.mainloop()

