# Hands on Lab 3
![repository](images/git-history.png)

<small>[*medium.freecodecamp.org](https://medium.freecodecamp.org/understanding-git-for-real-by-exploring-the-git-directory-1e079c15b807)
## Praca z gałęziami

!SUB
### Gałęzie

![branches](images/branches.svg)<!-- .element width="70%" -->

<small>[*atlassian.com](https://www.atlassian.com/git/tutorials)</small>

!SUB
### Zadania "odczyt z pliku"

Ponieważ dodajemy do programu kompletnie nowe funkcjonalności, dobrze jest w tym momencie utworzyć nowy branch, w którym będziemy dokonywali zmian niezależnie od mastera.

Ogólnie gałęzie przeznaczone do opracowania nowej funkcjonalności nazywamy: _Feature Branches_

!SUB
### Nowa gałąź
<!-- .slide: data-background="#bed3f4" data-transition="fade" -->

_**git checkout**_ - zmienia stan katalogu roboczego na wybraną gałąź

_**git checkout -b**_ - tworzy nową gałąź

```bash
git checkout -b feature
git branch
git status
```

!SUB
### Nowa gałąź

![VSC_branch](images/vscode-git-branch1.png)
![VSC_branch](images/vscode-git-branch2.png)

!SUB
### Git checkout

![merge](images/git-flow.png)

<small>[*unwiredlearning](https://unwiredlearning.com)</small>

!SUB
### Ćwiczenia (feature)
<!-- .slide: data-background="#f7cd99" data-transition="fade" -->

Dodajemy do pliku *main.py* nową funkcję która odczyta dane z pliku w formacie JSON

* tworzyny nowy plik z danymi `data.json`
  - słownik w formacie JSON wygląda identycznie jak w python
* otwieramy plik przy pomocy `open`
```python
f = open("data.json")
```
* czytamy zawartość przy pomocy `json.load`
```python
import json
data = json.load(f)
```
* modyfikujemy *main.py* aby korzystał z *nowej funkcji* zamiast tablicy `DATA`

!SUB
### Ćwiczenia (feature)
<!-- .slide: data-background="#f7cd99" data-transition="fade" -->

__data.json__

```json
[
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
    },
    {
        "imię": "Szczerbatek",
        "gatunek": "Smok",
        "waga": 1000,
        "wiek": 5
    }
]
```

!SUB
### Zapisujemy zmiany
<!-- .slide: data-background="#bed3f4" data-transition="fade" -->

```bash
git add main.py
git commit
git status
```

!SUB
### Zapisujemy zmiany

![VSC_branch](images/vscode-git-add.png)
![VSC_branch](images/vscode-commit.png)

!SUB
### Ćwiczenia (feature)
<!-- .slide: data-background="#f7cd99" data-transition="fade" -->

* Dodajemy do pliku *main.py* możliwość przeczytania dwóch plików i połączenia danych
* Korzystamy z metody `extend` dostępnej dla obiektów list w python
  - `data.extend(data2)`
* Zapisujemy zmiany jako **commit**.

  Jako komentarz używamy zwrotu **Fix #1**

!SUB
### Wysyłamy nową gałąź
<!-- .slide: data-background="#bed3f4" data-transition="fade" -->

```bash
git checkout feature
git push -u origin feature
```

!SUB
### Wysyłamy nową gałąź

![VSC new repo](images/vscode-branch-push.png)

!SUB
### Git push

![merge](images/git-flow.png)

<small>[*unwiredlearning](https://unwiredlearning.com)</small>


!SUB
### Praca z gałęziami
<!-- .slide: data-background="#bed3f4" data-transition="fade" -->

```bash
git status
ls
git checkout master
git status
ls
git diff feature
```

!SUB
### Praca z gałęziami

![VSC_branch](images/vscode-branch-history.png)

!SUB
### Praca z gałęziami

![VSC_branch](images/vscode-branch-diff1.png)

!SUB
### Praca z gałęziami

![VSC_branch](images/vscode-branch-diff2.png)

!SUB
### Praca z gałęziami

![VSC_branch](images/vscode-branch-diff3.png)

!SUB
### Ćwiczenia (master)
<!-- .slide: data-background="#f7cd99" data-transition="fade" -->

W gałęzi **master**:

* Upiększamy wypisywanie danych: zamieniamy funkcję `print` na `pprint`
```python
from pprint import pprint
pprint(data)
```
* Zapisujemy jako commit

  Jako komentarza używamy zwrotu **Fixes #2**

* Modyfikujemy funkcję `display`
  - przyjmuje dodatkowy parametr `select` z domyślną wartością `None`
  - jeśli parametr został zdefiniowany wyświetla tylko wybrane dane (np. na podstawie wieku)

!SUB
### Git - łączenie gałęzi

Załóżmy że gałęzie Feature oraz Master rozjechały się

![merge vs rebase](images/merge_rebase01.svg)<!-- .element width="70%" -->

<small>[*atlassian.com](https://www.atlassian.com/git/tutorials)</small>

!SUB
### Merge

* Pozostawia commity bez zmian
* Rozwiązywanie konfliktów wykonujemy dla pełnego merge
* Historia repozytorium staje się nieliniowa
* Jeśli repozytoria nie rozjechały się możliwy jest "fast forward"
  * Nowe commity dopisywane są na końcu gałęzi bez dodatkowego commitu "merge"

!SUB
### Merge

![merge](images/merge_rebase02.svg)

<small>[*atlassian.com](https://www.atlassian.com/git/tutorials)</small>

!SUB
### Merge
<!-- .slide: data-background="#bed3f4" data-transition="fade" -->

Będąc w gałęzi **master** wykonujemy *merge* zmian z gałęzi **feature**

```bash
git checkout master
git merge feature
gitk --all
```

!SUB
### Merge

![VSC_branch](images/vscode-merge1.png)
![VSC_branch](images/vscode-merge2.png)
![VSC_branch](images/vscode-merge3.png)

!SUB
### Rozwiązywanie konfliktów

![conflict](images/vscode-conflict.png)

!SUB
### Fast forward
<!-- .slide: data-background="#bed3f4" data-transition="fade" -->

**Fast Forward** występuje wtedy gdy zmiany z gałęzi możemy *czysto* nałożyć na aktualną.

- Zakładamy gałąź *clean*
- Dodajemy do repozytorium nowy plik *clean.txt*
- Wykonujemy **git commit**
- Przechodzimy do gałęzi *master*
- Wykonujemy **git merge clean**

!SUB
### Git - przepisywanie historii
<!-- .slide: data-background="#c6e0a3" data-transition="fade" -->

* `git commit --amend` - umożliwia poprawienie ostatniego wysłanego commitu
* `git rebase` i `git pull --rebase`
* `git cherry-pick`
* `git filter-branch` - pozwala przepisać historię WSZYSTKICH commitów
 <small>stosowane bardzo rzadko i tylko w gardłowych sytuacjach (np. commity zawierały poufne informacje)</small>

#### Uwaga
Dobrą zasadą jest nie podmienianie commitów wysłanych do publicznego repozytorium !!

!SUB
### Wybieranie wisienek
<!-- .slide: data-background="#c6e0a3" data-transition="fade" -->

_**git cherry-pick**_ - pozwala dodać pojedynczy commit z innej gałęzi

![cherry pick](images/cherry-pick.png)

<small>[*plasticscm.com](https://www.plasticscm.com/documentation/advanced-version-control-guide.html#cherry-pick)</small>

!SUB
### Rebase
<!-- .slide: data-background="#c6e0a3" data-transition="fade" -->

* Przepisuje commity w gałęzi od nowa
* Komity w gałęzi stają się dziećmi **HEAD** gałęzi master
* Rozwiązywanie konfliktów wykonujemy dla każdego z commitów
* Historia repozytorium pozostaje liniowa

!SUB
### Rebase
<!-- .slide: data-background="#c6e0a3" data-transition="fade" -->

![merge](images/merge_rebase03.svg)<!-- .element width="70%" -->


<small>[*atlassian.com](https://www.atlassian.com/git/tutorials)</small>

!SUB
### Rebase
<!-- .slide: data-background="#c6e0a3" data-transition="fade" -->

![merge](images/merge_rebase04.svg)<!-- .element width="70%" -->

<small>[*atlassian.com](https://www.atlassian.com/git/tutorials)</small>


!SUB
### Ćwiczenie Rebase
<!-- .slide: data-background="#c6e0a3" data-transition="fade" -->

Cofamy merge w gałęzi master

```bash
git reset --hard HEAD^
```

Uwaga!!! `git reset --hard` usuwa pliki

!SUB
### Git Reset
<!-- .slide: data-background="#c6e0a3" data-transition="fade" -->

![reset](images/reset.jpg)<!-- .element width="70%" -->

<small>[*blog.nakulrajput.com](https://blog.nakulrajput.com/git-reset/)</small>

!SUB
### Ćwiczenie Rebase
<!-- .slide: data-background="#c6e0a3" data-transition="fade" -->

Będąc w gałęzi **feature** wykonujemy *rebase* zmian na **HEAD** gałęzi **master**

```bash
git checkout feature
git rebase master
gitk --all
```

Dla każdego commitu z gałęzi **feature** rozwiązujemy konflikty jeśli istnieją

!SUB
### Ćwiczenie Rebase
<!-- .slide: data-background="#c6e0a3" data-transition="fade" -->

![VSC_branch](images/vscode-rebase1.png)
![VSC_branch](images/vscode-rebase2.png)
![VSC_branch](images/vscode-rebase3.png)
![VSC_branch](images/vscode-rebase4.png)
