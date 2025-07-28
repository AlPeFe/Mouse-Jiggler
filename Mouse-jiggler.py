mport tkinter as tk
from pynput.mouse import Controller
import threading
import time

# Mouse controller
mouse = Controller()

# Global control variables
running = False
interval = 5  # default interval in seconds

# Jiggler thread function
def jiggle():
    while running:
        current_pos = mouse.position
        mouse.move(1, 0)  # move slightly to the right
        time.sleep(0.1)
        mouse.position = current_pos  # move back
        time.sleep(interval)

# Start/Stop toggle
def toggle():
    global running
    if not running:
        try:
            int(entry.get())
            interval_slider.config(state='disabled')
        except ValueError:
            status_label.config(text="Invalid interval", fg="red")
            return
        running = True
        status_label.config(text="Running", fg="green")
        threading.Thread(target=jiggle, daemon=True).start()
        toggle_btn.config(text="Stop")
    else:
        running = False
        status_label.config(text="Stopped", fg="black")
        toggle_btn.config(text="Start")
        interval_slider.config(state='normal')

# Update interval from slider
def update_interval(val):
    global interval
    interval = int(float(val))
    entry.delete(0, tk.END)
    entry.insert(0, str(interval))

# GUI setup
root = tk.Tk()
root.title("Linux Mouse Jiggler")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

tk.Label(frame, text="Interval (seconds):").pack()
entry = tk.Entry(frame, width=5)
entry.insert(0, str(interval))
entry.pack()

interval_slider = tk.Scale(frame, from_=1, to=300, orient="horizontal", command=update_interval)
interval_slider.set(interval)
interval_slider.pack()

toggle_btn = tk.Button(frame, text="Start", width=10, command=toggle)
toggle_btn.pack(pady=5)

status_label = tk.Label(frame, text="Stopped", fg="black")
status_label.pack()

root.mainloop()
