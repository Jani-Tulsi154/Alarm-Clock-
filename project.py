import tkinter as tk
from tkinter import messagebox
import datetime
import winsound

# -----------------------------
# Update Clock
# -----------------------------
def update_clock():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    clock_label.config(text=current_time)

    # Check alarm
    if alarm_time.get() == current_time:
        ring_alarm()

    root.after(1000, update_clock)

# -----------------------------
# Ring Alarm
# -----------------------------
def ring_alarm():
    messagebox.showinfo("Alarm", "⏰ Time's Up!")

    # Beep 10 times
    for i in range(10):
        winsound.Beep(1000, 500)

    alarm_time.set("")  # Reset alarm

# -----------------------------
# Set Alarm
# -----------------------------
def set_alarm():
    try:
        datetime.datetime.strptime(alarm_entry.get(), "%H:%M:%S")
        alarm_time.set(alarm_entry.get())
        status_label.config(text=f"Alarm set for {alarm_entry.get()}", fg="green")
    except ValueError:
        messagebox.showerror("Error", "Enter time in HH:MM:SS format")

# -----------------------------
# GUI
# -----------------------------
root = tk.Tk()
root.title("Python Alarm Clock")
root.geometry("400x250")
root.resizable(False, False)

alarm_time = tk.StringVar()

title = tk.Label(root, text="Alarm Clock", font=("Arial", 20, "bold"))
title.pack(pady=10) #pack() places the widget inside the window.adds 10 pixels vertical space above and below the label.     

clock_label = tk.Label(root, font=("Arial", 30), fg="blue")
clock_label.pack()

tk.Label(root, text="Set Alarm (HH:MM:SS)", font=("Arial", 12)).pack(pady=10)

alarm_entry = tk.Entry(root, font=("Arial", 14), justify="center")
alarm_entry.pack()

set_button = tk.Button(
    root,
    text="Set Alarm",
    font=("Arial", 12),
    bg="green",
    fg="white",
    command=set_alarm
)
set_button.pack(pady=10)

status_label = tk.Label(root, text="", font=("Arial", 10))
status_label.pack()

update_clock()

root.mainloop()