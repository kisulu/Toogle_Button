from tkinter import *

root = Tk()
root.title("Toogle Swith")
root.geometry("400x600")
root.config(bg="white")
root.resizable(False, False)


# icon
# image_icon=PhotoImage(file="icon.png")
# root.iconphoto(False,image_icon)

button_mode= True

def customize():

    global button_mode
    if button_mode:
        button.config(image=off, bg="#26242f",activebackground="#26242f")
        root.config(bg="#26242f")
        button_mode = False
    else:
        button.config(image=on, bg="white",activebackground="white")
        root.config(bg="white")
        button_mode=True
        


on=PhotoImage(file="light.png")
off=PhotoImage(file="dark.png")

button=Button(root,image=on,bg="white",bd=0,activebackground="white",command=customize)
button.pack(padx=50,pady=50)

root.mainloop()
