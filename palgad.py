from module1 import *
from tkinter import*
root=Tk()#создаёт окно
root.title("")
root.geometry("2000x1000+100+100")

knop1=Button(root,text="add inimene",font="Arial 15",relief="flat",width=10,height=3,bg="#fb00ff",command=lambda:add_inimene())
knop2=Button(root,text="delete_inimene",font="Arial 15",relief="flat",width=10,height=3,bg="#fb00ff",command=lambda:delete_inimene())
knop1=Button(root,text="big_palk()",font="Arial 15",relief="flat",width=10,height=3,bg="#fb00ff",command=lambda:big_palk())
knop1=Button(root,text="smal_palk()",font="Arial 15",relief="flat",width=10,height=3,bg="#fb00ff",command=lambda:smal_palk())





knop1.pack()
root.mainloop()