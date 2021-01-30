#откладка кода

import re 


topics = [
'Местоимения',
]

def choise_theme_start():
	start = input('Выберите тему: ').capitalize()
	checking_the_word = search_pronoun(start)
	if checking_the_word in topics:
		name = checking_the_word
	return print(name)


def search_pronoun(string):
	changed_string =  re.search(r'[Мм]естоимения|[Мм]ест|[Местоим]|[Местоиме]|[Местоимен]|[Местоимени]', string)
	if changed_string:
		return 'Местоимения'
	else:
		return False



choise_theme_start()
