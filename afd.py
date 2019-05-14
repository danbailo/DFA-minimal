from string import ascii_letters as alphabet
class AFDState:
	def __init__(self,name):
		self.name=name
		self.t={}
		self.flag=""
	def __eq__(self,obj):
		if type(obj)==type(self):
			return obj.name==self.name
		elif type(obj)==str:
			return obj==self.name
		return False
	def __repr__(self):
		return self.__str__()
	def addTransition(self,symbol,child):
		if type(child)!=AFDState:raise TypeError("invalid child argument")
		if(type(symbol)!=str):raise TypeError("invalid symbol argument")
		self.t[symbol]=child
	def feed(self,symbol):
		try:return self.t[symbol]
		except KeyError:return None
	def __str__(self):
		return "AFDState(%s)"%self.name
	def __hash__(self):
		return hash(self.__str__())
	def __lt__(self,obj):
		if type(obj)==type(self):return str(self)<str(obj)
		raise TypeError()
class AFD:
	def __init__(self,q,sigma,delta,initial,finals):
		self.delta=delta
		self.q=[]
		for name in q:
			state=AFDState(name)
			if name==initial:
				state.flag+="i"
				self.initial=state
				self.reset()
			if name in finals:
				state.flag+="f"
			self.q.append(state)
		self.sigma=sigma
		m=len(delta)
		n=len(delta[0])
		if len(q)!=m or len(sigma)!=n:
			raise RuntimeError("invalid delta")
		for i in range(m):
			for j in range(n):
				statename=delta[i][j]
				if statename==None:continue
				child=None
				try:child=self.q[self.q.index(statename)]
				except ValueError:pass
				if child==None:continue
				self.q[i].addTransition(self.sigma[j],child)
			pass
	def reset(self):
		self.currstate=self.initial
	def isLanguage(self):
		if self.currstate==None:return False
		return "f" in self.currstate.flag
	def feed(self,word):
		for l in word:
			if l not in self.sigma:raise RuntimeError("word not in sigma")
			self.currstate=self.currstate.feed(l)
			if self.currstate==None:return False
		return self.isLanguage()