import tkinter as tk
root =tk.Tk()
root.geometry("600x300")
root.title("TKInter tutorial")
#Type:Str
# boundStr = tk.StringVar(value= "first option")

# rbl = tk.Radiobutton(root, variable=boundStr ,text ="first" , value="first option" )
# rbl.pack()
# rbl = tk.Radiobutton(root, variable=boundStr ,text ="second" , value="second option" )
# rbl.pack()
# rbl = tk.Radiobutton(root, variable=boundStr ,text ="third" , value="third option" )
# rbl.pack()

#Type:INT

boundInt = tk.IntVar(value= "first option")

rbl = tk.Radiobutton(root, variable=boundInt,text ="first" , value="327" )
rbl.pack()
rbl = tk.Radiobutton(root, variable=boundInt ,text ="second" , value="587" )
rbl.pack()
rbl = tk.Radiobutton(root, variable=boundInt,text ="third" , value="973" )
rbl.pack()

label = tk.Label(root,textvariable = boundInt)
label.pack()

def on_close():
    print("Closing window...")
    root.destroy()

root.protocol("WM_DELETE_WINDOW",on_close)

root.mainloop()