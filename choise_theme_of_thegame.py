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
			else:
				print('Такой темы не существует, попробуйте снова.')
				return ChoiseTheme().create_new_list_with_pronouns()
#проблема в том, что сюда Views_of_themes_in_pronouns.get(list_for_game) попадает название словаря, но Python его не видет. Нужно использовать список
			choise_dict_pronouns = Views_of_themes_in_pronouns.get(list_for_game)
			number_of_theme = Choises_dicts_theme.index(choise_dict_pronouns)
			for words in Choises_dicts_theme[number_of_theme]:
				print(choise_dict_pronouns)
				Pronoun_keys.append(words)
			return Logick().start_game_propouns()
#Попробавл использовать list - не получилось :D Нужно как-то иначе думать логику
	
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