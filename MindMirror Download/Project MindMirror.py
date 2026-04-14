# IMPORTS

import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from PIL import Image, ImageTk
import os

# QUIZ QUESTIONS
quiz = [
    # SPATIAL (5 questions)
    {"img_path": "Questions/Spatial/spatial_1.png", "options": ["A", "B", "C", "D"],  "intelligence": "spatial", "correct_button": 1},
    {"img_path": "Questions/Spatial/spatial_2.png", "options": ["A", "B", "C", "D"],  "intelligence": "spatial", "correct_button": 2},
    {"img_path": "Questions/Spatial/spatial_3.png", "options": ["A", "B", "C", "D"],  "intelligence": "spatial", "correct_button": 2},
    {"img_path": "Questions/Spatial/spatial_4.png", "options": ["A", "B", "C", "D"],  "intelligence": "spatial", "correct_button": 3},
    {"img_path": "Questions/Spatial/spatial_5.png", "options": ["A", "B", "C", "D"],  "intelligence": "spatial", "correct_button": 2},
    
    # LOGICAL-MATHEMATICAL (5 questions)
    {"img_path": "Questions/Logical-Mathematical/logmath_1.png", "options": ["A", "B", "C", "D"], "intelligence": "logical", "correct_button": 3},
    {"img_path": "Questions/Logical-Mathematical/logmath_2.png", "options": ["A", "B", "C", "D"], "intelligence": "logical", "correct_button": 0},
    {"img_path": "Questions/Logical-Mathematical/logmath_3.png", "options": ["A", "B", "C", "D"], "intelligence": "logical", "correct_button": 0},
    {"img_path": "Questions/Logical-Mathematical/logmath_4.png", "options": ["A", "B", "C", "D"], "intelligence": "logical", "correct_button": 1},
    {"img_path": "Questions/Logical-Mathematical/logmath_5.png", "options": ["A", "B", "C", "D"], "intelligence": "logical", "correct_button": 1},
    
    # INTRAPERSONAL (5 questions)
    {"img_path": "Questions/Intrapersonal/intra_1.png", "options": ["A", "B", "C", "D"], "intelligence": "intrapersonal", "correct_button": 1},
    {"img_path": "Questions/Intrapersonal/intra_2.png", "options": ["A", "B", "C", "D"], "intelligence": "intrapersonal", "correct_button": 1},
    {"img_path": "Questions/Intrapersonal/intra_3.png", "options": ["A", "B", "C", "D"], "intelligence": "intrapersonal", "correct_button": 1},
    {"img_path": "Questions/Intrapersonal/intra_4.png", "options": ["A", "B", "C", "D"], "intelligence": "intrapersonal", "correct_button": 1},
    {"img_path": "Questions/Intrapersonal/intra_5.png", "options": ["A", "B", "C", "D"], "intelligence": "intrapersonal", "correct_button": 1},
    
    # INTERPERSONAL (5 questions)
    {"img_path": "Questions/Interpersonal/inter_1.png", "options": ["A", "B", "C", "D"], "intelligence": "interpersonal", "correct_button": 2},
    {"img_path": "Questions/Interpersonal/inter_2.png", "options": ["A", "B", "C", "D"], "intelligence": "interpersonal", "correct_button": 1},
    {"img_path": "Questions/Interpersonal/inter_3.png", "options": ["A", "B", "C", "D"], "intelligence": "interpersonal", "correct_button": 1},
    {"img_path": "Questions/Interpersonal/inter_4.png", "options": ["A", "B", "C", "D"], "intelligence": "interpersonal", "correct_button": 2},
    {"img_path": "Questions/Interpersonal/inter_5.png", "options": ["A", "B", "C", "D"], "intelligence": "interpersonal", "correct_button": 1},
    
    # LINGUISTIC (5 questions)
    {"img_path": "Questions/Linguistic/ling_1.png", "options": ["A", "B", "C", "D"], "intelligence": "linguistic", "correct_button": 1},
    {"img_path": "Questions/Linguistic/ling_2.png", "options": ["A", "B", "C", "D"], "intelligence": "linguistic", "correct_button": 1},
    {"img_path": "Questions/Linguistic/ling_3.png", "options": ["A", "B", "C", "D"], "intelligence": "linguistic", "correct_button": 1},
    {"img_path": "Questions/Linguistic/ling_4.png", "options": ["A", "B", "C", "D"], "intelligence": "linguistic", "correct_button": 2},
    {"img_path": "Questions/Linguistic/ling_5.png", "options": ["A", "B", "C", "D"], "intelligence": "linguistic", "correct_button": 1},
    
    # NATURALISTIC (5 questions)
    {"img_path": "Questions/Naturalistic/natur_1.png", "options": ["A", "B", "C", "D"], "intelligence": "naturalistic", "correct_button": 3},
    {"img_path": "Questions/Naturalistic/natur_2.png", "options": ["A", "B", "C", "D"], "intelligence": "naturalistic", "correct_button": 1},
    {"img_path": "Questions/Naturalistic/natur_3.png", "options": ["A", "B", "C", "D"], "intelligence": "naturalistic", "correct_button": 1},
    {"img_path": "Questions/Naturalistic/natur_4.png", "options": ["A", "B", "C", "D"], "intelligence": "naturalistic", "correct_button": 2},
    {"img_path": "Questions/Naturalistic/natur_5.png", "options": ["A", "B", "C", "D"], "intelligence": "naturalistic", "correct_button": 1},
]

# SCORING
intelligences = ["spatial", "logical", "intrapersonal", "interpersonal", "linguistic", "naturalistic"]
scores = {intel: 0 for intel in intelligences}
max_points = {intel: 0 for intel in intelligences}

current_q_index = 0
question_canvas = None
chart_canvas = None

# SHOW QUESTION
def show_question():
    global current_q_index, question_canvas
    if current_q_index < len(quiz):
        question = quiz[current_q_index]
        
        # Load question image
        if os.path.exists(question["img_path"]):
            img = Image.open(question["img_path"])
            photo = ImageTk.PhotoImage(img)
            question_canvas.image = photo
            question_canvas.delete("all")
            question_canvas.create_image(0, 0, anchor="nw", image=photo)
            question_canvas.config(scrollregion=question_canvas.bbox("all"))
        else:
            question_canvas.delete("all")
            question_canvas.create_text(400, 300, text=f"Image missing: {question['img_path']}", font=("Aptos", 16))
        
        # Update 4-box buttons
        for i, btn in enumerate(option_buttons):
            btn.config(text=question["options"][i], state="normal")
        
        
    else:
        show_results()

# SELECTION BUTTONS
def select_option(idx):
    global current_q_index

    question = quiz[current_q_index]
    intel = question["intelligence"]

    if idx == question["correct_button"]:
        scores[intel] += 1

    max_points[intel] += 1
    current_q_index += 1
    show_question()

# RESULTS SCREEN
def show_results():
    for btn in option_buttons:
        btn.config(state="disabled")

    quiz_frame.pack_forget()
    results_frame = tk.Frame(root)
    results_frame.pack(fill="both", expand=True)

    bg_img = Image.open("Screens/results_screen.png")
    bg_img = bg_img.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
    bg_photo = ImageTk.PhotoImage(bg_img)

    bg_label = tk.Label(results_frame, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    percentages = []
    labels = []
    for intel in intelligences:
        p = (scores[intel] / max_points[intel] * 10) if max_points[intel] > 0 else 0
        p = round(p, 1)
        percentages.append(p)
        labels.append(intel.capitalize())

    angles = np.linspace(0, 2*np.pi, 6, endpoint=False)
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 8))

    fig.patch.set_facecolor("none")
    ax.set_facecolor("none")
    ax.patch.set_alpha(0)

    colors = ["#FF4444", "#4444FF", "#FFAA00", "#44AA44", "#DD44DD", "#44DDDD"]
    ax.bar(angles, percentages, width=2*np.pi/6, alpha=0.8, color=colors,
        edgecolor="white", linewidth=2)

    for angle, label, p in zip(angles, labels, percentages):
        ax.text(angle, 11.2, f"{label}\n{p:.1f}",
                ha="center", va="center",
                fontsize=11, fontweight="bold", color="black",
                rotation=0)

    ax.set_ylim(0, 10)
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_yticklabels([])
    ax.yaxis.grid(True, color="white", linewidth=2)
    ax.xaxis.grid(False)
    ax.set_xticks([])
    ax.spines["polar"].set_color("white")
    ax.spines["polar"].set_linewidth(2)

    fig.text(0.33, 0.97, "YOUR MINDMAP",
            ha="left", va="top",
            fontsize=24, fontweight="bold", color="white")

    chart_canvas = FigureCanvasTkAgg(fig, master=results_frame)
    chart_canvas.draw()
    chart_widget = chart_canvas.get_tk_widget()
    chart_widget.configure(bg="#6868de", highlightthickness=0, bd=0)
    chart_widget.place(relx=0.5, rely=0.5, anchor="center")


# TAB
root = tk.Tk()
root.title("Project MindMirror")
root.geometry("900x700")  
root.state('zoomed')

# WELCOME SCREEN
def start_quiz():
    welcome_frame.destroy()  # Clean up welcome
    quiz_frame.pack(fill="both", expand=True)
    show_question()

image = Image.open("Screens/welcome_screen.png")
photo = ImageTk.PhotoImage(image)
img_width, img_height = image.size

welcome_frame = tk.Frame(root)
welcome_frame.pack(fill="both", expand=True)

canvas = tk.Canvas(welcome_frame, width=1366, height=700)
canvas.pack(side="left", fill="both", expand=True)

v_scroll = tk.Scrollbar(welcome_frame, orient="vertical", command=canvas.yview)
v_scroll.pack(side="right", fill="y")
canvas.configure(yscrollcommand=v_scroll.set)

canvas.create_image(0, 0, anchor="nw", image=photo)
canvas.image = photo
canvas.config(scrollregion=(0, 0, img_width, img_height))

start_button = tk.Button(
    canvas, 
    text="Start Quiz", 
    font=("Aptos", 16, "bold"), 
    bg="#5CB55F", 
    fg="white", 
    relief="raised",
    bd=4,
    padx=30,
    pady=10,
    command=start_quiz
)
canvas.create_window(img_width // 3, 300, window=start_button) 


def on_fullscreen():
    root.state('zoomed')
root.after(100, on_fullscreen)

# QUIZ FRAME
quiz_frame = tk.Frame(root)
question_canvas = tk.Canvas(quiz_frame, bg="lightgray", height=500)
question_canvas.pack(side="left", fill="both", expand=True, padx=(0,10))

options_frame = tk.Frame(quiz_frame, width=350, bg="white")
options_frame.pack(side="right", fill="y")
options_frame.pack_propagate(False)

option_buttons = []
box_colors = ["#FF4444", "#4444FF", "#FFAA00", "#44AA44"]
for i in range(4):
    btn = tk.Button(
        options_frame, text="A", font=("Aptos", 20, "bold"),
        fg="white", bg=box_colors[i], width=12, height=3,
        relief="ridge", bd=8,
        command=lambda idx=i: select_option(idx)
    )
    btn.pack(pady=8, padx=20, fill="x")
    option_buttons.append(btn)

quiz_frame.pack_forget()
root.mainloop()