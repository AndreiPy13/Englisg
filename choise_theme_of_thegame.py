from search import SearchWord
from lists_and_dict import *
from main_logick import *

class ChoiseTheme():


#Проверка темы и создание нового списка местоимений
	def create_new_list_with_pronouns(self):
		if ChoiseTheme().choise_theme_start() == 'Местоимения':
			print('Выбрана тема: Местоимения')
			print('Какие местоимения хотетие переводить:')
			for type in Views_of_themes_in_pronouns:
				print('* ' + type)
			pronouns_theme = input('Тема: ').capitalize()
			if pronouns_theme in Views_of_themes_in_pronouns:
				list_for_game = pronouns_theme
				print (list_for_game)
			else:
				print('Такой темы не существует, попробуйте снова.')
				return ChoiseTheme().create_new_list_with_pronouns()
#проблема в том, что сюда Views_of_themes_in_pronouns.get(list_for_game) попадает словарь, но Python его не видет
			for pronouns in Views_of_themes_in_pronouns.get(list_for_game):
				Pronoun_keys.append(pronouns)
			return Logick().start_game_propouns()
		


#Выбор темы для игры
	def choise_theme_start(self):
		print('Темы для выбора: ')
		for key in Themes:
			print('- ' + key)
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