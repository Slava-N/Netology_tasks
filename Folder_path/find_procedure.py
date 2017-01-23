import glob
import os.path
import time

migrations = 'Migrations'
files = glob.glob(os.path.join(migrations, '*.sql'))

def search(files, searched_str):
	search_result = []
	for file in files:
		with open(file) as potential_target:
			if searched_str in potential_target.read():
				search_result.append(file)
	return(search_result)

def results(search_result):
	for each_line in search_result:
		print(each_line)
		time.sleep(0.01)
	print('Всего: {}'.format(len(search_result)), sep='\n')

while True:
	searched_str = input('Что Вы хотите найти?\n')
	time.sleep(1)
	search_result = search(files, searched_str)
	results(search_result)
	files = search_result
