import tkinter as tk
from time import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

        # Display label
        self.label = tk.Label(root, text="00:00:000", font=("Arial", 40))
        self.label.pack(pady=20)

        # Buttons
        self.start_button = tk.Button(root, text="Start", command=self.start, width=10)
        self.start_button.pack(side="left", padx=10, pady=10)

        self.pause_button = tk.Button(root, text="Pause", command=self.pause, width=10)
        self.pause_button.pack(side="left", padx=10, pady=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset, width=10)
        self.reset_button.pack(side="left", padx=10, pady=10)

        # Update loop
        self.update_timer()

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time() - self.elapsed_time

    def pause(self):
        if self.running:
            self.running = False
            self.elapsed_time = time() - self.start_time

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.label.config(text="00:00:000")

    def update_timer(self):
        if self.running:
            self.elapsed_time = time() - self.start_time
            minutes = int(self.elapsed_time / 60)
            seconds = int(self.elapsed_time % 60)
            milliseconds = int((self.elapsed_time - int(self.elapsed_time)) * 1000)
            self.label.config(text=f"{minutes:02d}:{seconds:02d}:{milliseconds:03d}")
        self.root.after(10, self.update_timer)  # update every 10ms

# Create app window
root = tk.Tk()
app = Stopwatch(root)
root.mainloop()