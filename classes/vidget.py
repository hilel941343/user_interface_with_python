import tkinter as tk

root = tk.Tk()
root.geometry("600x300")
root.title("TKInter tutorial!")
# כל דבר שאנחנו מוסיפים לחלון כמו טקסט או תיבת טקסט וכו' נקרא וידגט בUI
label = tk.Label(root, text="Hello tkinter")
# pack -מוסיף את הוידג'טים בזה אחר זה שורה אחרי שורה
label.pack()

textbox = tk.Text(root, height=1)
textbox.pack()
entry = tk.Entry(root)
entry.pack()

checkbox = tk.Checkbutton(root, text="I'm hungry")
checkbox.pack()


def handleClick():
    print("Button clicked")


button = tk.Button(root, text="Click me", command=handleClick)
button.pack()
root.mainloop()
