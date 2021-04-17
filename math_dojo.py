class MathDojo:
	def __init__(self): 
		self.result = 0

	def add(self, *num): 
		for i in range(0, len(num)):
			if type(num[i]) is list or type(num[i]) is tuple:
				for j in num[i]: 
					self.result += j
			else:
				self.result += num[i]
		return self
	def subtract(self, *num): 
		for i in range(0, len(num)):
			if type(num[i]) is list or type(num[i]) is tuple:
				for j in num[i]: 
					self.result -= j
			else:
				self.result -= num[i]
		return self

	def resultado(self): 
		return self.result

# md = MathDojo().add(2).add(2,5,1).subtract(3,2).resultado()
md2 = MathDojo().add([2,3,4]).add(2,5,1).subtract(3,[3,4]).resultado()
# md3 = MathDojo().add([2,2],[5,3]).add(2,5,(1,2,3)).subtract(3,2,(1,2,3)).resultado()


print(md2)
    


