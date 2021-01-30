import random



Pronoun = {
	'I': 'Я', 
	'You': 'Ты',
	'He': 'Он',
	'She': 'Она',
	'It': 'Оно'
}

Pronoun_answers = []
Pronoun_keys = []


Themes = {
	'Местоимения': 'Pronoun'
}

topics = [
'Местоимения',
]

def number_objects_in_dicst():
	how_obj = len(Pronoun)
	return random.randint(0, how_obj - 1)


def choise_theme_start():
	start = input('Выберите тему: ').capitalize()
	if start in topics:
		name = start
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

def start_game():
	if choise_theme_start() == 'Местоимения':
		print('Выбрана тема: Местоимения')
		for pronouns in Pronoun:
			Pronoun_keys.append(pronouns)
		random_propoun = Pronoun_keys[number_objects_in_dicst()]
		question = print('Как переводится: ' + random_propoun + '?')
		answer = input('Ответ: ')
		if answer == Pronoun.get(random_propoun):
			print('Good job, bro!')
			Pronoun_answers.append(random_propoun)
			
		else:
			print('Restart?')







start_game()
print(Pronoun_answers)
print(Pronoun_keys)

	
	

















