import urllib.parse
import requests


class ParsedName:

    def __init__(self, name):
        self.parsed_name = self.parse_name(name)
        self.verbatim = self.parsed_name['verbatim']
        self.normalized = self.parsed_name['normalized']
        self.canonical = self.parsed_name['canonicalName']['value']
        self.name_map = {
            'genus': 'genus',
            'specificEpithet': 'species',
            'infragenericEpithet': 'subgenus',
            'infraspecificEpithets': 'infraspecies'
        }
        self.epithets = {
            'genus': {'epithet': '', 'authors': '', 'year': ''},
            'subgenus': {'epithet': '', 'authors': '', 'year': ''},
            'species': {'epithet': '', 'authors': '', 'year': ''},
            'trinomial': {'epithet': '', 'authors': '', 'year': ''},
            'quadrinomial': {'epithet': '', 'authors': '', 'year': ''},
        }
        self.parse_details()
        self.bactera = bool(self.parsed_name['bacteria'])
        self.virus = bool(self.parsed_name['virus'])
        self.surrogate = bool(self.parsed_name['surrogate'])
        self.parser_version = self.parsed_name['parserVersion']

    def parse_name(self, name):
        url = 'http://localhost:4334/api?q=' + \
              urllib.parse.quote(name)
        return requests.get(url).json()['namesJson'][0]

    # TODO: add infraspecies support
    def parse_details(self):
        for key, data in self.parsed_name['details'][0].items():
            if type(data) is not list:
                self.epithets[self.name_map[key]]['epithet'] = data['value']
            else:
                if len(data) > 2:
                    raise Exception('Pentanomial and lower names are not supported.')
                for _, infra in data:
                    pass


if __name__ == '__main__':
    aus = ParsedName('Aus (Rus) bus cus L.')
    print('Genus: ' + aus.epithets['genus']['epithet'])
    print('Genus Author: ' + aus.epithets['genus']['authors'])
    print('Subgenus: ' + aus.epithets['subgenus']['epithet'])
    print('Subgenus Author: ' + aus.epithets['subgenus']['authors'])
    print('Species: ' + aus.epithets['species']['epithet'])
    print('Species Author: ' + aus.epithets['species']['authors'])
    print('Trinomial: ' + aus.epithets['trinomial']['epithet'])
    print('Trinomial Author: ' + aus.epithets['trinomial']['authors'])
    print('Quadrinomial: ' + aus.epithets['quadrinomial']['epithet'])
    print('Quadrinomial Author: ' + aus.epithets['quadrinomial']['authors'])