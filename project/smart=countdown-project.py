import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
from datetime import datetime
import winsound

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Smart Countdown Dashboard")
root.geometry("1000x600")
root.resizable(False, False)

# ---------------- Variables ----------------
running = False
paused = False
total_seconds = 0
current_theme = "light"

# ---------------- Sidebar ----------------
sidebar = tk.Frame(root, bg="#1f4fa3", width=200)
sidebar.pack(side="left", fill="y")

tk.Label(sidebar, text="⏱ COUNTDOWN TIMER", bg="#1f4fa3", fg="white",
         font=("Arial", 18, "bold")).pack(pady=20)

# ---------------- Main Area ----------------
main_frame = tk.Frame(root, bg="white")
main_frame.pack(side="right", fill="both", expand=True)

# ---------------- Header ----------------
header = tk.Frame(main_frame, bg="white")
header.pack(fill="x")

title = tk.Label(header, text="Smart Countdown Dashboard",
                 font=("Arial", 20, "bold"), bg="white")
title.pack(side="left", padx=20, pady=10)

clock_label = tk.Label(header, font=("Arial", 12), bg="white")
clock_label.pack(side="right", padx=20)

def update_clock():
    now = datetime.now().strftime("%d-%m-%Y  %H:%M:%S")
    clock_label.config(text=now)
    root.after(1000, update_clock)

update_clock()

# ---------------- Timer Display ----------------
timer_display = tk.Label(main_frame, text="00:00:00",
                         font=("Arial", 48, "bold"),
                         fg="#1f4fa3", bg="white")
timer_display.pack(pady=20)

status_label = tk.Label(main_frame, text="Status: Waiting",
                        font=("Arial", 12), bg="white")
status_label.pack()

# ---------------- Input Section ----------------
input_frame = tk.Frame(main_frame, bg="white")
input_frame.pack(pady=15)

hour_entry = ttk.Entry(input_frame, width=5)
hour_entry.grid(row=0, column=0, padx=5)

min_entry = ttk.Entry(input_frame, width=5)
min_entry.grid(row=0, column=1, padx=5)

sec_entry = ttk.Entry(input_frame, width=5)
sec_entry.grid(row=0, column=2, padx=5)

# ---------------- Buttons ----------------
btn_frame = tk.Frame(main_frame, bg="white")
btn_frame.pack(pady=10)

# ---------------- History Section ----------------
history_label = tk.Label(main_frame, text="Timer History",
                         font=("Arial", 14, "bold"), bg="white")
history_label.pack(pady=(25, 5))

history_frame = tk.Frame(main_frame, bg="white")
history_frame.pack(padx=50)

history_box = tk.Listbox(history_frame, height=6, width=80)
history_box.pack(side="left")

scrollbar = tk.Scrollbar(history_frame)
scrollbar.pack(side="right", fill="y")

history_box.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=history_box.yview)

# ---------------- Theme Function ----------------
def apply_theme(mode):
    global current_theme
    current_theme = mode

    if mode == "dark":
        main_frame.config(bg="#2b2b2b")
        header.config(bg="#2b2b2b")
        title.config(bg="#2b2b2b", fg="white")
        clock_label.config(bg="#2b2b2b", fg="white")
        timer_display.config(bg="#2b2b2b", fg="#4da6ff")
        status_label.config(bg="#2b2b2b", fg="white")
        history_label.config(bg="#2b2b2b", fg="white")
        history_frame.config(bg="#2b2b2b")
        btn_frame.config(bg="#2b2b2b")
        input_frame.config(bg="#2b2b2b")
    else:
        main_frame.config(bg="white")
        header.config(bg="white")
        title.config(bg="white", fg="black")
        clock_label.config(bg="white", fg="black")
        timer_display.config(bg="white", fg="#1f4fa3")
        status_label.config(bg="white", fg="black")
        history_label.config(bg="white", fg="black")
        history_frame.config(bg="white")
        btn_frame.config(bg="white")
        input_frame.config(bg="white")

# ---------------- Settings Window ----------------
def open_settings():
    settings_window = tk.Toplevel(root)
    settings_window.title("Theme Settings")
    settings_window.geometry("300x200")
    settings_window.resizable(False, False)

    tk.Label(settings_window, text="Select Theme",
             font=("Arial", 14, "bold")).pack(pady=20)

    tk.Button(settings_window, text="🌞 Light Mode",
              width=20,
              command=lambda: apply_theme("light")
              ).pack(pady=10)

    tk.Button(settings_window, text="🌙 Dark Mode",
              width=20,
              command=lambda: apply_theme("dark")
              ).pack(pady=10)

# ---------------- Countdown Logic ----------------
def start_timer():
    global running, paused, total_seconds

    if running:
        return

    try:
        hours = int(hour_entry.get() or 0)
        minutes = int(min_entry.get() or 0)
        seconds = int(sec_entry.get() or 0)

        total_seconds = hours * 3600 + minutes * 60 + seconds

        if total_seconds <= 0:
            messagebox.showwarning("Invalid", "Enter valid time!")
            return

        running = True
        paused = False
        status_label.config(text="Status: Running")

        threading.Thread(target=countdown).start()

    except ValueError:
        messagebox.showerror("Error", "Enter numeric values only!")

def countdown():
    global running, paused, total_seconds

    original_time = total_seconds

    while total_seconds > 0 and running:
        if not paused:
            mins, secs = divmod(total_seconds, 60)
            hrs, mins = divmod(mins, 60)

            timer_display.config(text=f"{hrs:02d}:{mins:02d}:{secs:02d}")
            time.sleep(1)
            total_seconds -= 1
        else:
            time.sleep(0.1)

    if total_seconds == 0 and running:
        timer_display.config(text="00:00:00")
        status_label.config(text="Status: Time's Up!")
        winsound.Beep(1000, 1000)
        messagebox.showinfo("Finished", "Countdown Completed!")

        finish_time = datetime.now().strftime("%H:%M:%S")
        duration = datetime.utcfromtimestamp(original_time).strftime("%H:%M:%S")

        history_box.insert(tk.END,
                           f"Duration: {duration}  |  Completed at {finish_time}")

        running = False

def pause_timer():
    global paused
    if running:
        paused = not paused
        status_label.config(text="Status: Paused" if paused else "Status: Running")

def reset_timer():
    global running, paused, total_seconds
    running = False
    paused = False
    total_seconds = 0
    timer_display.config(text="00:00:00")
    status_label.config(text="Status: Reset")

# ---------------- Buttons ----------------
ttk.Button(btn_frame, text="Start", command=start_timer).grid(row=0, column=0, padx=10)
ttk.Button(btn_frame, text="Pause", command=pause_timer).grid(row=0, column=1, padx=10)
ttk.Button(btn_frame, text="Reset", command=reset_timer).grid(row=0, column=2, padx=10)

# Sidebar Buttons (After Functions Defined)
tk.Button(sidebar, text="Settings", bg="#1f4fa3", fg="white",
          bd=0, font=("Arial", 12),
          command=open_settings).pack(fill="x", pady=5)

tk.Button(sidebar, text="Exit", bg="#1f4fa3", fg="white",
          bd=0, font=("Arial", 12),
          command=root.quit).pack(fill="x", pady=5)

root.mainloop()