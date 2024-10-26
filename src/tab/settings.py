import tkinter
from tkinter import ttk
from tkinter import colorchooser, messagebox

class SettingsWindow:
    """Window for selecting and applying color settings"""

    def __init__(self, master, color_config, apply_callback):
        self.color_config = color_config
        self.apply_callback = apply_callback

        # Settings window
        self.window = tkinter.Toplevel(master)
        self.window.title("Settings")
        
        # Color changes
        primary_color_button = ttk.Button(self.window, text="Set Primary Color", command=self.set_primary_color)
        primary_color_button.pack(pady=5)
        secondary_color_button = ttk.Button(self.window, text="Set Secondary Color", command=self.set_secondary_color)
        secondary_color_button.pack(pady=5)
        apply_button = ttk.Button(self.window, text="Apply Changes", command=self.apply_changes)
        apply_button.pack(pady=10)
        revert_button = ttk.Button(self.window, text="Revert to Default Colors", command=self.revert_to_defaults)
        revert_button.pack(pady=5)

    def set_primary_color(self):
        color = colorchooser.askcolor(title="Choose Primary Color")
        if color[1]: 
            self.color_config.primary_color = color[1]

    def set_secondary_color(self):
        color = colorchooser.askcolor(title="Choose Secondary Color")
        if color[1]:
            self.color_config.secondary_color = color[1]

    def apply_changes(self):
        self.color_config.save_config()
        messagebox.showinfo("Restart Required", "Colors updated. Restart to apply changes.")
        self.window.destroy()

    def revert_to_defaults(self):
        self.color_config.revert_to_defaults()
        messagebox.showinfo("Defaults Restored", "Default colors restored. Restart to apply changes.")
