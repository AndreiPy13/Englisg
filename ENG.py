from choise_theme_of_thegame import ChoiseTheme
from search import SearchWord

Personal_propoun = {
	'I': 'Я', 
	'You': 'Ты',
	'He': 'Он',
	'She': 'Она',
	'It': 'Оно'
}


Possessive_propoun = {
	'My': 'Мой',
	'Your': 'Твой',
	'His': 'Его',
	'Her': 'Её',
	'Its': 'Его/Её для неодуш',
	'Our': 'Наш',
	'Your': 'Ваш',
	'Their': 'Их'
}







def start_game():
	ChoiseTheme().create_new_list_with_pronouns()


start_game()

<<<<<<< HEAD
=======


Pronoun_copy = {
	
}

#Словарь для сохранения ключей местоимений, которые еще не отгаданы
Pronoun_keys = []


Themes = {
	'Местоимения': 'Pronoun'
}

topics = [
'Местоимения',
]

#Выбор случайного местоимения из списка
def number_objects_in_dicst():
	how_obj = len(Pronoun_keys) - 1
	while len(Pronoun_keys) != 0:
		if how_obj == 1:
			return 0
		else:
			return random.randint(0, how_obj)
		break


#Поиск при вводе темы для отгадывания
def search_pronoun(string):
	changed_string =  re.search(r'Мм]естоимения|[Мм]естоимени|[Мм]естоимен|[Мм]естоиме|[Мм]естоим| \
								[Мм]естои|[Мм]есто|[Мм]ест|[Vv]tcnjbvty|[Vv]tcnjbv|[Vv]tcnjb|[Vv]tcnj|[Vv]tcn', \
	 							string) #нужно доработать, потому что слово 'местоывфпаы' тоже пропускает :)
	if changed_string:
		return 'Местоимения'
	else:
		return False


#Проверка темы и создание нового списка местоимений
def create_new_list_with_pronoums():
	if choise_theme_start() == 'Местоимения':
		print('Выбрана тема: Местоимения')
		for pronouns in Pronoun:
			Pronoun_keys.append(pronouns)
		return start_game_propouns()


#Выбор темы для игры
def choise_theme_start():
	start = input('Выберите тему: ').capitalize()
	checking_the_word = search_pronoun(start)
	if checking_the_word in topics:
		name = checking_the_word
		return name
	else: 
		print('Такой темы нет, попробовать снова?')
		choise = input('Да/Нет:? ').capitalize()
		if choise == 'Да':
			return choise_theme_start()
		elif choise == 'Нет':
			return print('До встречи :)')
		else:
			return print('Начните заново!')



#Проверка перевода
def start_game_propouns():
	while len(Pronoun_keys) != 0:
		random_propoun = Pronoun_keys[number_objects_in_dicst()]
		question = print('Как переводится местоимение: ' + random_propoun)
		answer = input('Ответ: ').capitalize()
		if answer == Pronoun.get(random_propoun):
			print( '----------------------------' + '\n' +\
				   'Good job, bro!'               + '\n' +\
				   '----------------------------' 
				 )
			Pronoun_keys.remove(random_propoun)
			return start_game_propouns()
		else:
			print('Restart?')
		break
	print("Game over")






create_new_list_with_pronoums()
>>>>>>> 1bf277f9fe2d4d1745de78c53f17e718401fde8b


	
	

















