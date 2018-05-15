# Hands on Lab 3
![remote](images/Remote.jpg)

<small>[*mjms.net](http://www.mjms.net/blog/5-tips-for-managing-remote-workers/)</small>
## Repozytoria zdalne

!SUB
### GitLab

[gitlab.com](https://gitlab.com)

![gitlab](images/gitlab-logo.png)

GitLab to platforma pracy grupowej dostępna na licencji open source. Udostępnia zarządcę repozytoriów git, system ticketów, narzędzia do recenzji kodu i wiele więcej. Dostępny w 3 wersjach:
 * GitLab CE: Community Edition - [code.cis.gov.pl](https://code.cis.gov.pl)
 * GitLab EE: Enterprise Edition
 * GitLab.com - darmowa dla małych projektów, udostępnia prywatne repozytoria

!SUB
### Inne platformy

[github.com](https://github.com)

![github](images/Octocat.png)

Największa platforma pracy grupowej udostępniająca repozytoria git. Darmowy dla projektów opensource.

[bitbucket.org](https://bitbucket.org)

![bitbucket](images/bitbucket.png)

Kolejna platforma z repozytoriami git. Darmowy dla projektów opensource oraz małych zespołów (do 5 osób)

!SUB
### Visual Studio Code + Git

![VSC init](images/vsc-init.png)

!SUB
### Visual Studio Code + Git

![VSC commands](images/vsc-git-commands.png)

!SUB
### Visual Studio Code + Git

![VSC commands](images/vsc-ignore.png)

!SUB
### Visual Studio Code + Git

![VSC commands](images/vsc-history.png)

!SUB
### [https://code.cis.gov.pl/projects/new](https://code.cis.gov.pl/projects/new)

![new repo](images/gitlab-new-repo.png)

!SUB
### Wrzucamy testowe repozytorium na [code.cis.gov.pl](https://code.cis.gov.pl)

- Commit zmian
- Dołączamy zdalne repozytorium zgodnie z podpowiedzią GitLab

```
git remote add origin git@code.cis.gov.pl:<user>/git_ex1.git
git checkout master
git push -u origin master
```

- Oglądamy nasze commit-y na [code.cis.gov.pl](https://code.cis.gov.pl)


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
  * Dołączamy zmiany do lokalnej gałęzi: `git merge` lub `git rebase

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
. ~/miniconda3/bin/activate
conda create --name <myenv>
source activate <myenv>
conda install matplotlib pandas scipy statmodels seaborn scikit-learn
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
### Wysyłanie zmian

_**git push**_ - Wysyła zmiany z lokalnego do zdalnego repozytorium

```
git push
```

Domyślnie git clone konfiguruje gałąź główną (*master*) aby śledziła zdalną gałąź główną (*origin/master*).

![push](images/push.png)

<small>[*hikaruzone.wordpress.com](https://hikaruzone.wordpress.com/2015/10/06/in-case-of-fire-1-git-commit-2-git-push-3-leave-building/)</small>

!SUB
### Merge requests

![merge request](images/merge-request.png)

