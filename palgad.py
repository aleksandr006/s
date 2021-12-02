from module1 import *
while True:
a=input("Funktsioonid: \n delet-1\n Add-2\n sortirovka-3\n min-4\n biggest-5\n")
if a=="1":
delete_inimene()
elif a=="2":
add_inimene()
elif a=="3":
sortirovka()
elif a=="4":
smal_palk()
elif a=="5":
big_palk()
break
else:
("eta funktsia ne robit")