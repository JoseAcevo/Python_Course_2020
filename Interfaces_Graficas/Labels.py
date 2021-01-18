from tkinter import *

root = Tk()
miFrame = Frame(root, width=520, height=520)

#miLabel = Label(miFrame, text='Primer Label')
#miLabel.place(x=120, y=125)
#Label(miFrame, text='Primer Label', fg="blue", font=('verdana',20 )).place(x=120, y=125)


Image = PhotoImage(file="F:\Python_programing\Curso tutorizado Python\Interfaces_Graficas\Imágenes\Python.png")
Label(miFrame, image=Image).place(x=0, y=0)








miFrame.pack()
root.mainloop()