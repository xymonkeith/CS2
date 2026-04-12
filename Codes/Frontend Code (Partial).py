import tkinter as tk
from PIL import Image, ImageTk

# Create main window
root = tk.Tk()
root.title("Puzzling Out Intelligence")
root.geometry("800x600")  # window size

# Load image first to get its size
image = Image.open("welcome.png")
photo = ImageTk.PhotoImage(image)
img_width, img_height = image.size

# Create a frame to hold canvas + scrollbar
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

# Create canvas with exact image width
canvas = tk.Canvas(frame, width=1366, height=2694)  # show 600px of height
canvas.pack(side="left", fill="both", expand=True)


# Vertical scrollbar
v_scroll = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
v_scroll.pack(side="right", fill="y")
canvas.configure(yscrollcommand=v_scroll.set)

# Put image on canvas
canvas.create_image(0, 0, anchor="nw", image=photo)
canvas.image = photo  # keep reference

# Make canvas scrollable for full image
canvas.config(scrollregion=(0, 0, img_width, img_height))

# Add Start Quiz button 
def start_quiz():
    print("Quiz started!")

start_button = tk.Button(root, text="Start Quiz", font=("Aptos", 16), bg="#5CB55F", fg="white", command=start_quiz)
canvas.create_window(img_width // 3, 300,  window=start_button)  

root.mainloop()
