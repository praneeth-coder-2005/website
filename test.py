import tkinter as tk
from tkinter import messagebox
import pyautogui as pag
import webbrowser
import time

# Function to start the login process
def start_login():
    phone_number = phone_entry.get()
    if not phone_number.isdigit() or len(phone_number) != 10:
        messagebox.showerror("Error", "Enter a valid 10-digit phone number")
        return

    # Open Hotstar login page
    webbrowser.open("https://www.hotstar.com/in")
    time.sleep(5)

    # Automate login process
    pag.click(200, 200)  # Click "Login" button (adjust coordinates)
    time.sleep(2)
    pag.typewrite(phone_number)
    pag.press("enter")

    messagebox.showinfo("Info", "OTP sent. Enter it in the next step.")

# Function to submit OTP
def submit_otp():
    otp = otp_entry.get()
    if not otp.isdigit() or len(otp) != 6:
        messagebox.showerror("Error", "Enter a valid 6-digit OTP")
        return

    # Automate OTP entry
    time.sleep(2)
    pag.typewrite(otp)
    pag.press("enter")

    messagebox.showinfo("Success", "Logged in successfully!")

# GUI
app = tk.Tk()
app.title("Custom Hotstar Login Tool")
app.geometry("300x200")

tk.Label(app, text="Phone Number:").pack(pady=5)
phone_entry = tk.Entry(app)
phone_entry.pack(pady=5)

tk.Button(app, text="Start Login", command=start_login).pack(pady=10)

tk.Label(app, text="Enter OTP:").pack(pady=5)
otp_entry = tk.Entry(app)
otp_entry.pack(pady=5)

tk.Button(app, text="Submit OTP", command=submit_otp).pack(pady=10)

app.mainloop()
