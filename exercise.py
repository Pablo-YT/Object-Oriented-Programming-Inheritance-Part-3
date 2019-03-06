class System():
	"""docstring for System"""
	

	def __init__(self):
		self.bodies = []



	def add(self, planet):
		for planet in self.bodies:
			if planet not in self.bodies:
				self.bodies.append(planet)
			else: 
				print("Error cannot add inside body!")
				return self.bodies
		


	def total_mass(self):
		mass = 0
		for x in enumerate(self.bodies):
			mass += body.mass
			return mass

		


class Body(System):
	def __init__(self, name, mass):
		self.name = name 
		self.mass = mass




class planets(Body):
	def __init__(self, name, mass, day, year):
		super().__init__(name, mass)
		self.day = day
		self.year = year
		




class stars(Body):
	def __init__(self, name, mass, type_star):
		super().__init__(name, mass)
		self.type_star = type_star


class moons(Body):
	def __init__(self,name,mass,month,planet):
		super().__init__(name, mass)
		self.month = month
		self.planet = planet



planet1 = planets('Earth', 223, 365, 1)
planet2 = planets('Mars', 210, 425, 2)

star1 = stars('Sun', 1000, 'G-type')
star2 = stars('Stars in the sky', 902, 'D-type star')

moon1 = moons('Moon', 1212, 144, 'Earth')
moon2 = moons('Moons',9821, 245, 'Saturn')

Solar_System = System()
Solar_System.add(planet1)
Solar_System.add(planet2)

Solar_System.add(star1)
Solar_System.add(star2)

Solar_System.add(moon1)
Solar_System.add(moon2)

print(Solar_System)
print(Solar_System.total_mass())
