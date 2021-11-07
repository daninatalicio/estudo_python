from training_oo.core import House, Bedroom, Kitchen, Resident, Room, Bathroom


def test_house():
	house = House(number=1, rooms = ['Kitchen','Bathroom','Room'], street='Major Sertório', city='São Paulo', state='SP', zip_code='01222-001')

	assert type(house) == House
	assert house.number == 1
	assert house.street == 'Major Sertório'
	assert house.city == 'São Paulo'
	assert house.state == 'SP'
	assert house.zip_code == '01222-001'


def test_bedroom():
	bedroom = Bedroom(name='quarto_1')

	assert type(bedroom) == Bedroom
	assert bedroom.name == 'quarto_1'
	assert bedroom.light_on == False


def test_bedroom_two():
	bedroom = Bedroom(name='quarto_3')

	assert type(bedroom) == Bedroom
	assert bedroom.name == 'quarto_3'
	assert bedroom.light_on == False

	bedroom.light_on_off()
	assert bedroom.light_on == True

def test_kitchen():
	kitchen = Kitchen(name='cozinha_1')

	assert type(kitchen) == Kitchen
	assert kitchen.name == 'cozinha_1'
	assert kitchen.light_on == False

	kitchen.light_on_off()
	assert kitchen.light_on == True

def test_kitchen_turn_on_off_light():
	kitchen = Kitchen(name='cozinha_1')

	assert type(kitchen) == Kitchen
	assert kitchen.name == 'cozinha_1'
	assert kitchen.light_on == False

	kitchen.light_on_off()
	kitchen.light_on_off()
	kitchen.light_on_off()
	kitchen.light_on_off()
	assert kitchen.light_on == False

def test_resident():
	resident = Resident(name='João', age=35)

	assert type(resident) == Resident
	assert resident.name == 'João'
	assert resident.age == 35

	resident.do_birthday()

	assert resident.age == 35 + 1

def test_room():
	room = Room(name='room_1')

	assert type(room) == Room
	assert room.name == 'room_1'
	assert room.light_on == False

	room.light_on_off()
	assert room.light_on == True

def test_bathroom():
	bathroom = Bathroom(name='bathroom_1')

	assert type(bathroom) == Bathroom
	assert bathroom.name == 'bathroom_1'
	assert bathroom.light_on == False

	bathroom.light_on_off()
	assert bathroom.light_on == True


def test_house_with_rooms():
	bathroom = Bathroom(name='bathroom_1')
	room = Room(name='room_1')
	house = House(number=1, rooms = [bathroom, room], street='Major Sertório', city='São Paulo', state='SP', zip_code='01222-001')

	assert type(house) == House
	assert house.number == 1
	assert house.rooms == [bathroom, room]

def test_house_with_rooms_light_on():
	bathroom = Bathroom(name='bathroom_1')
	room = Room(name='room_1')
	house = House(number=1, rooms = [bathroom, room], street='Major Sertório', city='São Paulo', state='SP', zip_code='01222-001')


	bathroom.light_on_off()
	assert type(house) == House
	assert house.number == 1
	assert house.rooms == [bathroom, room]
	total_rooms_ligth_on = house.get_rooms_with_light_on()
	assert total_rooms_ligth_on == 1