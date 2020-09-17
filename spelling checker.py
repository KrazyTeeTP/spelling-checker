from textblob import TextBlob

names = ['psswrd', 'impot', 'corect']
to_correct_list = []

for name in names:
	to_correct_list.append(TextBlob(name))

for word in to_correct_list:
	print(word.correct())