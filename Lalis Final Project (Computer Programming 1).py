# (pip install pytz) first before running

import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pytz

# GUI (Window)
root = tk.Tk()
root.title("Timezone Converter")
root.geometry("340x280")
root.resizable(False, False)

# Title label
tk.Label(root, text="Timezone Converter By Lalis", font=("Arial", 14)).pack(pady=10)

# Time input
tk.Label(root, text="Enter time (YYYY-MM-DD HH:MM):").pack()
time_input = tk.Entry(root, width=25)
time_input.pack(pady=5)

# Dropdowns (From and To)
all_zones = pytz.common_timezones

tk.Label(root, text="From Timezone:").pack()
from_timezone = ttk.Combobox(root, values=all_zones, width=30)
from_timezone.set("Asia/Manila")
from_timezone.pack()

tk.Label(root, text="To Timezone:").pack()
to_timezone = ttk.Combobox(root, values=all_zones, width=30)
to_timezone.set("Asia/Manila")
to_timezone.pack()

# Function
def convert_time():
    try:
        # Get user input
        time_str = time_input.get()
        from_zone = pytz.timezone(from_timezone.get())
        to_zone = pytz.timezone(to_timezone.get())

        # Convert String to Datetime
        input_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M")

        # Localize and Convert
        localized = from_zone.localize(input_time)
        converted = localized.astimezone(to_zone)

        result_label.config(
            text=f"Converted Time:\n{converted.strftime('%Y-%m-%d %H:%M')}"
        )
    except Exception as e:
        result_label.config(text="Invalid input! Use format: YYYY-MM-DD HH:MM")

# Convert Button
tk.Button(root, text="Convert", command=convert_time).pack(pady=10)

# Result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()