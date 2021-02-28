#откладка кода

import re 

Views_of_themes_in_pronouns = {
	'Личные': 'Personal_propouns', 
	'Притяжательные': 'Possessive_propouns', 
	'Притяжательные абсолютной формы': 'Possessive_propouns_ofthe_absolute_form', 
	'Указательные': 'Demonstrative_propouns', 
	'Возвратные': 'Reflexive_propouns', 
	'Вопросительные': 'Interrogative_propouns', 
	'Отрицательные': 'Negative_propouns'
}

topics = [
'Местоимения',
]

print(type(Views_of_themes_in_pronouns))
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



#choise_theme_start()


