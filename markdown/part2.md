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
### [https://code.cis.gov.pl/projects/new](https://code.cis.gov.pl/projects/new)

![new repo](images/gitlab-new-repo.png)

!SUB
### Wrzucamy repozytorium z ćwiczeniami [code.cis.gov.pl](https://code.cis.gov.pl)

- Commit zmian
- Dołączamy zdalne repozytorium zgodnie z podpowiedzią GitLab
- Visual Studio Code jak narazie nie ma interfejsu do dodawania zdalnych repozytorii

```
git remote add origin git@code.cis.gov.pl:<user>/git_ex1.git
git checkout master
git push -u origin master
```

- Oglądamy nasze commit-y na [code.cis.gov.pl](https://code.cis.gov.pl)

!SUB
### Wysyłanie zmian
<!-- .slide: data-background="#bed3f4" data-transition="fade" -->

_**git push**_ - Wysyła zmiany z lokalnego do zdalnego repozytorium

```
git push
```

Domyślnie git clone konfiguruje gałąź główną (*master*) aby śledziła zdalną gałąź główną (*origin/master*).

![push](images/push.png)

<small>[*hikaruzone.wordpress.com](https://hikaruzone.wordpress.com/2015/10/06/in-case-of-fire-1-git-commit-2-git-push-3-leave-building/)</small>

!SUB
### Wysyłamy nową gałąź
<!-- .slide: data-background="#bed3f4" data-transition="fade" -->

```
git checkout feature
git push -u origin feature
```

!SUB
### Wysyłamy nową gałąź

![VSC new repo](images/vscode-branch-push.png)

