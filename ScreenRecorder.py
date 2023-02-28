from tkinter import *
import pyscreenrec

# def makeTransparent (img, colorToMakeTransparent):
#     newPhotoImage = PhotoImage(width=img.width(), height=img.height())
#     for x in range(img.width()):
#         for y in range(img.height()):
#             rgb = '#%02x%02x%02x' % img.get(x, y)
#             if rgb != colorToMakeTransparent:
#                 newPhotoImage.put(rgb, (x, y))
#     return newPhotoImage


root = Tk()
root.geometry('400x600')
root.title('Screen Recorder')
root.config(bg='#d0dbe4')
root.resizable(False, False)

# mycanvas = Canvas(root, width=200, height=200, bg='orange').pack()
#window logo
# logo = PhotoImage(file='logo.png')
# logo = makeTransparent(logo, '#ffffff')
# canvasImage = mycanvas.create_image(100, 100, image=logo, ANCHOR=CENTER)
# Label(root, image=logo, bd=0, bg='blue').pack(pady=30)

#command functions
def start_rec():
    file=Filename.get()
    record.start_recording(str(file+".mp4"),15)

def pause_rec():
    record.pause_recording()

def resume_rec():
    record.resume_recording()

def stop_rec():
    record.stop_recording()



record=pyscreenrec.ScreenRecorder()

#window icon
window_icon=PhotoImage(file="icon.png")
root.iconphoto(False,window_icon)

#window bg
# window_bg=PhotoImage(file="bg.png")
# Label(root, image = window_bg, bg= '#fff').place(x=50, y=50)

#window header
header = Label(root, text='Screen Recorder', bg='#d0dbe4', font='Cambria 15 bold').pack(pady=20)
Label(root, text='-by Josh', font='Cambria 12', bd=0, bg='#d0dbe4').place(x=240, y=45)
# #window logo
logo = PhotoImage(file='logo.png')
Label(root, image=logo, bd=0, bg='#d0dbe4').pack(pady=30)

#file entries
Filename=StringVar()
entry=Entry(root, textvariable=Filename, width=20, font='Calibri 13', bg='#d0dbe4')
entry.place(x=100, y=380)
Filename.set('new_recording')

#start button
record_image = PhotoImage(file='record.png')
start_button = Button(root, image=record_image, font='Cambria 22', bd=0, bg='#d0dbe4', command=start_rec)
start_button.place(x=40, y=460)

#pause image and button
pause_image = PhotoImage(file='pause.png')
pause_button = Button(root, image=pause_image, bd=0, bg='#d0dbe4', command=pause_rec)
pause_button.place(x=122, y=460)

#stop image and button
stop_image = PhotoImage(file='stop.png')
stop_button = Button(root, image=stop_image, bd=0, bg='#d0dbe4', command=stop_rec)
stop_button.place(x=310, y=460)

#resume image and button
resume_image = PhotoImage(file='resume.png')
resume_button = Button(root, image=resume_image, bd=0, bg='#d0dbe4', command=resume_rec)
resume_button.place(x=218, y=460)


root.mainloop()