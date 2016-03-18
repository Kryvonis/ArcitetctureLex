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

============================================================================================================================================================================================================

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
======DECORATOR=====================================================================================================================================================================================================

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

======OBSERVER======================================================================================================================================================================================================

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

----------------------------------Event Code----------------------------------------
def event():
	print('Event') #Хід певної фігури 
				   #Повідомити всіх тих хто підписаний на цю подію
	for observer in observers:
		observer()
---------------------------------Register Observers---------------------------------

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



======OBSERVER AND DECORATOR======================================================================================================================================================================================================
def notify(f):
	def wrepper():
		res = f()
		for observer in observers:
			observer()
		return res
	return wrapper


----------------------------------Event Code----------------------------------------
@notify
def event():
	print('Event')

======FILE======================================================================================================================================================================================================


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

-----------------Запис в файл-----------------

f.write('string1\n')

-----------------Читання з файлу-----------------

s = f.read() #Зчитає весь файл в String
s = f.readline() #зчитує порядково (якщо доходимо до кінця то отримуємо порожній рядок)

for line in iter(f.readline(),''):

s = f.read(10)

for line in f:

f.readinto()

f.tell() #вказує де стоїть файловий вказівник
f.seek(pos,0/1/2) #посунути файл вказівник (pos - позиція на яку посунути, 0 - з поточної ,1 - з початку, 2 - з кінця)


-----------------Сontext manamger-----------------
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
#в цьому місці файл закриється 






















































