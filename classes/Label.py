import tkinter as tk
root =tk.Tk()
root.geometry("600x300")
root.title("TKInter tutorial")



entry = tk.Entry(root)
entry.pack()

label = tk.Label(root)
label.pack()

def update_text():
    update_text = entry.get()
    label['text'] = update_text
button = tk.Button(root,text= "update text",command=update_text)
button.pack()

root.mainloop()