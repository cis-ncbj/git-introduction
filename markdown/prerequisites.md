# Zajęcia "Hands on"
## Zanim zaczniemy ...

!SUB
### Garść uwag
* Slajdy dostępne są pod adresem:

 [http://cis-ncbj.github.io/git-introduction/](http://cis-ncbj.github.io/git-introduction/)
* Nawigacja przez slajdy jest prosta, wystarczy używać strzałek na klawiaturze:
  * Lewo i prawo przechodzi do poprzedniej lub następnej sekcji. Góra i dół przechodzi do poprzedniego lub następnego slajdu.
  * Spacja zawsze przechodzi do następnego slajdu.
* Wszystkie kroki zakładają że macie otwarty terminal lub Visual Studio Code.
* Prawie wszystkie bloki kodu pomyślane są aby je wykonać:
  *  `\` oznacza kontynuację linii i można go kopiować,
  * `< ... > ` oznacza że należy wstawić poprawną wartość.
* Bawcie się dobrze, nie śpieszcie się, zadawajcie pytania.

!SUB
### Informacje dodatkowe
<!-- .slide: data-background="#c6e0a3" data-transition="fade" -->

* W prezentacji będą pojawiały się slajdy z informacjami dodatkowymi.
* Będą miały zielone tło jak ten slajd.

**UWAGA**

Nie wykonujemy poleceń przedstawionych na slajdach dodatkowych :)

!SUB
### Polecenia git
<!-- .slide: data-background="#bed3f4" data-transition="fade" -->

* Ćwiczenia będziemy wykonywać w większości w Visual Studio Code.
* Dodatkowo przedstawiamy jak ćwiczenia wykonać w linii komend.
* Slajdy z poleceniami **git** będą miały niebieskie tło jak ten slajd.

**UWAGA**

Nie wykonujemy poleceń przedstawionych na slajdach dodatkowych :)

!SUB
### Środowisko

* Zajęcia prowadzone będą w środowisku Visual Studio Code
  * Pokarzemy jak te polecenia wykonać także z lini komend
* Przykłady wymagają git-a w wersji min 2.0

```
git --version
```

* Przykłady testowane były z git-em 2.13 oraz 2.39

!SUB
### VPN

Będziemy pracować z serwisem https://code.cis.gov.pl

Do połączenia wymagane jest zestawienie połączenia VPN:
* Uruchamiamy klienta OpenVPN
* Sprawdzamy czy możemy się zalogować na https://code.cis.gov.pl

!SUB
### Klucze SSH

Najwygodniejszą metodą logowania do zdalnych repozytorii są klucze SSH

* Generujemy nową parę kluczy - należy zdefiniowac hasło:
```
ssh-keygen -f ~/.ssh/id_rsa_code
```

* Używamy naszych kluczy
```
eval $(ssh-agent)
ssh-add ~/.ssh/id_rsa_code
```

* Wyświetlamy klucz publiczny
```
cat ~/.ssh/id_rsa_code.pub
# albo
ssh-add -L
```

!SUB
### Dodajemy klucz publiczny SSH do code.cis.gov.pl

![ssh](images/ssh.png)

Testujemy:
```
ssh git@code.cis.gov.pl
```

<!--
!SUB
### Visual Studio Code + Git

![VSC start](images/vsc-start.png)
-->

!SUB
### Visual Studio Code + Git

![VSC git extensions](images/vsc-plugins.png)
