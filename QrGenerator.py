from tkinter import *
import pyqrcode
import png
from tkinter import filedialog
from PIL import Image, ImageTk

root=Tk()
root.geometry('500x500')

def create_code():
    input_path=filedialog.asksaveasfilename(title="Save Image",filetyp=(("PNG File",".png"),("All Files","*.*")))
    
    if input_path:
        if input_path.endswith(".png"):
            # Creat QR code from entry box
            get_code=pyqrcode.create(my_entry.get())
            #save as PNG File
            get_code.png(input_path,scale=5)
        
        else:
            # Add that .png to the end of the file name
            input_path= f'{input_path}.png'
            # Create QR Code from entry box
            get_code=pyqrcode.create(my_entry.get())
            #save as PNG File
            get_code.png(input_path,scale=5)

        # Put QR code on screen
        global get_image
        get_image= ImageTk.PhotoImage(Image.open(input_path))
        # Add image to label
        my_lable.config(image=get_image)
        # Delete entry box
        my_entry.delete(0, END)
        # Flash up a finished message
        my_entry.insert(0, "Finished!")



def clear_all():
    my_entry.delete(0, END)
    my_lable.config(image='')

my_entry=Entry(root,font=("Helvetica",18))
my_entry.pack(pady=20)

button_1=Button(root,text="Create Qr Code",command=create_code)
button_1.pack(pady=20)

button_2=Button(root,text="Clear",command=clear_all)
button_2.pack()

my_lable=Label(root,text='')
my_lable.pack(pady=20)

root.mainloop()