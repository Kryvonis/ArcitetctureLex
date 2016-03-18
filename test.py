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
get_area(3)