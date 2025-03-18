import tkinter as tk

root = tk.Tk()
root.geometry("600x300")
root.title("TKInter tutorial!")

frame1 = tk.Frame(root)
frame1.pack(fill=tk.X, pady=20)

frame2 = tk.Frame(root)
frame2.pack()


button1 = tk.Button(frame1, text="Click me")
button1.pack(side=tk.LEFT, fill=tk.X, expand=True)
button2 = tk.Button(frame1, text="Click me")
button2.pack(side=tk.LEFT, fill=tk.X, expand=True)
button3 = tk.Button(frame1, text="Click me")
button3.pack(side=tk.LEFT, fill=tk.X, expand=True)
button4 = tk.Button(frame2, text="Click me")
button4.pack(side=tk.LEFT)
button5 = tk.Button(frame2, text="Click me")
button5.pack(side=tk.LEFT)
button6 = tk.Button(frame2, text="Click me")
button6.pack(side=tk.LEFT)
root.mainloop()
