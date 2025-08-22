from .notificationMethod import notificationMethod
import tkinter as tk
from tkinter import messagebox

class alert(notificationMethod):
    
    def notify(self, message: str):
        root = tk.Tk()
        messagebox.showinfo("INFO", message)
        root.destroy()
        