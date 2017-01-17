import json, yaml, csv
import xml.etree.ElementTree as ET

from pprint import pprint
with open('recipe.txt', encoding='utf-8') as document:
    menu={}
    for line in document:
        dish = line.strip()
        number_of_products = int(document.readline().strip())
        product_items = []
        for product in range(number_of_products):
            raw_line = document.readline().strip().split(' | ')
            product_info = {'product' : raw_line[0], 'quantity' : int(raw_line[1]), 'unit' : raw_line[2]}
            product_items.append(product_info)
        empty_line = document.readline().strip()
        menu[dish] = product_items
print('Меню: \n {}'.format(menu))

#загрузка файла json, созданного в ручном режиме.
with open("recipe_manual.json", encoding='utf-8') as json_file:
    menu_loaded = json.load(json_file)
    pprint(menu_loaded)

#автоматическая выгрузка файла json
with open("recipe_dump.json", 'w', encoding="utf-8") as json_file_write:
    json.dump(menu, json_file_write)

#автоматическая выгрузка файла yaml
with open("recipe_dump.yaml", 'w', encoding="utf-8") as yaml_file_write:
    yaml.dump(menu, yaml_file_write)

#прочтение файла csv
with open('CSV_1.csv') as csvfile:
    csv_read = csv.reader(csvfile, delimiter = ";")
    print(list(csv_read))

#прочтение xml файла, созданного вручную
tree=ET.parse('recipe_manual.xml')
for e in tree.iter():
    if e.attrib:
        print("{0}:{1}".format(e.tag, e.attrib))
    else: print(e.tag, e.text)
