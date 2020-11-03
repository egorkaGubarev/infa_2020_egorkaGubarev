# 0 - тип объекта star/planet
# 1 - координата х в [px]
# 2 - координата у в [px]
# 3 - скорость vx в [px/с]
# 4 - скорость vy в [px/с]
# 5 - радиус r в [px]
# 6 - масса m в [кг]
# 7 - цвет color в виде (r, g, b)

objects = []

def read_space_objects(input_parameters: str, objects):
	"""
	Считывает данные о космических объектах из файла system.txt
	Вызывает функцию write_space_objects и передает в нее считанные параметры objects
	Возращает обратно список параметров objects
	"""


	with open(input_parameters, 'r') as input_file:
		for line in input_file:
			if len(line.strip()) == 0 or line[0] == '#':
				continue  # пустые строки и строки-комментарии пропускаем
			else:
				objects.append(line)

	return input_parameters, objects


def write_space_objects(output_parameters, objects):
	"""
	Записывает данные полученные из функции read_space_objects в файл space_objects
	и возращает их обратно
	"""

	with open('space_objects.txt', 'w') as output_file:
		for object in objects:
			output_file.write(object)

	return output_parameters.txt, objects


open("system.txt", "r")

read_space_objects('system.txt', objects)
write_space_objects(space_objects.txt, objects)

read_space_objects(space_objects.txt, objects)
write_space_objects(space_objects.txt, objects)

print()
