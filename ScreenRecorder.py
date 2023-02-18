from tkinter import *
import pyscreenrec

root = Tk
root.geometry('400x600')
root.title('Screen Recorder')
root.config(']fff')
root.resizable(False, False)

#command functions
def start_screen_rec():
    file=filesave.get()
    rec.start_recording(str(file+',mp4'),5)

def pause_screen_rec():
    rec.pause_recording()

def resume_screen_rec():
    rec.resume_recording()

def stop_screen_rec():
    rec.stop_recordng()


record=pyscreenrec.ScreenRecorder()

#window icon
window_icon=PhotoImage(file="icon.png")
root.iconphoto(False,window_icon)

#window bg
window_bg=PhotoImage(file="bg.png")
Label(root, image = window_bg, bg= '#fff').place(x=50, Y=50)

#window header
header = Label(root, text='Screen Recorder', bg='#fff', font='Cambria 15 bold').pack(pady=20)

#window logo
logo = PhotoImage(file='logo.png')
Label(root, image=logo, bd=0).pack(pady=30)

#file entries
filesave=StringVar()
saved_file=Entry(root, textvariable=filesave, width=18, font='Cambria 14')
saved_file.place(x=100, y=300)

filesave.set('enter file name')

#start button
record_image = PhotoImage(file='record.png')
start_button = Button(root, image='record.png', font='Cambria 22', bd=0, command=start_screen_rec)
start_button.place(x=20, y=20)

#pause image and button
pause_image = PhotoImage(file='pause.png')
pause_button = Button(root, image=pause_image, bd=0, bg='#fff', command=pause_screen_rec)
pause_button.place(x=70, y=70)

#stop image and button
stop_image = PhotoImage(file='stop.png')
stop_button = Button(root, image=stop_image, bd=0, bg='#fff', command=stop_screen_rec)
stop_button.place(x=110, y=70)

#resume image and button
resume_image = PhotoImage(file='resume.png')
resume_button = Button(root, image=resume_image, bd=0, bg='#fff', command=resume_screen_rec)
resume_button.place(x=150, y=70)


root.mainloop()