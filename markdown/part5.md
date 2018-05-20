# Hands on Lab 4
![remote](images/Remote.jpg)

<small>[*mjms.net](http://www.mjms.net/blog/5-tips-for-managing-remote-workers/)</small>
## Praca zespołowa

!SUB
### Widelce

[data-science-ipython-notebooks](https://code.cis.gov.pl/developerscis/data-science-ipython-notebooks)

![github fork](images/github-fork.gif)

<small>[*github.com/diy](https://github.com/diy/open-sourcerer/blob/master/script.md)</small>

!SUB
### Klonowanie

_**git clone**_ - Klonuje / tworzy kopię zdalnego repozytorium lokalnie

Klonowanie istniejącego repozytorium (SSH):

```
git clone git@code.cis.gov.pl:<username>/data-science-ipython-notebooks.git
```

Klonowanie istniejącego repozytorium (HTTPS):

```
git clone https://code.cis.gov.pl/<username>/data-science-ipython-notebooks.git
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
cd data-science-ipython-notebooks
git remote -v
```

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

!SUB
### Feature branch

Przygotowujemy środowisko - ładujemy anaconda

Przykład dla linux-a i miniconda:
```
. ~/Anaconda3/bin/activate
```

Tworzymy gałąź na poprawki które przygotowujemy do włączenia do *upstream*

```bash
git checkout -b excercise
```

Uruchamiamy notebook-a

```
cd <matplotlib|numpy|pandas|scikit-learn|scipy>
jupyter notebook
```

Commit zmian

```
git add <my_notebook>.ipynb
git commit
```

!SUB
### Merge requests

![merge request](images/merge-request.png)

