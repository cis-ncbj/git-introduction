# Hands on Lab 1
![helloworld](images/helloworld.png)
## Podstawy git-a

!SUB
### Żargon

* Na potrzeby tej prezentacji będziemy korzystać z wyrażeń takich jak:
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
### Nowe repozytorium
_**git init**_ - inicjalizacja repozytorium

W bieżacym katalogu:

```bash
git init
```

W katalogu o zadanej nazwie:

```bash
git init git_ex1
cd git_ex1
```

Powinien pojawić się nowy ukryty katalog `.git`, który zawiera lokalne repozytorium (*local repository*) naszego kodu.

!SUB
### Trójpolówka ;)
![Git Areas](images/areas.png)

<small>[*git-scm.com](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)</small>

!SUB
### Dodawanie plików do repozytorium

Posłużymy się przykładem "Hello World" w python.

```bash
cat << EOF > README.md
# Hello World
Przykład wykorzystania print w python3
EOF
cat << EOF > hello_world.py
#!/usr/bin/env python3
print("Hello World")
EOF
touch pusty.txt
touch full.txt
```

_**git status**_ - sprawdzamy aktualny stan naszego repozytorium:

```bash
git status
```

_**git add**_ - dodajmy nowe pliki do *indeksu*:

```bash
git add README.md
git add hello_world.py
git add pusty.txt
git add full.txt
git status
```

!SUB
### .gitignore

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
### Zapisujemy zmiany

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

* Commity powinny być:
  * nieduże i częste
  * dobrze opisane

!SUB
### Praca z kodem

Dodajemy nowe pliki i modyfikujemy stare:

```bash
touch test.txt
touch test2.txt
echo "Nowa linia" >> README.md
echo "print(\"HELLO2\")" >> hello_world.py
echo "Nie pusty" >> pusty.txt
```

Dodajemy zmiany do indeksu:

```bash
git add README.md
git add hello_world.py
git add test.txt
```

Wprowadzamy kolejne modyfikacje:

```
echo "Nowa linia 2" >> README.md
```

Sprawdzamy status:

````
git status -s
```

!SUB
### git status

Przykład repozytorium z plikami w różnym stanie
```bash
$ git status -s
MM README.md       #<3>
M  hello_world.py  #<2>
 M pusty.txt       #<1>
 A  test.txt
 ?? test2.txt
```
* `??` - plik nie jest śledzony, ale znajduje się w katalogu roboczym
* `A` - nowy plik został dodany do indeksu
* `M` - zawartość śledzonego pliku została zmodyfikowana
* pierwsze dwie kolumny określają stan danego pliku z punktu widzenia katalogu roboczego i indeksu
  * <1> - plik został zmodyfikowany w katalogu roboczym
  * <2> - plik został dodany do indeksu i zmodyfikowany
  * <3> - plik zawiera zmiany zarówno w katalogu roboczym jak i indeksie (został zmodyfikowany, dodany do indeksu, a potem zmodyfikowany ponownie)

!SUB
### Co właściwie się zmieniło?

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
### Historia zmian

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
### Operacje na plikach

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
