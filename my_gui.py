import tkinter as tk
from tkinter import filedialog

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1000x500")
        self.root.title("CSV Loader")

        self.label = tk.Label(self.root, text="Upload a CSV file", font = ("Aerial", 16))
        self.upload_button = tk.Button(self.root, text="Upload CSV", font = ('Aerial', 12), command=self.uploadDialouge)
        self.load_button = tk.Button(self.root,text = "Load CSV", font = ('Arial', 12))

        self.label.grid(row=0, column=0)
        self.upload_button.grid(row=1,column=6)
        self.load_button.grid(row=1,column=7)

        self.root.mainloop()
        
    def uploadDialouge(self):

        
        self.root.filename = filedialog.askopenfilename(initialdir="/python/",title="Select a file", filetypes=(("csv files","*.csv"),("all files","*.*")))
        self.file_name = tk.Label(self.root, text = self.root.filename)
        self.file_name.grid(row=1, column=5)

MyGUI()
