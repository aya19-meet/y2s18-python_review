class Superhero:
	"""docstring for Superhero"""
	def __init__(self, name, superpower, strength):
		self.name = name
		self.superpower=superpower
		self.strength=strength

	def step2(self):
		print(self.name , self.strength)

	def save_civilian(self):
		work =  int(input("what's the work"))
		if self.strength<work:
			print("superhero is not strong enough")
		self.strength = self.strength-work
aya = Superhero("aya","watching netflix", 25)
aya.step2()
aya.save_civilian()
		