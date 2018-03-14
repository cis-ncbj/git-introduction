# Hands on Lab 2
![repository](images/git-history.png)

<small>[*medium.freecodecamp.org](https://medium.freecodecamp.org/understanding-git-for-real-by-exploring-the-git-directory-1e079c15b807)
## Praca z gałęziami

!SUB
### Gałęzie

![branches](images/branches.svg)<!-- .element width="70%" -->

<small>[*atlassian.com](https://www.atlassian.com/git/tutorials)</small>

!SUB
### Zadanie

Dodać do naszego repozytorium program generujący tablicę liczb losowych o 100 elementach i wypisujących ich na konsolę.

Ponieważ dodajemy do programu kompletnie nowe funkcjonalności, dobrze jest w tym momencie utworzyć nowy branch, w którym będziemy dokonywali zmian niezależnie od mastera.

_**git checkout**_ - zmienia stan katalogu roboczego na wybraną gałąź

_**git checkout -b**_ - tworzy nową gałąź

```bash
git checkout -b feature
git branch
git status
```

!SUB
### Zadanie

**random_array.py**

```
#!/usr/bin/env python3

import numpy

random_array = numpy.random.uniform(-1, 1, size=100)
print(random_array)
```

Commit

```
git add random_array.py
git commit
git status
```

!SUB
### Praca z gałęziami

```
git status
ls
git checkout master
git status
ls
git diff feature
```

!SUB
### Git - Merge vs Rebase

Załóżmy że gałęzie Feature oraz Master rozjechały się

![merge vs rebase](images/merge_rebase01.svg)<!-- .element width="70%" -->

<small>[*atlassian.com](https://www.atlassian.com/git/tutorials)</small>

Mamy dwie strategie ich połączenia: *merge* albo *rebase*

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
### Rebase

* Przepisuje commity na HEAD gałęzi z którą wykonujemy rebase
  * Zmienione zostają SHA1 commitów (z punktu widzenia git są to nowe byty)
* Każdy z commitów z Feature nakładany jest osobno - rozwiązujemy konflikty pojedyńczo

!SUB
### Rebase

![rebase](images/merge_rebase03.svg)<!-- .element width="80%" -->


<small>[*atlassian.com](https://www.atlassian.com/git/tutorials)</small>

!SUB
### Rebase

Po wykonaniu merge otrzymujemy liniową historię

![merge result](images/merge_rebase04.svg)<!-- .element width="80%" -->

<small>[*atlassian.com](https://www.atlassian.com/git/tutorials)</small>

!SUB
### Git - przepisywanie historii

* `git commit --amend` - umożliwia poprawienie ostatniego wysłanego commitu
* `git rebase` i `git pull --rebase`
* `git cherry-pick`
* `git filter-branch` - pozwala przepisać historię WSZYSTKICH commitów
 <small>stosowane bardzo rzadko i tylko w gardłowych sytuacjach (np. commity zawierały poufne informacje)</small>

#### Uwaga
Dobrą zasadą jest nie podmienianie commitów wysłanych do publicznego repozytorium !!

!SUB
### Wybieranie wisienek

_**git cherry-pick**_ - pozwala dodać pojedynczy commit z innej gałęzi

![cherry pick](images/cherry-pick.png)

<small>[*plasticscm.com](https://www.plasticscm.com/documentation/advanced-version-control-guide.html#cherry-pick)</small>

!SUB
### Testujmy merge i rebase

Przygotujemy gałęzie *master_rebase* i *master_merge* do testów:
* master pozostaje bez zmian
* na master_rebase wykonamy rebase
* na master_merge wykonamy merge

```
git checkout master
git checkout -b master_rebase
echo "Zmiana w master" >> README.md
git commit -a
git chekout -b master_merge
gitk --all
```

!SUB
### Fast forward

Będąc w gałęzi master wykonujemy *merge* zmian z gałęzi feature

```
git chekout master
git merge feature
gitk --all
```

!SUB
### Merge

Będąc w gałęzi master_merge wykonujemy *merge* zmian z gałęzi feature

```
git checkout master_merge
git merge feature
gitk --all
```

!SUB
### Rebase

Będąc w gałęzi feature wykonujemy *rebase* zmian z gałęzi master_rebase

```
git checkout feature
git rebase master_rebase
gitk --all
```

Będąc w gałęzi master_rebase wykonujemy *merge* zmian z gałęzi feature

```
git checkout master_rebase
git merge feature
gitk --all
```