#Словари с местоимениями и не только

'''15/02/21 Сюда нужно добавить словарь с ключами {'тема местоимений': "номер местоимений"}
	а так же в дальнейшем список доступних тем для выбора, соответственно, если пользователь перевёл все слова,
	то дальше он может либо продолжить игру, либо остановиться и ещё нужно придумать, как добавить в значение словаря несколько значений'''

#Словарь для сохранения ключей местоимений, которые еще не отгаданы
Pronoun_keys = []

#Темы для перевода
Themes = {
	'Местоимения': 'Pronoun'
}

Views_of_themes_in_pronouns = {
	'Личные': 'Personal_propouns', 
	'Притяжательные': 'Possessive_propouns', 
	'Притяжательные абсолютной формы': 'Possessive_propouns_ofthe_absolute_form', 
	'Указательные': 'Demonstrative_propouns', 
	'Возвратные': 'Reflexive_propouns', 
	'Вопросительные': 'Interrogative_propouns', 
	'Отрицательные': 'Negative_propouns'
}

#Список главных тем для выбора
topics = [
'Местоимения',
]

#Словари с местоимениями:

#Личные местоимения
Personal_propouns = {
	'I': 'Я', 
	'You': 'Ты',
	'He': 'Он',
	'She': 'Она',
	'It': 'Оно'
}

#Притяжательные местоимения
Possessive_propouns = {
	'My': 'Мой',
	'Your': 'Твой',
	'His': 'Его',
	'Her': 'Её',
	'Its': 'Его/Её для неодуш',
	'Our': 'Наш',
	'Your': 'Ваш',
	'Their': 'Их'
}


#Притяжательные местоимения абсолютной формы
Possessive_propouns_ofthe_absolute_form = {
	'Mine':'Мой',#(Моё/Моя/Мои)
	'Yours':'Твой',#(Твоя/Твоё/Твои)
	'His': 'Его',
	'Hers': 'Её',
	'Its': 'Его',#(/Её - для неодушевленных)
	'Ours':'Наш',#(Наша/Наши/Наше)
	'Yours': 'Ваш',#(Ваша/Ваше/Ваши)
	'Theirs': 'Их'
}



#Указательные местоимения
Demonstrative_propouns = {
	'This': 'Этот',#(Эта/То)
	'That': 'Тот',#(Та/То)
	'These': 'Эти',
	'Those': 'Те',
	'Such': 'Такой'
}


#Возвратные местоимения
Reflexive_propouns = {
	'Myself': 'Себя',#(Сам/Собой)
	'Yourself': 'Себя',#(Собой/Сам)
	'Himself': 'Сам',#(Само)
	'Herself': 'Сама',
	'Ourselfs': 'Себя',#(Собой/Сами)
	'Yourself': 'Себя',#(Сами/Собой)
	'Themselves': 'Себя'#(Собой/Сами)
}

#Вопросительные местоимения
Interrogative_propouns = {
	'Who': 'Кто?',
	'What': 'Что?',
	'Where': 'Где?',#(/Куда)
	'Why': 'Почему?',
	'How': 'Как?',
	'Which': 'Который?',
	'Whose': 'Чей'
}


#Отрицательные местоимения
Negative_propouns = {
	'No': 'Никакой',
	'Nothing': 'Ничего',#(/Нечто)
	'Nobody': 'Никто',
	'No one': 'Никто',
	'None': 'Ни один из',
	'Neither': 'Ни тот, ни другой'#(Ни один/Никто) 
}

#Cписок для добавления выбранных словарей
Choises_dicts_theme = [Personal_propouns, Possessive_propouns, Possessive_propouns_ofthe_absolute_form, Demonstrative_propouns, \
Reflexive_propouns, Interrogative_propouns, Negative_propouns]