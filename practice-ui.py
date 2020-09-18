from tkinter import *
from tkinter.filedialog import askopenfilename
from pathlib import Path
from zipfile import ZipFile
import shutil
import os
import csv

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
        csvfile=Label(root, text="File").grid(row=1, column=0)
        bar=Entry(master).grid(row=1, column=1) 

        #Buttons  
        self.cbutton= Button(root, text="Copy", command=self.copyTestFile)
        self.cbutton.grid(row=30, column=3, sticky = W + E)
        self.cbutton= Button(root, text="Run", command=self.unzip)
        self.cbutton.grid(row=20, column=3, sticky = W + E)
        self.cbutton= Button(root, text="OK", command=self.process_csv)
        self.cbutton.grid(row=10, column=3, sticky = W + E)
        self.bbutton= Button(root, text="Browse", command=self.browsecsv)
        self.bbutton.grid(row=1, column=3)

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
            print(self.directory, student)
            student_folder = student[0:student.find("_")] # \studentname
            shutil.copy(self.fullpath, self.sectionFolder + student_folder + "\\" + self.filename) # C:\Users\tyler\Downloads\students\studentname\recursion_tester.py

            try:
                os.system("python " + self.sectionFolder + student_folder + "\\" + self.filename)
                cur = os.getcwd() + "\\log_file.txt"
                shutil.move(cur, self.sectionFolder + student_folder)
            except:
                os.remove(cur)
                arr.append(student_folder)
        
        print("Students that failed a test: ", arr)

    def process_csv(self):
        pass
        

root = Tk()
root.title("Auto-Grader")
root.geometry('800x600')
window=Window(root)
root.mainloop() 