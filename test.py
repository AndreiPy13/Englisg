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


Personal_propouns = {
	'I': 'Я', 
	'You': 'Ты',
	'He': 'Он',
	'She': 'Она',
	'It': 'Оно'
}

topics = [
'Местоимения',
]

Views_of_themes_in_pronouns1 = [Personal_propouns, topics]

#list_for_game = input('Введите тему: ')
#choise_dict_pronouns = Views_of_themes_in_pronouns.get(list_for_game)
#Views_of_themes_in_pronouns1.append(choise_dict_pronouns)
print(Views_of_themes_in_pronouns1[0])
#нужно превратить string в переменную