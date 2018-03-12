# Hands on Lab 2
![remote](images/Remote.jpg)

<small>[*mjms.net](http://www.mjms.net/blog/5-tips-for-managing-remote-workers/)</small>
## Repozytoria zdalne

!SUB
### GitLab

[gitlab.com](https://gitlab.com)

GitLab to platforma pracy grupowej dostępna na licencji open source. Udostępnia zarządcę repozytoriów git, system ticketów, narzędzia do recenzji kodu i wiele więcej. Dostępny w 3 wersjach:
 * GitLab CE: Community Edition - [code.cis.gov.pl](https://code.cis.gov.pl)
 * GitLab EE: Enterprise Edition
 * GitLab.com - darmowa dla małych projektów, udostępnia prywatne repozytoria

!SUB
### Inne platformy

[github.com](https://github.com)

Największa platforma pracy grupowej udostępniająca repozytoria git. Darmowy dla projektów opensource.

[bitbucket.org](https://bitbucket.org)

Kolejna platforma z repozytoriami git. Darmowy dla projektów opensource oraz małych zespołów (do 5 osób)

!SUB
### Klucze SSH

Najwygodniejszą metodą logowania do zdalnych repozytorii są klucze SSH

Przykład dla usrint.cis.gov.pl

```
ssh-keygen -f ~/.ssh/id_rsa_code
eval $(ssh-agent)
ssh-add ~/.ssh/id_rsa_code
```

!SUB
### [https://code.cis.gov.pl/projects/new](https://code.cis.gov.pl/projects/new)

![new repo](images/gitlab-new-repo.png)

!SUB
### Klonowanie

_**git clone**_ - Klonuje / tworzy kopię zdalnego repozutorium lokalnie

Klonowanie istniejącego repozytorium (SSH):

```
git clone git@code.cis.gov.pl:developerscis/gitdemo.git
```

Klonowanie istniejącego repozytorium (HTTPS):

```
git clone https://code.cis.gov.pl/developerscis/gitdemo.git
```

Klonowanie istniejącego lokalnego repozytorium:

```
git clone file:///home/mkarpiarz/git/gitdemo.git
```

!SUB
### Wysyłanie zmian

_**git push**_ - Wysyła zmiany z lokalnego do zdalnego repozytorium

Wysyłamy lokalne commity:

```
git push
```

Domyślnie git clone konfiguruje gałąź główną (*master*) aby śledziła zdalną gałąź główną (*origin/master*).

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

!SUB
### Śledzenie

Git pozwala na śledzenie zdalnych repozytoriów:

```
git remote --help
```

Podczas operacji `clone` domyślnie dodawane jest zdalne repozytorium `origin`

```
$ git clone git@code.cis.gov.pl:kklimaszewski/gitdemo.git
$ cd gitdemo
$ git remote -v
origin git@code.cis.gov.pl:kklimaszewski/gitdemo.git (fetch)
origin git@code.cis.gov.pl:kklimaszewski/gitdemo.git (push)
```

!SUB
### Śledzenie

Możemy śledzić dowolną liczbę zadalnych repozytoriów

```
$ git remote add upstream git@code.cis.gov.pl:cisdevelopers/gitdemo.git
$ git remote add appserver git@code.cis.gov.pl:webservices/appserver.git
$ git remote
origin
upstream
appserver
```

