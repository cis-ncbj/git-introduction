# Hands on Lab 1
![helloworld](images/helloworld.png)
## Podstawy git-a

!SUB
### Żargon

Na potrzeby tej prezentacji będziemy korzystać z wyrażeń takich jak:

* *tree/drzewo* - całość historii zmian w repozytorium git
* *branch/gałąź* - odgałęzienia w historii zmian
* *commit* - pojedyncza zmiana (może obejmować wiele plików)
* *merge* - łączenie gałęzi

!SUB
### Git
* Git jest systemem *rozproszonym* - repozytorium znajduje się lokalnie na dysku komputera każdego użytkownika i na dysku zapisywane są commity; można (i najczęściej tak się robi) przechowywać zmiany także w repozytorium zdalnym (np. na innym centralnym komputerze).
* Git przechowuje pliki jako *obiekty* (blob, branch, tree).
* Git przechowuje *snapshot* pliku, a nie tylko różnicę względem poprzedniej wersji.
* W Git pojawia się koncepcja *indeksu*, w którym pliki lądują przed wypchnięciem commitu.

Literatura:
* "Pro Git", S.Chacon and B.Straub, http://git-scm.com/book
* "Git in Practice", M.McQuaid
* http://git-scm.com/docs
* https://www.atlassian.com/git/tutorials

!SUB
### Konfiguracja

Git wymaga aby zdefiniować kim jesteśmy - wszystkie zmiany mają konkretnego autora ;)

* globalną konfigurację (dla wszystkich repozytoriów na danej maszynie) można zmienić poleceniami:

```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

* lub edytując plik `~/.gitconfig`

* konfigurację globalną sprawdzamy poleceniem:

```
git config --global --list
```


!SUB
### Konfiguracja repozytorium
<!-- .slide: data-background="#c6e0a3" data-transition="fade" -->

Lokalną konfigurację (dla danego repozytorium) można zmienić poleceniami:

```
git config user.name "Your Name"
git config user.email "you@example.com"
```

* lub edytując plik `.git/config` w danym repozytorium

* konfigurację lokalną sprawdzamy poleceniem:

```
git config --local --list
```

!SUB
### Otwieramy projekt
<!-- .slide: data-background="#bed3f4" data-transition="fade" -->

```bash
mkdir git_handson
cd git_handson
```

!SUB
### Otwieramy projekt (workspace)

![VSC start](images/vscode-workspace-start.png)

!SUB
### Nowe repozytorium
<!-- .slide: data-background="#bed3f4" data-transition="fade" -->
_**git init**_ - inicjalizacja repozytorium

W bieżacym katalogu:

```bash
git init
```

Lub inicjujemy **oraz** tworzymy katalog jednocześnie:

```bash
git init second_project
cd second_project
```

Powinien pojawić się nowy ukryty katalog `.git`, który zawiera lokalne repozytorium (*local repository*) naszego kodu.

```
ls -a
```

!SUB
### Nowe repozytorium

![VSC start](images/vsc-init.png)

!SUB
### Trójpolówka ;)
![Git Areas](images/areas.png)

<small>[*git-scm.com](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)</small>

!SUB
### Dodawanie plików do repozytorium
<!-- .slide: data-background="#bed3f4" data-transition="fade" -->

Dodajmy do repozytorium pusty plik *main.py*

_**git status**_ - sprawdzamy aktualny stan naszego repozytorium:

```bash
git status
```

_**git add**_ - dodajmy nowe pliki do *indeksu*:

```bash
git add main.py
git status
```

Możemy dodać wiele plików:

```bash
git add *.py
```

!SUB
### Dodawanie plików do repozytorium

![VSC commands](images/vscode-git-add.png)
![VSC commands](images/vscode-git-add-all.png)

!SUB
### Git add

![merge](images/git-flow.png)

<small>[*unwiredlearning](https://unwiredlearning.com)</small>

!SUB
### .gitignore
<!-- .slide: data-background="#bed3f4" data-transition="fade" -->

* zawiera listę plików z katalogu roboczego, które będą ignorowane przy wykonywaniu `git add` czy `git status`
* `.gitignore` jest dodawany do katalogu roboczego i traktowany jak każdy inny plik, tj. podlega śledzeniu zmian; należy więc dodać go do commitu (najlepiej na samym początku pracy z projektem)

```
# no .a files
*.a

# but do track lib.a, even though you're ignoring .a files above
!lib.a

# only ignore the root TODO file, not subdir/TODO
/TODO

# ignore all files in the build/ directory
build/

# ignore doc/notes.txt, but not doc/server/arch.txt
doc/*.txt

# ignore all .txt files in the doc/ directory
doc/**/*.txt
```

Przykładowe pliki .gitignore: https://github.com/github/gitignore

!SUB
### .gitignore

![VSC commands](images/vscode-gitignore.png)

!SUB
### Zapisujemy zmiany
<!-- .slide: data-background="#bed3f4" data-transition="fade" -->

_**git commit**_ - zapisujemy zmiany:

```bash
git commit
```

lub

```bash
git commit -m "<Commit message>"
```

commit "na skróty"

(dodaje wszystkie pliki z katalogu roboczego do indeksu i robi commit):

```bash
git commit -a -m "<Commit message>"
```

Commity powinny być:

* nieduże i częste
* dobrze opisane

!SUB
### Zapisujemy zmiany

![VSC commands](images/vscode-commit.png)

!SUB
### Visual Studio Code + Git
<!-- .slide: data-background="#c6e0a3" data-transition="fade" -->

![VSC commands](images/vsc-git-commands.png)

!SUB
### Git commit

![merge](images/git-flow.png)

<small>[*unwiredlearning](https://unwiredlearning.com)</small>

!SUB
### Praca z kodem 1
<!-- .slide: data-background="#f7cd99" data-transition="fade" -->

* Dodajemy plik *README.md* z opisem naszych ćwiczeń
* W pliku *main.py* dodajemy instrukcję wypisania na ekran

```
print("Git Handson")
```

!SUB
### Dodajemy zmiany do repozytorium
<!-- .slide: data-background="#bed3f4" data-transition="fade" -->

Dodajemy wybrane zmiany do indeksu:

```bash
git status

git add README.md
git add main.py

git status
```

!SUB
### Dodawanie plików do repozytorium

![VSC commands](images/vscode-git-add.png)

!SUB
### git status
<!-- .slide: data-background="#bed3f4" data-transition="fade" -->

Przykład repozytorium z plikami w różnym stanie
```bash
$ git status -s
MM README.md        #<3>
A  parametry.txt    #<2>
 M main.py          #<1>
 ?? test.txt
```
* `??` - plik nie jest śledzony, ale znajduje się w katalogu roboczym
* `A` - nowy plik został dodany do indeksu
* `M` - zawartość śledzonego pliku została zmodyfikowana
* pierwsza kolumna określa stan pliku w indeksie
* druga kolumna określa stan pliku w katalogu roboczym
  - <1> - plik został zmodyfikowany w katalogu roboczym
  - <2> - plik został dodany do indeksu
  - <3> - plik zawiera zmiany zarówno w katalogu roboczym jak i indeksie (został zmodyfikowany, dodany do indeksu, a potem zmodyfikowany ponownie)

!SUB
### git status

![VSC status](images/vscode-git-status.png)

!SUB
### Historia zmian
<!-- .slide: data-background="#bed3f4" data-transition="fade" -->

_**git log**_ - Wypisuje znane commity

Historia zmian z komentarzami:

```
git log
```

Historia zmian z zawartością:

```
git log -p
```

Historia zmian do wybranego commit-u

```
git log <hash commit-u>
```

!SUB
### Historia zmian

![VSC history](images/vscode-git-history.png)

!SUB
### Praca z kodem 2
<!-- .slide: data-background="#f7cd99" data-transition="fade" -->

W pliku *main.py* definiujemy

* Dane w postaci __globalnej__ listy słowników `DATA` opisujących wybrane obiekty np. zwierzęta
  - Niech każdy z obiektów jest opisany kilkoma atrybutami: `imię`, `gatunek`, `waga`, `wiek`
* Definiujemy funkcję *display* która przyjmuje Dane jako __parametr__ i wypisuje na ekran
* Wywołujemy *display* na końcu main.py

!SUB
### Praca z kodem 2
<!-- .slide: data-background="#f7cd99" data-transition="fade" -->

```
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
```

!SUB
### Co właściwie się zmieniło?
<!-- .slide: data-background="#bed3f4" data-transition="fade" -->

_**git diff**_ - narzędzie do prównywania wersji

Zmiany w katalogu roboczym
```
git diff
```

Zmiany czekające w *indeksie*
```
git diff --cached
```

Zmiany pomiędzy wersjami
```
git diff <hash commit-u A> <hash commit-u B>
```

!SUB
### Co właściwie się zmieniło?

![VSC diff](images/vscode-git-diff.png)

!SUB
### Operacje na plikach
<!-- .slide: data-background="#c6e0a3" data-transition="fade" -->

_**git rm**_ - Usuwa pliki z katalogu roboczego i/lub indeksu

Usuń plik i przygotuj tą zmianę do commit-u
```
git rm full.txt
```

Usuń plik z indeksu ale pozostaw kopię w katalogu roboczym
```
git rm --cached test.txt
```

Zmiana nazwy pliku:

```
git mv pusty.txt nowy.txt
```

albo

```
mv pusty.txt nowy.txt
git add nowy.txt
git rm pusty.txt
```

!SUB
### Git rm/mv

![merge](images/git-flow.png)

<small>[*unwiredlearning](https://unwiredlearning.com)</small>
