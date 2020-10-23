from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter.font as tkFont
from pathlib import Path
from zipfile import ZipFile
from PIL import Image, ImageTk
import shutil
import os
import csv
import sys

# Step 1: Browse input zip
# Step 2: Click run to unzip student and class zip file
# Step 3: Click copy and select test file then all the student's files will be tested
# Extras: Only goes to the log file does not make spreadsheet

class Window:       
    def __init__(self, master):     
        self.filename=""
        self.directory=""
        self.fullpath=""
        self.nofilesuffix=""
        self.section = None
        self.sectionFolder = ""
        
        # import image to window
        load = Image.open("Canvas-Grader.gif")
        render = ImageTk.PhotoImage(load)
        img = Label(root, image=render)
        img.image = render
        img.place(x=0, y=0)

        fontStyle = tkFont.Font(family="Arial", size=10)

        # first prompt
        lbl1 = Label(root, text="1. Select Class Zip: ", font=fontStyle, fg = 'grey')
        lbl1.place(x=90, y=145, anchor=CENTER)
        lbl1.config(bg="white")
        self.bbutton= Button(root, text="Browse", command=self.browsecsv, width="6", bg="#E63D2F", fg='white', font=fontStyle)
        self.bbutton.place(x=180, y=145, anchor=CENTER)

        # second prompt
        lbl2 = Label(root, text="2. Select Test File: ", font=fontStyle, fg = 'grey')
        lbl2.place(x=88.7, y=175, anchor=CENTER)
        lbl2.config(bg="white")
        self.cbutton= Button(root, text="Copy", command=self.copyTestFile, width="6", bg="#E63D2F", fg='white', font=fontStyle)
        self.cbutton.place(x=180, y=175, anchor=CENTER)
        

    def browsecsv(self):

        Tk().withdraw() 
        self.fullpath = askopenfilename() # C:\Users\tyler\Downloads\(zipname).zip
        path = Path(self.fullpath).parts

        for i in range(len(path)-1): # C:\Users\tyler\Downloads\
            if path[i].find("\\") == -1:
                self.directory += (path[i] + "\\")
            else:
                self.directory += (path[i])

        self.filename = path[len(path)-1] # (zipname).zip
        self.nofilesuffix = self.filename[0:self.filename.find(".")] # zipname
        print(self.fullpath, self.filename, self.directory)
        self.unzip()

    def unzip(self):
        with ZipFile(self.fullpath, 'r') as zip_ref:
            zip_ref.extractall(self.directory+self.nofilesuffix)
        self.directory += (self.nofilesuffix + "\\") # C:\Users\tyler\Downloads\(zipname)\
        self.section = os.listdir(self.directory)

        for student in self.section: # loops through all (student).zip
            studentnfs = student[0:student.find("_")] # (student)
            with ZipFile(self.directory + "\\" + student, 'r') as zip_ref:
                zip_ref.extractall(self.directory + "\\" + studentnfs)
            os.remove(self.directory + "\\" + student)
        
        self.sectionFolder = self.directory
    
    def copyTestFile(self):
        arr = []
        Tk().withdraw() 
        self.fullpath = askopenfilename() # C:\Users\tyler\Downloads\testfile.py
        path = Path(self.fullpath).parts
        self.directory = ''
        for i in range(len(path)-1): # C:\Users\tyler\Downloads\
            if path[i].find("\\") == -1:
                self.directory += (path[i] + "\\")
            else:
                self.directory += (path[i])

        self.filename = path[len(path)-1] # testfile.py
        for student in self.section:
            print(student[:student.find("_")])
            student_folder = student[0:student.find("_")] # \studentname
            shutil.copy(self.fullpath, self.sectionFolder + student_folder + "\\" + self.filename) # C:\Users\tyler\Downloads\students\studentname\recursion_tester.py

            try:
                os.system("python " + self.sectionFolder + student_folder + "\\" + self.filename)
                cur = os.getcwd() + "\\log_file.txt"
                shutil.move(cur, self.sectionFolder + student_folder)
            except:
                os.remove(cur)
                arr.append(student_folder)
        
        print("Students that need to be checked: ", arr)

        sys.exit(0)
        

root = Tk()
root.title("Canvas-Grader")
root.geometry('250x200')
root.configure(bg='white')
window=Window(root)
root.mainloop() 