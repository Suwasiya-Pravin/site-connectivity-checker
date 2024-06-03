from tkinter.font import BOLD
import tkinter.messagebox
from tkinter import *
import tkinter as tk
import urllib.request

# Initialize the main window
root = tk.Tk()
url = tk.StringVar()
root.title("Site Connectivity Checker by #Pravin Suwasiya")
root.geometry("1000x500")
root.config(bg="#dbd9d9")

# Function to clear the URL entry
def onDelete():
    url.set('')

# Function to check the site's availability
def onClick():
    if url.get() == "":
        tk.messagebox.showwarning("WARNING", "PLEASE ENTER URL...")
    else:
        try:
            saveUrl = url.get()
            # Ensure the URL starts with http:// or https://
            if not (saveUrl.startswith('http://') or saveUrl.startswith('https://')):
                saveUrl = 'http://' + saveUrl
            status = urllib.request.urlopen(saveUrl).getcode()
            if status == 200:
                tk.messagebox.showinfo("Warning", "THIS SITE IS AVAILABLE")
            else:
                tk.messagebox.showinfo("Warning", "THIS SITE IS NOT AVAILABLE RIGHT NOW")
        except Exception as e:
            tk.messagebox.showwarning("Warning", f"OOPS...SITE IS NOT AVAILABLE RIGHT NOW\n{e}")

# GUI elements
label_1 = Label(root, text="SITE CONNECTIVITY CHECKER", bg="#dbdbdb", fg="#d80202", font=("Helvetica", 30))
label_1.place(x=80, y=20)
label_2 = Label(root, text="ENTER URL OF WEBSITE :", bg="#dbdbdb", fg="#d80202", font=("Roboto", 10), bd=0)
label_2.place(x=20, y=100)
entry_1 = Entry(root, textvariable=url, width=45, bg="white", fg="black", font=("comic sans ms", "16"))
entry_1.place(x=210, y=100)
button_check = Button(root, text="Check URL", bg="#4dff4d", fg="black", command=onClick, font=("comic sans ms", "16"))
button_check.place(x=430, y=162)
button_delete_entry = Button(root, text="Delete Entry", command=onDelete, font=("comic sans ms", "16"), bg="#ff6666")
button_delete_entry.place(x=430, y=242)

# Start the Tkinter event loop
root.mainloop()
