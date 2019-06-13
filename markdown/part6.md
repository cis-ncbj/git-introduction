# Automatyzacja
![rabbit](images/automatization.jpg)<!-- .element width="80%" -->
## Szanuj swój czas ;)

!SUB
### Continous Integration

#### Best practices

* Maintain a code repository
* Automate the build
* Make the build self-testing
* Everyone commits to the baseline every day
* Every commit (to baseline) should be built
* Keep the build fast
* Test in a clone of the production environment
* Make it easy to get the latest deliverables
* Everyone can see the results of the latest build
* Automate deployment

!SUB
### CI

![jenkins](images/jenkins.png)<!-- .element width="5%" -->

https://jenkins.io

![travis](images/TravisCI-Full-Color.png)<!-- .element width="20%" -->

https://travis-ci.org

!SUB
### CI

![circleci](images/circleci.png)<!-- .element width="10%" -->

https://circleci.com

![gitlab](images/gitlab-logo.png)

https://gitlab.com


!SUB
### Testery kodu

![codacy](images/codacy.png)<!-- .element width="10%" -->

https://www.codacy.com/

![coveralls](images/coveralls.png)<!-- .element width="25%" -->

https://coveralls.io/

![snyk](images/snyk.png)<!-- .element width="8%" -->

https://snyk.io/

!SUB
### Przykłady

* https://github.com/tensorflow/tensorflow
* https://github.com/flutter/flutter
* https://github.com/facebook/react


!SUB
### code.cis.gov.pl

https://docs.gitlab.com/ce/ci/

https://docs.gitlab.com/ce/ci/yaml/README.html

!SUB
### Ćwiczenia

Aktywujemy CI dla projektu **git_handson**

* Settings -> General Settings -> Visibility ... -> Piplines -> [On]
* Settings -> CI/CD -> Runners -> Shared Runners -> [Enable Shared Runners]

!SUB
### Ćwiczenia

* Otwieramy projekt git_handson
* Dodajemy plik _**.gitlab-ci.yml**_

```
pylint: # Nazwa zadania
  tags: # Tagi określają predefiniowane środowiska
    - python3 # W CIŚ mamy python3 i docker
  stage: test # Domyślnie wyróżniamy trzy etapy: build -> test -> deploy
  script: # Skrypt który będzie wykonany w zadaniu
    - pip install pylint --quiet
    - pylint *.py
```
