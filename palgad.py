from module1 import *
from tkinter import*
root=Tk()
root.title("Face")
root.geometry('1000x500')
root.configure(bg="blue")
root.grab_set()
knop1=Button(root,text="add inimene",font="Arial 15",relief="flat",width=10,height=3,bg="#FF4500",command=lambda:add_inimene())
knop2=Button(root,text="delete inimene",font="Arial 15",relief="flat",width=10,height=3,bg="#FF4500",command=lambda:delete_inimene())
knop3=Button(root,text="big palk",font="Arial 15",relief="flat",width=10,height=3,bg="#FF4500",command=lambda:big_palk())
knop4=Button(root,text="smal palk",font="Arial 15",relief="flat",width=10,height=3,bg="#FF4500",command=lambda:smal_palk())
knop5=Button(root,text="sortirovka",font="Arial 15",relief="flat",width=10,height=3,bg="#FF4500",command=lambda:sortirovka())








knop1.pack()
knop2.pack()
knop3.pack()
knop4.pack()
knop5.pack()
root.mainloop()