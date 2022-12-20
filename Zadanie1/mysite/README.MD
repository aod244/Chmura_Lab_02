Aby skonteneryzowac aplikacje nalezy: 

Sklonowac repozytorium 

Przejsc do folderu mysite
Otworzyc terminal
Wpisac komende: "docker build --tag django-app
Nastepnie wpisac komende: "docker run --name djangoapptest --publish 8000:8000 django-app
Jezeli wszystko zostalo pomyslnie zrealizowane nalezy przejsc do strony http://localhost:8000/polls/