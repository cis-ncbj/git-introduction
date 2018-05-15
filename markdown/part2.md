# Hands on Lab 2
![repository](images/git-history.png)

<small>[*medium.freecodecamp.org](https://medium.freecodecamp.org/understanding-git-for-real-by-exploring-the-git-directory-1e079c15b807)
## Praca z gałęziami

!SUB
### Gałęzie

![branches](images/branches.svg)<!-- .element width="70%" -->

<small>[*atlassian.com](https://www.atlassian.com/git/tutorials)</small>

!SUB
### Zadanie 8 [4]

Ponieważ dodajemy do programu kompletnie nowe funkcjonalności, dobrze jest w tym momencie utworzyć nowy branch, w którym będziemy dokonywali zmian niezależnie od mastera.

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
### Zadanie 8 [4]
<!-- .slide: data-background="#f7cd99" data-transition="fade" -->

**Rozwiązujemy zadanie 8 [4]**

!SUB
### Zapisujemy zmiany
<!-- .slide: data-background="#bed3f4" data-transition="fade" -->

```
git add vects_from_file.py
git commit
git status
```

!SUB
### Zapisujemy zmiany

![VSC_branch](images/vscode-git-add.png)
![VSC_branch](images/vscode-commit.png)

!SUB
### Praca z gałęziami
<!-- .slide: data-background="#bed3f4" data-transition="fade" -->

```
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
### Zadania 9 - 13 [5,6,7 - master]
<!-- .slide: data-background="#f7cd99" data-transition="fade" -->

* Zadanie 9 - 11 rozwiązujemy w gałęzi **feature**
* Zadanie 12 - 13 rozwiązujemy w gałęzi **master**

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
### Testujmy merge i rebase

Przygotujemy dwie nowe gałęzie *master_rebase* i *master_merge* do testów:
* master pozostaje bez zmian
* master_rebase i master_merge będą symulować zmiany dokonane w gałęzi master
* na master_rebase wykonamy rebase
* na master_merge wykonamy merge

```
git checkout master

git checkout -b master_rebase
echo "TO JEST NOWY PLIK" >> nowy_plik.txt
git commit -a

git chekout -b master_merge
gitk --all
```

!SUB
### Fast forward

**Fast Forward** występuje wtedy gdy zmiany z gałęzi możemy *czysto* nałożyć na aktualną.

Będąc w gałęzi master wykonujemy *merge* zmian z gałęzi feature

```
git checkout master
git merge feature
gitk --all
```

!SUB
### Merge

Będąc w gałęzi **master_merge** wykonujemy *merge* zmian z gałęzi **feature**

```
git checkout master_merge
git merge feature
gitk --all
```

!SUB
### Rebase

Będąc w gałęzi **feature** wykonujemy *rebase* zmian z gałęzi **master_rebase**

```
git checkout feature
git rebase master_rebase
gitk --all
```

Będąc w gałęzi **master_rebase** wykonujemy *merge* zmian z gałęzi **feature**

```
git checkout master_rebase
git merge feature
gitk --all
```

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
