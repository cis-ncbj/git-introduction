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
    if filter is not None:
        _data = [_animal for _animal in data if _animal["wiek"]>select]
    else:
        _data = data
    pprint(_data)

print("Git Handson")
display(DATA, 1)
