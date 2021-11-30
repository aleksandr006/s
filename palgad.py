from module1 import*
p=loe_failist_listisse("ludi.txt")
i=loe_failist_listisse("zarplata.txt")
while True:
	a=input("Funktsioonid: \n Add-1\n remove-2\n biggest-3\n smallest-4\n sorteerimine-5\n search-7\n tulumaks-8")
	if a=="1":
		add_person()
	elif a=="2":
		delete_person()
	elif a=="3":
		suurim_palk(i,p)
	elif a=="4":
		smallest_salary()
	elif a=="5":
		sorting()
	elif a=="7":
		search_name()
	elif a=="8":
		tulumaks()
	elif a.upper=="E":
		break
	else:
		("See funktsioon ei tööta või ei olema")