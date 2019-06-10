import json
import hashlib
from pprint import pprint


class Country:

    def __init__(self, file_name):
        self.path = file_name
        with open(file_name, encoding='utf8') as read_file:
            data = json.load(read_file)
        self.data = data
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        country_name = self.data[self.counter]['name']['common']
        self.counter += 1
        wiki_link = 'https://wikipedia.org/wiki/' + country_name
        wiki_link = wiki_link.replace(' ', '')
        with open('text.txt', 'a', encoding='utf-8') as fw:
            fw.write(country_name + ' - ' + wiki_link + '\n')
        if self.counter == len(self.data):
            raise StopIteration
        return wiki_link


# for item in Country('countries.json'):
#    pprint(item)

def country(path):
    with open(path, encoding='utf8') as read_file:
        data = json.load(read_file.readline())
        counter = 0
        while counter < len(data):
            result = hashlib.md5(data.encode())
            x = result.hexdigest()
            yield x
            counter =+ 1


for item in country('C:/My documents/iterators/countries.json'):
    pprint(item)