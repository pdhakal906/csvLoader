import tkinter as tk
from tkinter import filedialog
import tkinter.ttk as ttk
import csv

class MyGui():
    def __init__(self):
        def loadCsv():
            self.load_button.pack_forget()
            self.label.pack_forget()
            self.file_name.pack_forget()
            self.csv_file = open(self.file) 

            self.csvreader = csv.reader(self.csv_file)
            self.columns = []
            self.columns = next(self.csvreader) # column headers
            self.row_set = [row for row in self.csvreader] # list of rows of data
            self.tree_view = ttk.Treeview(self.root)
            self.tree_view["columns"] = self.columns
            self.tree_view.column("#0", width=0, minwidth=0) #remove the phanton column that is the first column

            for i in self.columns:
                self.tree_view.column(i, width=150, anchor="c")
                self.tree_view.heading(i, text = i)

            for dt in self.row_set:
                value = [r for r in dt]
                self.tree_view.insert("", "end", iid=value[0], values=value)

            self.tree_view.pack()

        self.root = tk.Tk()
        self.root.geometry("1500x750")
        self.root.title("CSV Loader")
        
        self.label = tk.Label(self.root, text="Upload a CSV file", font = ("Aerial", 16))
        self.load_button = tk.Button(self.root,text = "Load CSV", font = ('Arial', 12), command=loadCsv)
        self.label.pack()
        self.load_button.pack()

        self.filename = filedialog.askopenfilename(initialdir="/python/",title="Select a file", filetypes=(("csv files","*.csv"),("all files","*.*")))
        self.file_name = tk.Label(self.root, text = self.filename)
        self.file_name.pack()

        self.file = self.file_name.cget("text")
        
        self.root.mainloop()


MyGui()
