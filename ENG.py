
Pronoun = {
	'I': 'Я', 
	'You': 'Ты',
	'He': 'Он',
	'She': 'Она',
	'It': 'Оно'
}

Themes = {
	'Местоимения': 'Pronoun'
}

topics = [
'Местоимения',
]


def choise_theme_start():
	start = input('Выберите тему: ').capitalize()
	if start in topics:
		name = start
		print('Выбрана тема:' + ' ' + name)
	else: 
		print('Такой темы нет, попробовать снова?')
		choise = input('Да/Нет:? ').capitalize()
		if choise == 'Да':
			return choise_theme_start()
		elif choise == 'Нет':
			return print('Конец игры!')
		else:
			return print('GoodBye :D')


choise_theme_start()






