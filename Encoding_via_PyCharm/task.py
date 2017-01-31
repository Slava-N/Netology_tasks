import json
import re

countries = {
    'newsafr.json ': ['Африка', 'UTF-8'],
    'newscy.json': ['Кипр', 'KOI8-R'],
    'newsfr.json': ['Франция', 'iso8859_5']
    # 'newsit.json' : ['Италия', 'cp1251']
}


def open_read(file_name, country_encoding):
    with open(file_name, encoding=country_encoding) as json_file:
        region = json.load(json_file)
        new_block = region['rss']['channel']['item']
        newslines_2 = ''
        for each in new_block:
            news_text = each['description']['__cdata']
            news_text_wo_tags = re.sub("<.*>", "", news_text)
            news_text_clean = re.sub(r'[^\w\s]', '', news_text_wo_tags)
            newslines_2 += news_text_clean
    return newslines_2


def split_into_words(newslines_3):
    all_words_1 = []
    for each_word in newslines_3.split():
        all_words_1.append(each_word.strip().lower())
    return all_words_1


def count_words_function(all_words_2):
    count_words_1 = {}
    for every_word in all_words_2:
        if len(every_word) >= 6:
            try:
                count_words_1[every_word] += 1
            except:
                count_words_1[every_word] = 1
    return count_words_1


for each_country in countries.keys():
    newslines = open_read(each_country, countries[each_country][1])
    all_words = split_into_words(newslines)
    count_words = count_words_function(all_words)
    sorted_count_words = sorted(count_words.keys(), key=count_words.__getitem__, reverse=True)
    print('Топ новостных слов для {0}: \n{1}'.format(countries[each_country][0], sorted_count_words[:10]))
    print('\n')
