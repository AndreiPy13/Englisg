from search import SearchWord
from proponuns import *
from main_logick import *

class ChoiseTheme():


#Проверка темы и создание нового списка местоимений
	def create_new_list_with_pronouns(self):
		if ChoiseTheme().choise_theme_start() == 'Местоимения':
			print('Выбрана тема: Местоимения')
			#print('Какие местоимения хотетие переводить')
			#propouns_theme = input('Тема:')
            '''15/02/21Тут нужно решить, либо сделать "поиск" по вводу, либо же сразу предлагать доступные темы для ввода и сравнивать по ним.
            Легче будет сразу предлагать темы, а в дальнейшем сделать поиск'''
			for pronouns in Personal_propouns:
				Pronoun_keys.append(pronouns)
			return Logick().start_game_propouns()
		


	#Выбор темы для игры
	def choise_theme_start(self):
		start = input('Выберите тему: ').capitalize()
		checking_the_word = SearchWord().search_pronoun(start)
		if checking_the_word in topics:
			name = checking_the_word
			return name
		else: 
			print('Такой темы нет, попробовать снова?')
			choise = input('Да/Нет:? ').capitalize()
			if choise == 'Да':
				return ChoiseTheme().choise_theme_start()
			elif choise == 'Нет':
				return print('До встречи :)')
			else:
				return print('Некорректное значение ввода. Начните заново!')