import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk


class DatasetGenerationGUI:
    def __init__(self, controller):
        """
        Initialize the GUI for dataset generation.
        """
        self.controller = controller

        # Create the main window
        self.root = tk.Tk()
        self.root.title("Dataset Generation")

        # Create a frame for buttons
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10)

        # Start button
        self.start_button = ttk.Button(
            button_frame, text="Start Generation", command=self.start_generation
        )
        self.start_button.grid(row=0, column=0, padx=10)

        # Stop button (optional, disabled for now)
        self.stop_button = ttk.Button(
            button_frame,
            text="Stop Generation",
            state="disabled",
            command=self.stop_generation,
        )
        self.stop_button.grid(row=0, column=1, padx=10)

        # Create a log window (scrolled text area) for output and activity log
        self.log_area = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, width=80, height=20, state="disabled"
        )
        self.log_area.pack(pady=10)

    def start_generation(self):
        """
        Handle Start Generation button press.
        """
        self.start_button.config(state="disabled")
        self.controller.start_generation()

    def stop_generation(self):
        """
        Handle Stop Generation button press.
        """
        # This feature can be implemented if stopping is required
        self.stop_button.config(state="disabled")
        self.controller.stop_generation()

    def update_log(self, message):
        """
        Update the log area with new messages.
        """
        self.log_area.config(state="normal")  # Enable editing
        self.log_area.insert(tk.END, message + "\n")  # Add new message
        self.log_area.see(tk.END)  # Scroll to the bottom
        self.log_area.config(state="disabled")  # Disable editing

    def run(self):
        """
        Start the Tkinter main loop.
        """
        self.root.mainloop()
