# Hands on Lab 4
![remote](images/Remote.jpg)

<small>[*mjms.net](http://www.mjms.net/blog/5-tips-for-managing-remote-workers/)</small>
## Praca zespołowa

!SUB
### Klony

[git-for-scientists](https://code.cis.gov.pl/developerscis/git-for-scientists)

![clones](images/clones.jpg)<!-- .element width="50%" -->


<small>[*Lucasfilm Ltd.](https://www.lucasfilm.com/)</small>

!SUB
### Klonowanie

_**git clone**_ - Klonuje / tworzy kopię zdalnego repozytorium lokalnie

Klonowanie istniejącego repozytorium (SSH):

```
git clone git@code.cis.gov.pl:developerscis/git-for-scientists.git
```

Klonowanie istniejącego repozytorium (HTTPS):

```
git clone https://code.cis.gov.pl/developerscis/git-for-scientists.git
```

Klonowanie istniejącego lokalnego repozytorium:

```
git clone file:///home/mkarpiarz/git/gitdemo.git
```

!SUB
### Śledzenie

Git pozwala na śledzenie zdalnych repozytoriów:

```
git remote --help
```

Podczas operacji `clone` domyślnie dodawane jest zdalne repozytorium `origin`

```
cd git-for-scientists
git remote -v
```

<!--
!SUB
### Śledzenie *upstream*

Możemy śledzić dowolną liczbę zadalnych repozytoriów

```
git remote add upstream \
  git@code.cis.gov.pl:developerscis/data-science-ipython-notebooks
git fetch upstream
git remote
git branch -a
```

![forks](images/forks.png)
-->

!SUB
### Pobieranie zmian

_**git pull**_ - Pobiera zdalne zmiany i integruje je z lokalnym repozytorium

```bash
git pull          # git fetch + git merge
git pull --rebase # git fetch + git rebase
```

* W rzeczywistości synchronizacja z zdalnym repozytorium przebiega dwu etapowo:
  * Pobieramy aktualny stan zdalnego repozytorium: _**git fetch**_
  * Dołączamy zmiany do lokalnej gałęzi: `git merge` lub `git rebase`

![pull](images/pull.jpg)

<small>[*stackexchange](https://physics.stackexchange.com/questions/133614/the-best-way-in-which-a-man-can-pull-a-train)</small>

<!--
!SUB
### Pobieranie zmian z *upstream*

- Należy zadbać aby wszystkie nasze zmiany były z-commit-owane
- Pobieramy zmiany z repozytorium *upstream* z gałęzi *master*

```bash
git pull upstream master
```

- Często lepszym rozwiązaniem jest *rebase*

```bash
git pull --rebase upstream master
```
-->

!SUB
### Feature branch

Tworzymy gałąź na poprawki które przygotowujemy do włączenia do *upstream*

```bash
git checkout -b <username>
```

* Zapoznajmey się z `Main.md`
* Wybieramy jeden z "rozdziałów"
* Edytujemy plik rozdziału zgodnie z zawartym __TODO__

```
git add <rozdział>.md
git commit
```

!SUB
### Feature branch

Wysyłamy nową gałąź do repozytorium zdalnego:

```
git push -u origin <username>
```

!SUB
### Merge requests

![merge request](images/merge-request.png)


!SUB
### Merge requests

* Każdy zostanie przypisany do jednego MR
* Każdy dodaje min jeden komentarz dotyczący konkretnej linii kodu widocznej w "changes"

![comments](images/comments.png)
