from proponuns import *
import random


class Logick():


#Выбор случайного местоимения из списка
	def number_objects_in_dicst(self):
		how_obj = len(Pronoun_keys) - 1
		while len(Pronoun_keys) != 0:
			if how_obj == 1:
				return 0
			else:
				return random.randint(0, how_obj)
			break

'''15/02/21 Здесь нужно заменить имена словарей, которые используются на прямую. Т.к в дальнейшем это будут переменные(Personal_propouns)'''

#Проверка перевода
	def start_game_propouns(self):
		while len(Pronoun_keys) != 0:
			random_propoun = Pronoun_keys[Logick().number_objects_in_dicst()]
			question = print('Как переводится местоимение: ' + random_propoun)
			answer = input('Ответ: ').capitalize()
			if answer == Personal_propouns.get(random_propoun):
				print( '----------------------------' + '\n' +\
					   'Good job, bro!'               + '\n' +\
					   '----------------------------' 
					 )
				Pronoun_keys.remove(random_propoun)
				return Logick().start_game_propouns()
			else:
				print('Restart?')
			break
		print("Game over")