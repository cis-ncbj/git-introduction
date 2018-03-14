# Hands on Lab 5
![rabbit](images/rabbit.png)<!-- .element width="25%" -->

<small>[yandex.ru](https://fotki.yandex.ru/next/users/tatyana2q8-medvedeva/album/129793/view/276799)</small>
## Sztuczki git

!SUB
### Git - zwaliłem ostatni commit ;-(
![facepalm](images/face-palm.jpg)<!-- .element width="70%" -->

<small>[*diy.despair.com](http://diy.despair.com)</small>

!SUB
### Git - zwaliłem ostatni commit ;-(

_**git commit --ammend**_ zamienia ostatni commit na nowy

* Ostatni commit jest wadliwy / Ma błędny komentarz
  * Poprawiamy kod w lokalnym katalogu
  * Zaznaczamy pliki do commitu (`git add`)
  * Wrzucamy poprawkę do repozytorium: `git commit --ammend`

Pozwala na prostą poprawkę / zmianę komentrza

!SUB
### Git - zwaliłem ostatni commit ;-(

![history](images/history01.svg)

<small>[*atlassian.com](https://www.atlassian.com/git/tutorials)</small>

!SUB
### Git - zmiany w starszych commitach

_**git rebase --interactive**_ - pozwala na interaktywne wybieranie commitów oraz ich edycję

```
git rebase --interactive <rodzic_commitu_z_błędem>
```

* Otwiera edytor -> Każda linia to jeden commit
* Usunięcie linii usuwa commit
* Możemy zmienić kolejność
* Dla każdej linii zostanie wykonane polecenie:

```
Commands:
p, pick = use commit
r, reword = use commit, but edit the commit message
e, edit = use commit, but stop for amending
s, squash = use commit, but meld into previous commit
f, fixup = like "squash", but discard this commit's log message
x, exec = run command (the rest of the line) using shell
```

!SUB
### git stash

_**git stash**_ umożliwia zapisanie stanu katalogu roboczego (oraz stanu indeksu) na oddzielnym stosie nieukończonych zmian bez potrzeby dokonywania commitu

* polecenie `git stash` jest przydatne jeśli zaistnieje potrzeba powrotu do któregoś z poprzednich commitów w trakcie pracy nad nowym.

Zapisanie stanu katalogu roboczego:
```bash
git stash
git stash list
```

Przywrócenie ostatniego stanu i usunięcie go ze stosu:
```bash
git stash pop
```

Inne:
```bash
git stash apply stash@{2}  # przywrócenie stanu katalogu roboczego
git stash drop stash@{0}  # usunięcie zapisanego stanu ze stosu
git stash pop stash@{1}  # przywrócenie konkretnego stanu i usunięcie go ze stosu
```

<small>Komendy `git stash apply`, `git stash drop` i `git stash pop` wykonane bez określania konkretnego elementu stosu, będą działały na ostatnim dodanym elemencie</small>

!SUB
### Git - bugi

_**git blame**_ - pokazuje kto zmienił każdą linijkę w pliku i kiedy

_**git bisect**_ - wykorzystuje metodę bisekcji (na grafach) do wykrycia w którym miejscu po raz pierwszy pojawił się błąd

!SUB
### Git bisect

Znamy ostatni dobry commit oraz commit gdzie objawia się błąd:

![bisect1](images/bisect1.png)

<small>[*paradigmadigital.com](https://www.paradigmadigital.com/dev/sacale-mas-partido-tus-proyectos-git/)

!SUB
### Git bisect

Startujemy bisekcję:

```
git bisect start
git bisect bad                 # Aktualna wersja jest zła
git bisect good v2.6.13-rc2    # Wiemy że tag v2.6.13-rc2 jest dobry
```
_**git bisect**_ będzie checkout-ował kolejne commit-y z pomiędzy ostatniego dobrego i najstarszego złego starając się zminimalizować liczbę commitów do przejrzenia

![bisect2](images/bisect2.png)

<small>[*paradigmadigital.com](https://www.paradigmadigital.com/dev/sacale-mas-partido-tus-proyectos-git/)

!SUB
### Git bisect

Po weryfikacji oznaczamy commit jako dobry lub zły

```
git bisect good  # Jeśli wersja jest dobra
git bisect bad   # Jeśli wersja jest zła
```

![bisect3](images/bisect3.png)

<small>[*paradigmadigital.com](https://www.paradigmadigital.com/dev/sacale-mas-partido-tus-proyectos-git/)

!SUB
### Git bisect

W końcu docieramy do commit-u który wprowadził błąd do kodu

![bisect3](images/bisect4.png)

<small>[*paradigmadigital.com](https://www.paradigmadigital.com/dev/sacale-mas-partido-tus-proyectos-git/)

