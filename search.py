import re


class SearchWord():

	
#Поиск при вводе темы для отгадывания
	def search_pronoun(self, string):
		changed_string =  re.search(r'[Мм]естоимения|[Мм]естоимени|[Мм]естоимен|[Мм]естоиме|[Мм]естоим| \
									[Мм]естои|[Мм]есто|[Мм]ест|[Vv]tcnjbvty|[Vv]tcnjbv|[Vv]tcnjb|[Vv]tcnj|[Vv]tcn', \
		 							string) #нужно доработать, потому что слово 'местоывфпаы' тоже пропускает, хотя пока может так и надо :)
		if changed_string:
			return 'Местоимения'
		else:
			return False


'''15/02/21 Тут будет поиск по темам местоимений'''


