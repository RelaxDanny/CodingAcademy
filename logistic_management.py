# import tkinter as tk
# from tkinter import filedialog as fd 
# import base64

# def getImage_convert():
#     name= fd.askopenfilename()
#     print(name)
#     with open(name, "rb") as image:
#         f = base64.b64encode(image.read())

#     if name[-3:] == 'jpg':
#         with open("imageToSave.jpg", "wb") as fh:
#             fh.write(base64.decodebytes(f))
#     if name[-3:] == 'png':
#         with open("imageToSave.png", "wb") as fh:
#             fh.write(base64.decodebytes(f))
    
    
# errmsg = 'Error!'
# tk.Button(text='Click to Open File', 
#        command=getImage_convert).pack(fill=tk.X)
# tk.mainloop()
import tkinter
from TkinterDnD2 import *

def drop(event):
    entry_sv.set(event.data)

root = TkinterDnD.Tk()
entry_sv = Tkinter.StringVar()
entry = Tkinter.Entry(root, textvar=entry_sv, width=80)
entry.pack(fill=Tkinter.X)
entry.drop_target_register(DND_FILES)
entry.dnd_bind('<<Drop>>', drop)
root.mainloop()