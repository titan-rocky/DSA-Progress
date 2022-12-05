class array:

	def __init__(self):
		self.__arr=[]

	#setter
	def add(self,element):
		self.__arr+=[element]

	#getter
	@property
	def display(self):
		return list(self.__arr) #self._arr is display : False

	def insert(self,element:int,index:int):
		for i in range(len(self.__arr)):
			if index==i:
				self.__arr=self.__arr[:i]+[element]+self.__arr[i+1:]

	def search(self,element:int):
		for i in range(len(self.__arr)):
			if element==self.__arr[i]:
				return i #index
				
		else:
			return -1



a=array()
a.add(20)
a.add(33)
a.add(65)
a.add(103)
a.add(2)
print(a.display)
a.display[4]=5
a.insert(3,2)
print(a.search(33),a.search(36))
print(a.display)
	