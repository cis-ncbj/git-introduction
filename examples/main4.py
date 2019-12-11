import json

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

def display(data):
    print(data)

def read(file_name):
    _file = open(file_name)
    _data = json.load(_file)
    _file.close()
    return _data

print("Git Handson")
_data1 = read("data.json")
_data2 = read("data2.json")
_data1.extend(_data2)
display(_data1)
