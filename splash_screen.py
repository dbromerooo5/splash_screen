import tkinter as tk

# Creates the main window & sets the title.
splash_window = tk.Tk()
splash_window.title("Splash Screen")

# Sets the window's width & height.
splash_width = 400
splash_height = 230

# Gets the dimensions of the screen.
screen_width = splash_window.winfo_screenwidth()
screen_height = splash_window.winfo_screenheight()

# Calculates the x & y coordinates needed to center the window on the screen.
x = (screen_width // 2) - (splash_width // 2)
y = (screen_height // 2) - (splash_height // 2)

# Places the window in the center of the screen.
splash_window.geometry(f"{splash_width}x{splash_height}+{x}+{y}")

# Creates a label to hold the game studio text.
GAME_STUDIO = "Your Game Studio"
game_studio_label = tk.Label(splash_window, text=GAME_STUDIO, font=("Helvetica", 16))

# Displays the game studio text in the center of the window.
game_studio_label.pack(expand=True, fill=tk.BOTH)

# Waits until the splash screen has finished playing, then closes the splash screen.
splash_duration = 2250  # Time in milliseconds (2.25 seconds).
splash_window.after(splash_duration, splash_window.destroy)

# Starts the main loop.
splash_window.mainloop()