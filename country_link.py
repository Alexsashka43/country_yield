import json
import hashlib


def convert(file):
    list_country = []
    for item in file:
        a = item['name']['common'].replace(' ','_')
        list_country.append(a)
    return list_country


class Country:

    def __init__(self, file=str):
        self.file = file
        with open(self.file) as information:
            self.json_load = json.load(information)
        self.countries = convert(self.json_load)
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        url = 'https://ru.wikipedia.org/wiki/'
        if self.counter == len(self.countries)-1:
            raise StopIteration
        self.counter += 1

        dictionary_countries = {}

        dictionary_countries['name'] = self.countries[self.counter]
        dictionary_countries['link'] = url + self.countries[self.counter]

        return dictionary_countries


dictionary = Country('countries.json')

list_country = []

for items in dictionary:
    list_country.append(items)

with open('name_links.json', 'w', encoding='utf8') as file:
    json.dump(list_country, file, ensure_ascii=False, indent=2)



def open_file(file_i):
    json_file = None
    with open(str(file_i),encoding='utf8') as file_to_hash:
        json_file = json.load(file_to_hash)
    return json_file

def hash_file(object):

    list_country = {}
    counter = 0
    for item in object:
        list_country['name'] = item['name']
        hash_object = hashlib.md5(bytes(str(item['link']), encoding='utf8'))
        list_country['hash_link'] = hash_object.hexdigest()
        yield list_country
        counter += 1
    print(f'всего строк было обработано:{counter}')



file = open_file('name_links.json')

for item in hash_file(file):
    print(item)
