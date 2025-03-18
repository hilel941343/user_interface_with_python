import tkinter as tk

root = tk.Tk()
root.geometry("600x300")
root.title("TKInter tutorial!")


button1 = tk.Button(root, text="Click me")
button1.pack(side=tk.LEFT, fill=tk.Y)
button2 = tk.Button(root, text="Click me")
button2.pack(side=tk.LEFT, fill=tk.Y)

root.mainloop()