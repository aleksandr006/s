def lists()->list:
	"""tegi listid failist
	"""
	palgad=[]
	with open("zarplata.txt", "r") as f1: #avame fail
		for s in f1:
			palgad.append(s.strip()) 
	inimesed=[]
	with open ("ludi.txt", "r") as inimene:
		for q in inimene:
			inimesed.append(q.strip())
	return palgad,inimesed

def add_inimene():
	""" lisamine inimese ja palk
	"""
	nimi=input("Siseta nimi: ")
	palga=input("Siseta palgad: ")
	with open("ludi.txt", "a") as inimesed: #lisame nimi failisse 
		inimesed.write(nimi+"\n")	
	with open("zarplata.txt", "a") as palgad: #lisame palk failisse
		palgad.write(palga+"\n")

def delete_inimene():
	"""delete_inimene()
	"""
	palgad,inimesed=lists() # failid ja kasutamine lsitid 
	nimi=input("Siseta nimi: ")
	if nimi not in inimesed: # vaatame kas on olemas selline inimene
		print("Kas sa tahad lisada nimi ja palgad?") 
		c=input("Y = jah, N = ei")
		if c.upper=="Y":
			add_person() 
		else:
			pass
	else:
		a=inimesed.index(nimi) # otsing  indeks
		inimesed.pop(a) # delet nimi
		palgad.pop(a) #deletpalk
	f=open("ludi.txt", "w")
	for g in inimesed:
		f.write(g+"\n")
	f.close()
	d=open("zarplata.txt", "w")
	for i in palgad:
		d.write(i+"\n")
	d.close()

def big_palk():
	"""Arvutamine suurim palk
	"""
	palgad,inimesed=lists()
	suurim=max(palgad) 
	b=palgad.index(suurim) # indeks muutuja edasiseks kasutamiseks
	print("kõike suured palga on "+inimesed[b]+" palga")

def smal_palk():
	"""arvumine kõige smal palk
	"""
	palgad,inimesed=lists()
	palgadS=palgad.copy()
	palgadS.sort()
	a=palgadS[0]
	b=palgad.index(a)
	print("kõike väiksem palga on "+inimesed[b]+" palga ja see on "+ palgadS[0]+" euro")

def sortirovka():
	"""sortirovka()
	"""
	palgadS=[]
	palgad,inimesed=lists()
	palgadS=palgad.copy()
	palgadS.sort()
	for palk in palgadS:
		a=palgad.index(palk) #  otsime indeks et leida nimi ja palk sorteerimata loenditesтированых списках
		print(palgad[a]+" "+inimesed[a])




