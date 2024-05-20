import tkinter as tk
import pyautogui
import threading
import time  # Importing time module to use sleep function

class AutoTyperApp:
    def __init__(self, master):
        self.master = master
        master.title("AutoTyper Created by Ramishka")

        master.geometry("400x300")

        self.label = tk.Label(master, text="Enter your text here:")
        self.label.pack()

        self.text_area = tk.Text(master, height=10, width=50)
        self.text_area.pack()

        self.delay_label = tk.Label(master, text="Delay between characters (milliseconds):")
        self.delay_label.pack()

        self.delay_entry = tk.Entry(master)
        self.delay_entry.pack()

        self.start_button = tk.Button(master, text="Start Typing", command=self.start_typing)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop Typing", command=self.stop_typing, state=tk.DISABLED)
        self.stop_button.pack()

        self.typing = False

    def type_text(self):
        self.typing = True
        # Wait for 5 seconds before starting to type
        time.sleep(5)

        text = self.text_area.get("1.0", tk.END)
        try:
            delay_in_ms = float(self.delay_entry.get())
            delay_in_s = delay_in_ms / 1000.0  # Convert milliseconds to seconds
        except ValueError:
            delay_in_s = 0  # Default to no delay if input is invalid

        for char in text:
            if not self.typing:
                break
            pyautogui.typewrite(char)
            pyautogui.sleep(delay_in_s)  # Now it uses seconds, converted from milliseconds

        self.typing = False
        self.stop_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)

    def start_typing(self):
        self.stop_button.config(state=tk.NORMAL)
        self.start_button.config(state=tk.DISABLED)
        threading.Thread(target=self.type_text).start()

    def stop_typing(self):
        self.typing = False
        self.stop_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)

root = tk.Tk()
my_gui = AutoTyperApp(root)
root.mainloop()

