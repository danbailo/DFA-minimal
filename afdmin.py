from afd import AFD,AFDState
from ast import literal_eval as leval
from sys import argv,exit
from copy import deepcopy
import copy

def readAfdFromFile(filename):
	f=open(filename)
	states=list(leval(f.readline().strip()))
	sigma=list(f.readline().strip())
	delta=[]
	for i in range(len(states)):
		temp=leval(f.readline().strip())
		if len(temp)!=len(sigma):raise RuntimeError("invalid delta on "+filename)
		for t in temp:
			if t not in states:
				raise RuntimeError("invalid delta on "+filename)
		delta.append(list(temp))
	initial=leval(f.readline().strip())
	if initial not in states:raise RuntimeError("invalid initial on "+filename)
	final=leval(f.readline().strip())
	final=list(final)if type(final)==tuple else [final]
	for temp in final:
		if temp not in states:raise RuntimeError("invalid final on "+filename)
	f.close()
	return AFD(states,sigma,delta,initial,final)
def step3(q,sigma,table):
	table=deepcopy(table)
	for i,qi in enumerate(q):
		for j,qj in enumerate(q):
			if i<=j:continue
			for s in sigma:
				x=q.index(qi.feed(s))
				y=q.index(qj.feed(s))
				if y>x:x,y=y,x
				if table[x][y]:
					table[i][j]=True
	return table
def afdMin(afd):
	def tableComp(t1,t2):
		b=True
		for i in range(len(t1)):
			b&=t1[i]==t2[i]
		return b
	isFinal=lambda q:"f" in q.flag
	#passo 1
	table=[[False]*len(afd.q) for _ in afd.q]
	#passo 2
	for i,qi in enumerate(afd.q):
		for j,qj in enumerate(afd.q):
			if i<=j:continue
			table[i][j]=isFinal(qi)^isFinal(qj)
	#passo 3, repetir até parar de mudar
	while True:
		tableNew=step3(afd.q,afd.sigma,table)
		if tableComp(tableNew,table):break
		table=tableNew
	del tableNew
	#coletar pares
	temp=[]
	for i,qi in enumerate(afd.q):
		for j,qj in enumerate(afd.q):
			if i<=j:continue
			if not table[i][j]:
				temp.append(set([qj,qi]))
	#juntar conjuntos similares
	mergeList=[]
	while temp!=[]:
		t=temp.pop()
		for g in temp.copy():
			if (t&g)!=set():
				t|=g
				temp.remove(g)
			pass
		mergeList.append(t)
	#adicionar estados restantes
	for q in afd.q:
		b=False
		for g in mergeList:b|=q in g
		if b:continue
		mergeList.append({q})
	#nomear novos estados
	newQ=[]
	for g in mergeList:
		temp=list(g)
		temp.sort()
		newQ.append(str([q.name for q in temp]))
	
	#criar novo delta com nós mergidos
	newDelta=[[]for _ in newQ]
	for i,g in enumerate(mergeList):
		for s in afd.sigma:
			dest=set()
			for q in g:dest|={q.feed(s)}
			desti=False
			for ii,gg in enumerate(mergeList):
				if (dest&gg)!=set():
					desti=ii
					break
			if desti is False:raise RuntimeError("Mergelist gerado errado")
			newDelta[i].append(newQ[desti])
		pass
	#achar o estado inicial e estados finais nos grupos
	newInitial=False
	newFinals=[]
	for gi,g in enumerate(mergeList):
		for q in g:
			newqgi=newQ[gi]
			if "i" in q.flag:
				newInitial=newqgi
			if isFinal(q):
				if newqgi not in newFinals:newFinals.append(newqgi)
	if newInitial is False:raise RuntimeError("Mergelist gerado errado")
	return AFD(newQ,afd.sigma,newDelta,newInitial,newFinals)

def show_afdMin():
    if len(argv)<2:
        print("[USO]main.py [arquivo]")
        print("Por favor, adicione como parâmetro um arquivo de entrada!")
        exit(-1)

    afd=readAfdFromFile(argv[1])
    afdmin=afdMin(afd)

    print("Estados:")
    print([q.name for q in afdmin.q])
    print("\nSigma:")
    print(afdmin.sigma)
    print("\nDelta:")
    for q in afdmin.q:
        print([qq.name for qq in q.t.values()])
    print("\nEstado inicial:")
    print(afdmin.initial.name)
    print("\nEstados finais:")
    finals=[]
    for q in afdmin.q:
        if "f" in q.flag:
            finals.append(q.name)
    print(finals)
    return afd,afdmin