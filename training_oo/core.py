from typing import List


class Resident:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def do_birthday(self):
		self.age = self.age + 1


class House:

	def __init__(self, rooms: None, number: int, street: str, city: str, state: str, zip_code: str):
		self.number = number
		self.rooms = rooms or []
		self.street = street
		self.city = city
		self.state = state
		self.zip_code = zip_code

	def rooms_names(self):
		return self.rooms

	def get_rooms_with_light_on(self):
		total_rooms_light_on = 0
		for room in self.rooms:
			if room.light_on == True:
				total_rooms_light_on  = total_rooms_light_on  + 1
		return total_rooms_light_on

# função na classe house que vai acender a luz de todos os comodos 
# da casa e o teste tem que criar um monte de comodos, adicionar na casa e dps testa se todas estão acessas
# criar um repositorio no git e colocar o código


class Bedroom:

	def __init__(self, name):
		self.name = name
		self.light_on = False

	def light_on_off(self):
		if self.light_on == True:
			self.light_on = False
		else:
			self.light_on = True


class Kitchen:

	def __init__(self, name):
		self.name = name
		self.light_on = False

	def light_on_off(self):
		if self.light_on == True:
			self.light_on = False
		else:
			self.light_on = True

class Room:

	def __init__(self, name):
		self.name = name
		self.light_on = False

	def light_on_off(self):
		if self.light_on == True:
			self.light_on = False
		else:
			self.light_on = True

class Bathroom:

	def __init__(self, name):
		self.name = name
		self.light_on = False

	def light_on_off(self):
		if self.light_on == True:
			self.light_on = False
		else:
			self.light_on = True