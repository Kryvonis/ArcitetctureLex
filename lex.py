======TABLE=====================================================================================================================================================================================:
	-----------------------------------------------------------------
	| 			 	| 	mytable		|	Ordered 	| 	Buddered 	|
	-----------------------------------------------------------------
	| 	list		| 		+		|		+		|		-		|
	|	tuple 		|		-		|		+		|		-		|
	| 	dict		|		+		|		-		|		-		|
	| 	set	  	 	|		+		|		-		|		-		|
	|  str  | bytes | 		+		|		+		|		+		|
	|unicode| str	|		-		|		+		|		+		|
	|  bytearray	|		+		|		+		|		+		|
	|  frozenset	|		-		|		-		|		-		|
	|  memoryview	|		+		|		+		|		+		|
	 ----------------------------------------------------------------
======FUNCTION (part 1)=========================================================================================================================================================================:
	l = [1,7,3,2,4,6]
	for i in l:
		if i == x:
			print('Yes')
			break  	#якщо виходимо по break тоді зайдемо в вітку else 
	else:
		print('No')

	l = [x*x for x in range(10)]
	# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

	def f(x):
		return 2*x

	def sum_(a,*args):
		s = a
		for i in args:
			s+=i
		return s
	sum_(1,2,3)
	# 6

	def sum_(a,*args,**kwargs):
		s = a
		for i in args:
			s+=i


	def f(n):
		def g(x):
			return n*x
		return g

	double  = f(2)

	map(double , range(100))

	def odd(x):
		return x%2

	filter(odd,range(10))
	[1,3,5,7,9]


	reduce(add,range(5))
	[0,1,2,3,4]
	result ---> 10

	map(labda x: 2*x,range(10))
======FUNCTION (part 2)=========================================================================================================================================================================:

	a = 5

	def f(x , y = a):
		return x*y

	f(2) -----> 10
	a = 3
	f(2) -----> 10

	def f(a , l = []):
		l.append(a)
		print(a)

	f(1) -----> [1]
	f(1) -----> [1,1]


	def f(a , l = []):
		l.append(a)
		print(a)
		return l

	f(1) -----> [1]
	f(1) -----> [1,1]

	l = f(1)
	l.append(2)
	f(1) -----> [1,1,2,1]


	def f(a=None):
		if a is None:
			...

	f()
	f(1)
	f(None)
======DECORATOR=================================================================================================================================================================================:

	_no_value = object()

	def f(a=_no_value):
		if a is _no_value:
			...


	def get_area(x):
		return x*x

	def scale(f):
		def wrapper(x):
			print("In")
			res = f(x*10)
			print ("Out")
			return res
		return wrapper

	get_area = scale(get_area)


	def scale(n):
		def decorator(f):
			def wreper(x):
				return f(x*n)
			return wrapper
		return decorator

	get_area = scale(10)(get_area)
======OBSERVER==================================================================================================================================================================================:

	observer = []

	def register(observer):
		observers.append(observer)

	def unregister(observer):
		observer.remove(observer)

	def a():
		print('a')

	def b():
		print('b')
	def c():
		print('c')
	-----------------Event Code--------------------:
		def event():
			print('Event') #Хід певної фігури 
						   #Повідомити всіх тих хто підписаний на цю подію
			for observer in observers:
				observer()
	-----------------Register Observers------------:

		register(a)
		register(b)
		register(c)

		event() ----------> 'Event'
							'a'
							'b'
							'c'

		remove(a)
		event() ----------> 'Event'
							'b'
							'c'
======OBSERVER AND DECORATOR====================================================================================================================================================================:
	def notify(f):
		def wrepper():
			res = f()
			for observer in observers:
				observer()
			return res
		return wrapper
	-----------------Event Code--------------------:
		@notify
		def event():
			print('Event')
======FILE======================================================================================================================================================================================:


	#Другий параметер
	#Режими відкриття файлу
	#t-текс b-бінарний
	#w - write (відкритання для запису)
	#r - read (відкритання для читання)
	#a - append (для додавання) (якщо вайлу немає то буде створенний)
	#x - (для додавання) (якщо файлу немає то помилка)
	#w+ - (для запису і читання) 
	#r+ - (для запису і читання)
	#a+ - (для запису і читання)

	f = open('filename.txt','###')

	f.close()

	f.flush() #зберегнти зміни
	-----------------Запис в файл------------------:

		f.write('string1\n')
	-----------------Читання з файлу---------------:

		s = f.read() # Зчитає весь файл в String
		s = f.readline() # зчитує порядково (якщо доходимо до кінця то отримуємо порожній рядок)

		for line in iter(f.readline(),''):

		s = f.read(10)

		for line in f:

		f.readinto()

		f.tell() # вказує де стоїть файловий вказівник
		f.seek(pos,0/1/2) # посунути файл вказівник (pos - позиція на яку посунути, 0 - з поточної ,1 - з початку, 2 - з кінця)


	-----------------Сontext manager---------------:
		with open('my.txt','r') as f:
			#працює в межах цього контексу
			#
			#
			for line in f:
				print line
				...
			#	
			#
			#
		# в цьому місці файл закриється 


		repr() - переведення данних в текст
				# можемо замінити 
		repr(x) >>>>>>>>>>>>>>>>>`x`
	======Serialization=============================================================================================================================================================================:
		module pickle 
		# для серіалізації
		module cPickle 
		# також для серіалізаці
		# якщо модуль який починається з літери "с" то він написаний на С 

		obj = [1,'aaa',True,{'a',(1,2,3)}]

		import pickle
		with open('obj.pickle','wt') as f:
			pickle.dump(obj,f)

			s = pickle.dumps(obj) # запише в рядок серіалізований обєкт

			obj1 = pickle.loads(s) # зчитає обєкт з тими ж значеннями що і були записані (обєкт буде новий але ідентичний записаному)

			obj1 = pickle.load(f)
		-----------------JSON--------------------------:
			<<<JavaScriptObjectNotation>>>
			obj = [1,'aaa',true,{'a':[1,2,3]}] # результат на JavaScript

			import json
			json.dump(obj,f)
			obj1 = json.load(f)
			s = json.dumps(obj)
			obj1 = json.loads(s)
		-----------------Photobuf----------------------:
	
	-----------------MODULE OS---------------------:
		module os # обгортає всі стандартні функції для роботи з системою
		# інкапсулює всю функціональність нашої системи

		#Перегладаємо зміст поточної дерикторії
		import os
		l =  os.listdir('.') # список всіх файлів і директорій
		os.getcwd() # функція яка повертає почтону дерикторію
		os.cd()
		os.rmdir / mkdir / # 

		os.path() # містить можливості для роботи з шляхами для файлів 

		os.path('..','/') # поєднує імена директорій 

		os.walk() #пошук файла в дереві директорії
		for root,dirs,files in os.walk('/'):
			if file_ in files:
				print(root)
	-----------------Format STR---------------------:
		'Date: '+ date + ';task: '+ task  # Так погано робити

		'Date: %s ; task: %s' % (date,task) # так краще python 2
		'Date: {}; task.{}'.format(date,task) # так краще на python 3
======MODULE====================================================================================================================================================================================:
	$PYTHONPATH
	import sys
	sys.path #список шляхів з якого пітом може імпорувати модуль

	import modulel # бере їмя з розширяння .py // .pyc  // .so (.dll) далі виконується код який є в цьому модолі


	# якшо наприклад в modulel.py 
	a = 1 
	# після імпорту ми зможемо використовувати все що там написано

	import modulel
	modulel.a ---> 1
@04/08
======Class (part 1)============================================================================================================================================================================:
	1. 3 Механізми
	2. 5 принципів SOLID (Роберт Мартін "Гнучка розробка ля ля ля")
	3. >20 патернів 
	
	всі класи наслідуються від object 

	class ClassName(object):
		"""docstring for ClassName"""
		def __init__(self, arg):
			super(ClassName, self).__init__()
			self.arg = arg
		
	class A(object):
		pass

	B = A
	a = A()
	b - B()
	a equal b 
	у екземпляра а буде властивість a.__dict__  - це словник який містить властивості нашого класу
	a.__dict__['x'] = 1 після цього зяветься властивіть x  -------> a.x ----> 1
	a.x = 1 це теж саме що і попереднє
	vars(a) вміст всього __dict__

	class A:
		def set_x(self,x):
			self.x = x
		""""Constructor прийнято так називати але насправді це не конструктор а ініціалізатор """
		def __init__(self,x):
			set_x(x)

	a = A() ---> помилка 
	a = A(1) ---> все ок

	class B:
		pass

	a.__class__ = B
	якшо змінюємо змінну клас тоді ми перевизначаємо шлях пошуку функцій
	спочатку шукається в екземплярі а далі по змінній класс шукається функція
	-----------------Тест для Класів---------------:
		import unittest.mock
		створє фейкові обєкт для тествання

		class A:
			def __init__(self):
				self.x = 5

		a = A()

		def f():		
			return a.x

		@mock.patch('src/controller/a')
		def test_f(obj,b):
			b.x = 42
			self.assertEqual(f(),42)
@04/15
======Class (part 2)============================================================================================================================================================================:
	isinstance(x,int) враховує іерархію успадкування
	це краще ніж if type(x) == int

	import numbers - це модуль визначає всі базові типи

	numbers.Number - це всі можливі числові типи
	isinstance(x,numbers.Number) - найкращий варіант

	class ClassName(object):
		"""docstring for ClassName"""
		def __init__(self, arg):
			self.arg = arg - це публічна змінна
			self._arg = arg - це "приватна" змінна
			self.__arg = arg - це приватна змінна. Не буде доступна за межами нашого класу (майже)

	c = ClassName(2)
	vars(p)

	{'arg':2,'_arg':2,'_ClassName__arg':2}  для secret змінних пайтон застсовує спотворення імен.
	Це спеціальні імена які ми можемо використовувати для класів які успадкованні один від одного

	class A(object):
		"""docstring for A"""
		def __init__(self, arg):
			self.__arg = arg - в цьому класі це імя буде виглядадти як '_A__arg'

	class B(B):
		"""docstring for B"""
		def __init__(self, arg):
			super().__init__() - після цього визветься клас А і після цього в екземплярі В зяветься змінна __arg
			self.__arg = 1 - і тоді ми отримуємо дві змінні (таким чимон захищаємо від перевизначення) {'_B__arg':1,'_A_arg':}
			

	MRO - methor resolution order (вирішення множинного наслідування)


					.object

				.A 		.B  	.C
			 .D	  .E  	
				.I     .F
					.G
						.H

	Для побудови MRO почали застосовувати алгоритм С3
	він забеспечує дві важливі властивості локального старшинства. Якщо в класі H є піддерево ієрархій то в предку піддерево буде зберігатись
	Як він працює - цей алгоритм він так саме працює за правилом зліва на право але для кожного класу будується лінерізація 
	для класу А це буде (A,object)
	для класу B це буде (B,object)
	для класу C це буде (C,object)
	I(D,E)
	E(A)
	і це будується в список
	далі ми починаємо рухатись зіва в гору(якщо клас знаходиться в )
	H.mro()
	H -> G > I -> D -> E -> A -> F -> B -> C -> object
	якщо B(A), C(B,A) то тоді C.mro() -> OK!
	якщо B(A), C(A,B) - C.mro() -> runtime error
	-----------------super()---------------------------:
		B(A)
	super().__init__ - ок

	class Shape:
		"""docstring for Shape"""
		def __init__(self, pos):
			self.pos = pos

	class Circle(Shape):
			"""docstring for Circle"""
			def __init__(self, pos,r):
				super().__init__(pos)
				self.r = r;


	class ColoredShape(Shape):
			"""docstring for ClassName"""
			def __init__(self, pos,col):
				self.col = col
				self.pos = pos

	class StripedShape(Shape):
		"""docstring for StripedShape"""
		def __init__(self, pos,width):
			self.pos = pos
			self.width = width
	
	class ColoredCircle(Circle,ColoredShape):
		"""docstring for ColoredCircle"""
		def __init__(self,partos,r,color):
			super().__init__(pos,r)

	class A(object):
		"""docstring for A"""
		a = 1
		def __init__(self, arg):
			super(A, self).__init__()
			self.arg = arg
	

	-------ДВА ЦІКАВИХ ДЕКОРАТОРА---------:
		class A:
			@staticmethod
			def hello():

		A.f()

		class A:
			@classmethod
			def g(cls): -> отримуємо сам клас

	-----------------UML------------------:
		залежність - 
		спадкування - 
		агрегація - 




	class Persone(object):
		"""docstring for Persone"""
		def __init__(self, name, age):
			self.name = name
			self.age = age

		def __repr__(self):
			return "Persone('{}'.{})".format(self.name,self.age)

		def __str__(self):
			return "{},{}".format(self.name,self.age)
		"""
		[0.1]
		"""
		def __eq__(self,other):
			if isinstance(other,Persone):
				return self.name == other.name and self.age == other.age
			return False
		"""
		[0.2]
		"""
		def __lt__(self,other):
		return self.name < other.name and self.age < other.age

		def __hash__(self):
			return hash(self.name)


	p1 = Persone('Artem',19)
	p2 = Persone('Bill',30)
	p1 == p2 ---> False 	[0.1]

	l = [Persone('Bill',30),Persone('Bill',30)]

	l.index(Persone('Bill',30)) -> також буде працювати оскільки порівнюємо на індекс
	l.sort() -> не працювати

	реалізуємо компаратор [0.2]


	class Number:
		"""docstring for Number"""
		def __init__(self, value):
			self.value = value

		def __repr__(self):
			return 'Number(%d)'%self.value

		def __add__(self,other): ----> Number(2) + 1 -> OK
			if isinstance(other,Number):
				return Number(self.value+other.value)
			return Number(self.value + other)

		def __radd__(self,other):   ---> 1 + Number(2) -> OK
			return self.__add__(self,other)

		"""iterator"""
		Martin Fauler "Проектрования больше нет" знайти цю статтю
						Proecting is gone


	два способи реалізувати інтерфейсь
	Агрегація, Наслідування

	ми можемо успадкуватись від класу list і отримати додатковий функціонал
	ми список поміщаємо в середині класу тому в середині класу має бути реалізований інтерфейс для функцій

	Спадкування краще не юзати бо перетягуємо весь інтерфейс
	----------СПАДКУВАННЯ-----------:
		class  MyList(list):

			def sum(self): 				l = MyList([1,2,3])
				s = 0
				for i in self:
					s+=i
				return s
				
			
	------------АГРЕГАЦІЯ-----------:
		class MyList(object):
			"""docstring for MyList"""
			def __init__(self,l=[]):		-> l = MyList([1,2,3])
				self._l = list(l)

			def __len__(self):				-> len(l)
				return len(self._l)

			def __str__(self):				-> str(l)
				return str(self._l)

			def __repr__(self):				-> repr(l)
				return repr(self._l)

			def add(self,value):			->
				self._l.append(value)

			def __setitem__(self,index,value):
				self._l[index] = value

			def __getitem__(self,index):
				if isinstance(index,slice):
					return index(self,_l)
				elif isinstance(index,tuple):
					return[self._l[x] for x in index]
				elif index == Elipsis:
					return self._l.copy()
				else:
					return self._l[index]



				{
					l[1:5] --> slice(1,5,0)
					l[1:5,3:4,5]
					l[...]
					for i in MyList([1,2,3]):
						print i
						{1,2,3}
				}

			def __contains__(self,value):
				return value in self._l

			--------new iterator-------------:
				def __iter__(self):
					return iter(self._l)	-> easy way =)
			--------pichalni iterator-------------:
				def __iter__(self):
					self._i = 0
					return self

				def __next__(self):
					self.i+=1
					if(self.i > len(self._l)):
						raise StopIteration
					return self._l[self.i-1]
						{
							for i in l:
								for j in l:
									print(i,j) 			-> НІХЕРА НЕ ПРАЦЮЄ
						}
			--------good iterator-------------:
				class MyListIterator:
					def __init__(self,l,i=0):
						self.l = l
						self.i = i
					def __iter__(self):	
						return MyListIterator(self.l,self.i)

					def __next__(self):
						self.i+=1
						if self.i > len(self.l):
							raise StopIteration
						return self.l[self.i - 1]


				...
				MyList
				...
				def __iter__(self):
					return MyListIterator(self)
			--------original iterator-------------:
				def f():
					for i in range(5):
						yield i

				g = f()
				for i in g:
					print(i)

				def __iter__(self):
					for i in self._l:
						yield i

				l = [x*x for x in range(5)]
				---------------
				l1 = (x*x for x in range(5)) дозволяе не обчислювати все відразу
					lazy calculation
				
				for i in l1:
					if i>5:
						break
					print (i)

				def f(x,y):
					if x>5:
						return 2*y
					return 0

				f(0,g(...))
	в стандартній бібліотеці пайтон є модуль itertools 
	там є функції і різні способи використання yield
@04/15
======Class (part 3)============================================================================================================================================================================:
	class A:
		
		def __init__(self, arg):
			self.x = 0
	a = A()
	__dict__ =={'x':0}
	a.x = 1
	a.__dict__['x'] = 1

	locals() -> повертає весь локальний контекс
	globals() -> повертає весь глобальний контекст


	коли присвоємо значення викликаєтся
	__setattr__
	[a.x = 1]
			
	коли видаляємо значення викликаєтся
	__delattr__
	[del a.x]
	
	коли отримуємо значення викликаєтся
	__getattribute__
	[a.x]

	-------readOnlyAttr-----:
		Не працюватиме це тому що коли self.x = 0 викликаєтся __setattr__
			class A:
			def __init__(self, arg):
				self.x = 0

			def __setattr__(self,name,value):
				if(name=='x'):
					raise AttributeError('Read_Only_Attr')
				else:
					super().__setattr__(name,value)
		ПРАЦЮЄ
			class A:
			def __init__(self, arg):
				self.x = 0

			def __setattr__(self,name,value):
				if name=='x' and hasattr(self,name):
					raise AttributeError('Read_Only_Attr')
				else:
					super().__setattr__(name,value)

		a = A()
		a.x
		a.x = 1 -> AttributeError('Read_Only_Attr')
		але тепер 
		del a.x 
		a.x = 1 -> все ок =)
		треба ще добавити

			class A:
			def __init__(self, arg):
				self.x = 0

			def __setattr__(self,name,value):
				if name=='x' and hasattr(self,name):
					raise AttributeError('Read_Only_Attr')
				else:
					super().__setattr__(name,value)
			++++++++++++++++++++++++++++++++++++++++++++++++++
			def __delattr__(self,name):
				if name =='x':
					raise AttributeError('Read_Only_Attr')
				else:
					super().__delattr__(name)
	-------приклади використання __getattr__---------------:
		class A:
			def __init__(self):
				self.arg = arg

			def __getattr__(self,name):
				return 42


		class A:
			def m1(self):
				print('A.m1')
			def m2(self):
				print('A.m2')
		class Proxy:
			def __init__(self, arg):
				self.a = A()
			
			def m3(self):
				print('Proxy.m3')
			def __getattr__(self,name):
				return getattr(self.a,name)

		p = Proxy()
		p.m4() -> AttributeError 
		Краще перевірити hasattr чи є такий метод в іншому класі
	-------Patern NullObject-------------:
		class NullObject:
			def __getattr__(self,name):
				return labda *args,**kwargs: None
	--------DESCRIPTOR-----------:
		class Length:
			def __set__(self,obj,value):
				obj._length = value / 1000
			def __get__(self,obj,abjtype):
				return obj._length*1000
		class Line:
			def __init__(self):
				sefl._length = 0
			legth = Length()

		l = Line()
		l.legth = 5
		l.legth 
		class Line:
			def __init__(self):
				super._length = 0
			@property
			def length(self):
			    return self._length*1000
			@length.setter
			def length(self,value):
				self._length = value/1000

	--------Constructor-----------:
		__new__()

		class A:
			def __new__(cls):
				return 42
		a = A()

		>>> a
		>>> 42
		>>> type(a)
		>>> int

		якщо норм тоді
		class A:
			def __new__(cls):
				print('New')
				return suler().__new__(cls)
			def __init__(self):
				print('Init')
		a = A()
		>>> New
		>>> Init

	-----------SingleTone-----------:
		class Singletone:
			def __new__(cls):
				if not hasattr(cls._inst):
					cls._inst = super().__new__(cls)
				return cls._inst
		double checked Singletone
			class  A:
				x = 42



















