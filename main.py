import tkinter as tk
from pymongo import MongoClient
from datetime import datetime
import os
import locale

# Imposta la locale in italiano
locale.setlocale(locale.LC_TIME, "it_IT.UTF-8")

# Connetti al database MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["turni_db"]
collection = db["utenti"]

# Crea una cartella per i file dei turni, se non esiste
if not os.path.exists("turni_files"):
    os.makedirs("turni_files")

def login():
    username = username_entry.get()
    password = password_entry.get()

    user_data = collection.find_one({"username": username, "password": password})

    if user_data:
        login_window.destroy()
        show_turno_window(username)
    else:
        status_label.config(text="Username o password errati")

def show_turno_window(username):
    turno_window = tk.Tk()
    turno_window.title(f"Benvenuto, {username}")
    turno_window.geometry("400x200")  # Imposta le dimensioni della finestra

    def inizio_turno():
        benvenuto_label.config(text=f"Ciao {username}")
        with open(f"turni_files/{username}_turni.txt", "a") as file:
            now = datetime.now()
            formatted_date = now.strftime("%d-%m-%Y - %A")
            formatted_start_time = now.strftime("%H:%M")
            file.write(f"{formatted_date} - Inizio turno: {formatted_start_time}")
        turno_button.config(text="Fine turno", command=fine_turno)

    def fine_turno():
        with open(f"turni_files/{username}_turni.txt", "a") as file:
            now = datetime.now()
            formatted_end_time = now.strftime("%H:%M")
            file.write(f" - Fine turno: {formatted_end_time}\n")
        turno_window.destroy()

    benvenuto_label = tk.Label(turno_window, text=f"Ciao {username}", font=("Helvetica", 16))
    benvenuto_label.pack()

    turno_button = tk.Button(turno_window, text="Inizio turno", command=inizio_turno)
    turno_button.pack()

    turno_window.mainloop()

# Creazione della finestra di login
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x150")  # Imposta le dimensioni della finestra

username_label = tk.Label(login_window, text="Username:")
username_label.pack()

username_entry = tk.Entry(login_window)
username_entry.pack()

password_label = tk.Label(login_window, text="Password:")
password_label.pack()

password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

login_button = tk.Button(login_window, text="Login", command=login)
login_button.pack()

status_label = tk.Label(login_window, text="")
status_label.pack()

login_window.mainloop()
