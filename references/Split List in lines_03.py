lista1 = ["1", "2", "3"]
lista2 = ["objeto"]
lista_master=[]

for i in lista1:
	lista_master.append(i)

for i in lista2:
	lista_master.append(i)

print lista_master
print ('\n'.join(lista_master))
