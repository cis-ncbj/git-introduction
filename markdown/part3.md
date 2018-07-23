# Hands on Lab 3
![repository](images/git-history.png)

<small>[*medium.freecodecamp.org](https://medium.freecodecamp.org/understanding-git-for-real-by-exploring-the-git-directory-1e079c15b807)
## Praca z gałęziami

!SUB
### Gałęzie

![branches](images/branches.svg)<!-- .element width="70%" -->

<small>[*atlassian.com](https://www.atlassian.com/git/tutorials)</small>

!SUB
### Zadania "plots"

Ponieważ dodajemy do programu kompletnie nowe funkcjonalności, dobrze jest w tym momencie utworzyć nowy branch, w którym będziemy dokonywali zmian niezależnie od mastera.

Ogólnie gałęzie przeznaczone do opracowania nowej funkcjinalności nazywamy: _Feature Branches_

!SUB
### Nowa gałąź
<!-- .slide: data-background="#bed3f4" data-transition="fade" -->

_**git checkout**_ - zmienia stan katalogu roboczego na wybraną gałąź

_**git checkout -b**_ - tworzy nową gałąź

```bash
git checkout -b plots
git branch
git status
```

!SUB
### Nowa gałąź

![VSC_branch](images/vscode-git-branch1.png)
![VSC_branch](images/vscode-git-branch2.png)

!SUB
### Zadanie 8
<!-- .slide: data-background="#f7cd99" data-transition="fade" -->

**Rozwiązujemy zadania "plots"**

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
git diff plots
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
### Wysyłamy nową gałąź
<!-- .slide: data-background="#bed3f4" data-transition="fade" -->

```
git checkout plots
git push -u origin plots
```

!SUB
### Wysyłamy nową gałąź

![VSC new repo](images/vscode-branch-push.png)


!SUB
### Zadania "rng" i "dirs"
<!-- .slide: data-background="#f7cd99" data-transition="fade" -->

* Zadania "rng" rozwiązujemy w gałęzi **rng**
* Zadanie "dirs" rozwiązujemy w gałęzi **master**

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
<!-- .slide: data-background="#bed3f4" data-transition="fade" -->

Przygotujemy nowe gałęzie do testów:
* *master_rebase*
* *master_merge*
* *plots_rebase*
* *plots_merge*
* master i plots pozostają bez zmian
* na master_rebase wykonamy rebase
* na master_merge wykonamy merge

```
git checkout master
git checkout -b master_rebase
git chekout -b master_merge
git checkout plots
git checkout -b plots_rebase
git checkout -b plots_merge

gitk --all
```

!SUB
### Testujmy merge i rebase

1. _checkout **master**_
2. _new branch **master_rebase**_
3. _new branch **master_merge**_

![VSC_branch](images/vscode-git-checkout-master.png)
![VSC_branch](images/vscode-git-feature-new-branch.png)

!SUB
### Testujmy merge i rebase

1. _checkout **plots**_
2. _new branch **plots_rebase**_
3. _new branch **plots_merge**_

![VSC_branch](images/vscode-git-checkout-feature.png)
![VSC_branch](images/vscode-git-feature-new-branch.png)

!SUB
### Testujmy merge i rebase

![VSC_branch](images/vscode-merge-test1.png)

!SUB
### Rebase
<!-- .slide: data-background="#bed3f4" data-transition="fade" -->

Będąc w gałęzi **plots_rebase** wykonujemy *rebase* zmian na gałęzi **master_rebase**

```
git checkout plots_rebase
git rebase master_rebase
gitk --all
```

!SUB
### Rebase

![VSC_branch](images/vscode-rebase1.png)
![VSC_branch](images/vscode-rebase2.png)
![VSC_branch](images/vscode-rebase3.png)

!SUB
### Rebase

![VSC_branch](images/vscode-rebase4.png)

!SUB
### Merge
<!-- .slide: data-background="#bed3f4" data-transition="fade" -->

Będąc w gałęzi **master_merge** wykonujemy *merge* zmian z gałęzi **plots_merge**

```
git checkout master_merge
git merge plots_merge
gitk --all
```

!SUB
### Merge

![VSC_branch](images/vscode-merge1.png)
![VSC_branch](images/vscode-merge2.png)
![VSC_branch](images/vscode-merge3.png)

!SUB
### Fast forward
<!-- .slide: data-background="#bed3f4" data-transition="fade" -->

**Fast Forward** występuje wtedy gdy zmiany z gałęzi możemy *czysto* nałożyć na aktualną.

Będąc w gałęzi **master_rebase** wykonujemy *merge* zmian z gałęzi **plots_rebase**

```
git checkout master_rebase
git merge plots_rebase
gitk --all
```

!SUB
### Fast forward

1. _checkout **master_rebase**_
2. _merge **plots_rebase**_

!SUB
### Testujmy merge i rebase
![VSC_branch](images/vscode-merge-test2.png)

!SUB
### Dołączamy zmiany do gałęzi master
<!-- .slide: data-background="#bed3f4" data-transition="fade" -->

Będąc w gałęzi **master** wykonujemy *merge* zmian z gałęzi **plots_rebase**

```
git checkout master
git merge plots_rebase
```

Będąc w gałęzi **rng** wykonujemy *rebase* zmian na gałęzi **master**

```
git checkout rng
git rebase master
```

Będąc w gałęzi **master** wykonujemy *merge* zmian z gałęzi **rng**

```
git checkout master
git merge rng
```

!SUB
### Dołączamy zmiany do gałęzi master

1. _checkout **master**_
1. _merge **plots_rebase**_
1. _checkout **rng**_
1. _rebase **master**_
1. _checkout **master**_
1. _merge **rng**_

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
