class array:

	def __init__(self,cls):
		self.__arr=[]
		self.cls=cls

	def disp(self):
		print(self.__arr)


	def add(self,elm):
		if isinstance(elm,self.cls):
			self.__arr+=[elm]
		else:
			raise TypeError(f'Array of class {self.cls.__name__} : Invalid type {type(elm).__name__}')

	def rotate(self,n):
		if n<=len(self.__arr):
			return self.__arr[n:]+self.__arr[:n]


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



a=array(int)
a.add(20)
a.add(33)
#a.add('65')
a.add(103)
a.add(2)
a.disp()
a.insert(3,2)
print(a.search(33),a.search(36))
a.disp()
b=a.rotate(3)
print(b)
	