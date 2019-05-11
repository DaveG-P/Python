# Chapter 9
# Creating a class
class Dog():
	"""A simple attempt to model a dog """
	def __intit__(self, name, age):
		"""Initialize name and age attributes """
		self.name = name
		self.age = age

	def sit(self):
		""" Simulate a dog sitting """
		print(self.name.title() + " is now sitting")

	def roll_over(self):
		"""Simulate rolling over """
		print(self.name.title() + " rolled over")

my_dog = Dog('Willie', 6)
