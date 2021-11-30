def add_person ():
	"""lisamine inimese ja palk (valmis)
	"""
	nimi=input("Siseta nimi: ")
	palga=input("Siseta palgad: ")
	with open("inimesed.txt", "a") as inimesed:
		inimesed.write(nimi+"\n")	
	with open("palgad.txt", "a") as palgad:
		palgad.write(palga+"\n")
def delete_person ():
	"""Eemaldamine mees ja palk (valmis)
	"""
	f=open("inimesed.txt", "r")
	inimesed=[]
	for stroka in f:
		inimesed.append(stroka.strip())
	f.close
	nimi=input("Siseta nimi: ")
	if nimi not in inimesed:
		print("Sa pead nimi ja palk/?")
		c=input("Y = jah, N = ei")
		if c.upper=="Y":
			add_person()
		else:
			pass
	else:
		palgad=[]
		with open("palgad.txt", "r") as f1:
			for stro in f1:
				palgad.append(stro.strip())
		a=inimesed.index(nimi)
		inimesed.pop(a)
		palgad.pop(a)
	f=open("inimesed.txt", "w")
	for g in inimesed:
		f.write(g+"\n")
	f.close()
	d=open("palgad.txt", "w")
	for i in palgad:
		d.write(i+"\n")
	d.close()
def suurim_palk(i,p):
	suurim=max(p)
	b=p.index(suurim)
	kellel=i[b]
	return suurim,kellel

def smallest_salary():
	"""вычисление самой маленькой зарплаты (готово)
	"""
	palgad,inimesed=lists()
	palgadS=palgad.copy()
	palgadS.sort()
	a=palgadS[0]
	b=palgad.index(a)
	print("kõike väiksem palga on "+inimesed[b]+" palga ja see on "+ palgadS[0]+" euro")
def sorting():
	"""sordi palk nimedega kasvavas järjekorras 
	"""
	palgadS=[]
	palgad=[]
	with open("zarplata.txt", "r") as f1:
		for s in f1:
			palgad.append(s.strip())
	inimesed=[]
	with open ("ludi.txt", "r") as inimene:
		for q in inimene:
			inimesed.append(q.strip())
	palgadS=palgad.copy()
	palgadS.sort()
	for palk in palgadS:
		a=palgad.index(palk)
		print(palgad[a]+" "+inimesed[a])
def search_name():
	"""Otsi palk vastavalt mehele
	"""
	palgad=[]
	with open("zarplata.txt", "r") as f1:
		for s in f1:
			palgad.append(s.strip())
	inimesed=[]
	with open ("ludi.txt", "r") as inimene:
		for q in inimene:
			inimesed.append(q.strip())

	nimi=input("Siseta nimi: ")
	for inimene in inimesed:
		if inimene==nimi:
			n=inimesed.count(nimi)
			b=0
			t=[]
			for i in range(n):
				k=inimesed.index(nimi,b)
				palk=palgad[k]
				b+=k+1
				t.append(nimi+" "+str(palk))
			print(t)
		else:
			print("nimi ei ole")
def loe_failist_listisse(file:str)->list:
    """Loeme tekst failist ja salvesta järjendisse
    """
    file=open(file,"r")
    list_=[]
    for stroka in file:
        list_.append(stroka.strip())
    file.close()
    return list_
def keskmine(i,p):
	summa=0
	for palk in p:
		summa+=palk
		kesk=summa/len(p)
		print(kesk)
		vahe=0
		if 0<=p.index(kesk)<len(p)-1:
			return kesk
		else:
			kesk="Puudub"
			return kesk

