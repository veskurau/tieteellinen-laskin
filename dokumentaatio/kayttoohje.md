# Käyttöohje

## Ohjelman asennus

- Ohjelmassa on käytössä Poetry riippuvuuksien hallintaan. Tarkista, että Poetry on asennettu koneellesi. 

- Kloonaa ohjelma koneellesi

- Asenna riippuvuudet juuri kansiossa: 

```bash
poetry install
```

- Suorita ohjelma komennolla juuri kansiossa: 

```bash
poetry run python3 src/index.py
```

## Ohjelman käyttäminen

Ohjelma ottaa vastaan lausekkeita, jotka voivat sisältää:
- Positiivisia kokonaislukuja ja liukulukuja (esim. 5, 1000, 15.25)
- Jos haluat syöttää yksittäisen negatiivisen luvun, niin tässä pitää käyttää hyödyksi nollaa (esim. (0-5) vastaa arvoa -5)
- Normaalit laskuoperaatiot ovat: +, -, *, /, ^
- Lisäksi ohjelmalle voidaan syöttää kaarisulkeita ( ja )
- Mikäli negatiivisia lukuja halutaan esim. kertoa tai jakaa, käytetään jälleen hyödyksi nollaa. Esim. 2*(0-2)
- Yhden argumentin funktiot: sqrt, sin, cos, tan (esim. sqrt(9))
- Kahden argumentin funktiot: max, min (esim. max(2,3))