import json
from pprint import pprint

DATA = [
    {
        "imię": "Filemon",
        "gatunek": "Kot",
        "waga": 1,
        "wiek": 0.5
    },
    {
        "imię": "Szarik",
        "gatunek": "Pies",
        "waga": 30,
        "wiek": 2
    }
]

def display(data, select=None):
    if select is not None:
        _data = [_animal for _animal in data if _animal["wiek"]>select]
    else:
        _data = data
    pprint(_data)

def read(file_name):
    _file = open(file_name)
    _data = json.load(_file)
    _file.close()
    return _data

print("Git Handson")
_data1 = read("data.json")
_data2 = read("data2.json")
_data1.extend(_data2)
print("NO FILTER")
display(_data1)
print("WITH FILTER")
display(_data1, 1)
