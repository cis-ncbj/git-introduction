# Hands on Lab 2
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
git remote add origin git@code.cis.gov.pl:<user>/git_handson.git
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
### Issues

Gitlab posiada wbudowany system "zgłoszeń". Jego podstawowym zadaniem jest śledzenie zgłoszonych błędów.

Sprawdza się jednak równie dobrze jako narzędzie do planowania nowych funkcjonalności czy notatnik.

![gitlab_issues](images/gitlab-issues.png)

!SUB
### Labels

Nasze issues możemy grupować oznaczając je przy pomocy etykiet (labels):

![gitlab_labels](images/gitlab-labels.png)

!SUB
### Kamienie milowe

Milestones pozwalają na grupowanie poszczególnych issues w powiązane grupy. Zyskujemy w ten sposób:

- Łatwe narzędzie do ustalania priorytetów naszych zadań
- Wygodną wizualizację postępów naszej pracy

![gitlab_milestones](images/gitlab-milestones.png)

!SUB
### Markdown

<pre>
Nagłówek H1
===========

Nagłówek H2
-----------

### H3 - Lista numerowana

1. Kursywa: *gwiazdki* lub _podkreślniki_.
2. Wytłuszczenie: **gwiazdki** lub __podkreślinki__.
3. Łączenie kursywy i wytłuszczenia **gwiazdki plus _podkreślniki_**.
4. Przekreślenie: ~~Scratch this~~.

### H3 - Lista nienumerowana

* Lista nienumerowna wykorzystuje `*`, `-` lub `+`
- http://www.ncbj.gov.pl
+ [Odnośnik z nazwą](https://www.ncbj.gov.pl)

### H3 - Bloki kodu

```python
import sys
print(int("123"))
```
</pre>

!SUB
### Markdown

Nagłówek H1
===========

Nagłówek H2
-----------

### H3 - Lista numerowana

1. Kursywa: *gwiazdki* lub _podkreślniki_.
2. Wytłuszczenie: **gwiazdki** lub __podkreślinki__.
3. Łączenie kursywy i wytłuszczenia **gwiazdki plus _podkreślniki_**.
4. Przekreślenie: ~~Scratch this~~.

!SUB
### Markdown

### H3 - Lista nienumerowana

* Lista nienumerowna wykorzystuje `*`, `-` lub `+`
- http://www.ncbj.gov.pl
+ [Odnośnik z nazwą](https://www.ncbj.gov.pl)

### H3 - Bloki kodu

<pre class="python"><code>import sys
print(int("123"))
</code></pre>

!SUB
### Gitlab Markdown

Gitlab stosuje dodatkowy system odnośników:


- `@foo` : użytkownik
- `#123` : issue
- `!123` : merge request
- `$123` : snippet
- `1234567` : commit
- `[file](path/to/file)` : odnośnik do pliku

!SUB
### Odnośniki commit - issue

![gitlab_commit_link](images/gitlab-commit-link.png)<!-- .element width="50%" -->
![gitlab_issue_link](images/gitlab-issue-link.png)<!-- .element width="80%" -->


!SUB
### Ćwiczenia
<!-- .slide: data-background="#f7cd99" data-transition="fade" -->

- Zakładamy min 2 Issue
- Zakładamy min 1 Milestone
- Przypisujemy Issues do Milstone
