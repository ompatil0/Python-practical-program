# ⏱ Smart Countdown Dashboard

A modern **Dashboard-Style Countdown Timer Application** built using **Python and Tkinter**.

This project provides a professional GUI interface with real-time countdown functionality, theme switching, timer history tracking, and sound alerts.

---

## 🚀 Features

- ⏳ Custom time input (Hours, Minutes, Seconds)
- ▶ Start, ⏸ Pause, 🔄 Reset functionality
- 🔔 Sound alert when timer completes
- 🕒 Live date and time display
- 📜 Scrollable timer history section
- 🌞 Light Mode / 🌙 Dark Mode toggle
- 🖥 Professional dashboard-style layout
- ⚡ Smooth performance using threading

---

## 🛠 Technologies Used

- Python 3
- Tkinter (GUI)
- Threading Module
- Datetime Module
- Winsound (Alarm Sound)

---

## 🧠 How It Works

1. The user enters time in hours, minutes, and seconds.
2. The application converts the input into total seconds.
3. A background thread starts decrementing the time every second.
4. The display updates in real-time in HH:MM:SS format.
5. When the timer reaches zero:
   - A sound alert is played.
   - A popup message is shown.
   - The completed timer is added to the history section.

---

## 🎛 Theme Settings

The application includes a Settings panel where users can switch between:

- 🌞 Light Mode
- 🌙 Dark Mode

The theme updates dynamically across the dashboard.

---
