import tkinter as tk
welcome_label = tk.Label (text="Welcome! Click the oval to start scoring.", font=("Arial", 14), fg="green")
welcome_label.pack()
welcome_label.winfo_geometry = ("500x500")
def increase_score(event):
    x, y = event.x, event.y
    if canvas.coords(oval)[0] <= x <= canvas.coords(oval)[2] and canvas.coords(oval)[1] <= y <= canvas.coords(oval)[3]:
        global score
        score += 1
        score_label.config(text=f"Score: {score}")

root = tk.Tk()
root.title("Clicker Game")

score = 0

score_label = tk.Label(root, text=f"Score: {score}", font=("Arial", 16))
score_label.pack()

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack()
oval = canvas.create_oval(100, 50, 200, 150, fill="blue")
canvas.bind("<Button-1>", increase_score)
root.mainloop()

