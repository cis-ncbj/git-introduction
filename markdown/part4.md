# Git workflows
![teamwork](images/teamwork.jpg)<!-- .element width="40%" -->

<small>[*pinterest.com](https://pl.pinterest.com/pin/139400550939304902/)
## Praca zespołowa

!SUB
### Zespół jednoosobowy ;-)

Pracuje samodzielnie nad projektem.

**Po co mi Git?**

* Backup
* Przenośność między maszynami
* Prostota udostępnienia innym poprzez GitHub, GitLab etc.

![basic workflow](images/basic.png)

<small>[*buddy.works](https://buddy.works/blog/5-types-of-git-workflows)

!SUB
### Praca w zespole

* Istnieje wiele modeli pracy zespołowej w oparciu o git:
  * Git Flow
  * Feature Branch
  * GitHub Flow
  * Forking Flow

!SUB
### Praca w zespole

Wspólne cechy wszystkich *Flow:

* Jedna gałąź jest uznawana za **stabilną**
  - Kod który tu ląduje **musi** być działający i gotowy do wykorzystania
  - Często będzie automatycznie wysyłany do środowiska produkcyjnego
* Prace rozwojowe wykonujemy w **gałęziach**
* Operacje merge poprzedzone są **recenzją** kodu

!SUB
### Feature Branch / GitHub workflow

_**HEAD**_ gałęzi _**master**_ zawsze jest działającą aplikacją

_**Każda**_ zmiana zaczyna się od utworzenia nowej gałęzi

![branch workflow](images/feature-branch.png)

<small>[*buddy.works](https://buddy.works/blog/5-types-of-git-workflows)


!SUB
### Feature Branch / GitHub workflow

_**Każdy**_ merge poprzedzony jest merge/pull request-em i recenzją kodu

![branch workflow](images/GitHub-Flow.png)

<small>[*buildazure.com](https://buildazure.com/2018/02/21/introduction-to-git-version-control-workflow/)

!SUB
### Git Flow Workflow

* Preferowany przez większe projekty
* Kilka zdefiniowanych gałęzi odpowiada różnym stadiom rozwoju projektu
* Bardzo często łączony z Forking Workflow

!SUB
### Git Flow Workflow

![gitflow workflow](images/branch_workflow01.svg)<!-- .element width="80%" -->

<small>[*atlassian.com](https://www.atlassian.com/git/tutorials/comparing-workflows)</small>


!SUB
### Forking Workflow

* Bardzo podobny do GitHub workflow
* Zamiast **gałęzi** w głównym repozytorium wykorzystujemy **fork-i**
  - Każdy pracuje z własnym forkiem przesyłając pull requesty do maintainera
* Popularny wśród małych projektów na GitHub / BitBucket etc
* Jeden maintainer głównego repozytorium


!SUB
### Forking Workflow

![fork workflow](images/fork_workflow06.svg)

<small>[*atlassian.com](https://www.atlassian.com/git/tutorials/comparing-workflows)</small>

