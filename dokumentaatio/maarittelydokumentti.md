# Määrittelydokumentti

## Yleistä

Harjoitustyön tavoitteena on luoda tieteellinen laskin.

Opinto-ohjelma on tietojenkäsittelytieteen kandidaatti.

Harjoitustyön ohjelmointikieli on Python. Python on minulle tutuin kieli, joten pystyn vertaisarvioimaan muiden töitä, jotka ovat tehty Pythonilla.

Koodin luokat, funktiot, metodit, kommentit ym. kirjoitetaan englanniksi. Dokumentaatio tehdään suomeksi. 

## Harjoitustyön kuvaus

Tieteellinen laskin ottaa syötteekseen matemaattisen lausekkeen merkkijono muodossa ja antaa käyttäjälle lausekkeen arvon. Arvoja on mahdollista tallentaa muuttujiin ja käyttää muuttujia uusissa lausekkeissa. Lauseke voi sisältää lukuarvoja, muuttujia, sulkeita, peruslaskutoimituksia sekä joitakin yhden että kahden parametrin saavia funktioita. Mikäli käyttäjä yrittää syöttää virheellisen muotoisen lausekkeen, niin tästä annetaan virheilmoitus. Unix/Linux terminaali toimii käyttöliittymänä.  

Ratkaistava ongelma on, että kuinka saadaan laskettua arvo annetulle lausekkeelle, joka on annettu infix muodossa. Tämän ongelman ratkaisemiseksi toteutetaan shunting yard algoritmi. Algoritmi ottaa syötteenä matemaattisen lausekkeen infix muodossa. Hyödyntäen muun muassa pinoa, algoritmi antaa ulos lausekkeen postfix muodossa, tätä muotoa kutsutaan myös nimellä RPN (Reverse Polish notation). RPN muotoinen lauseke voidaan sitten käyttää pinon kautta, niin että aina kahdelle pinon päälimmäiselle luvulle suoritetaan seuraavaksi tuleva laskuoperaatio. Näin saadaan tulokseksi annettun lausekkeen arvo. 

Tärkeänä osana on toteuttaa algoritmi myös niin, että se havaitsee, jos käyttäjän syöttämä lauseke on virheellinen. Se ei esimerkiksi sisällä oikeaa määrää sulkuja, joltain operandilta puuttuu operaatio tai lauseketta ei ylipäätään pysty laskemaan. 

Shunting yard algoritmi lukee jokaisen merkin yhden kerran, pinoon menevät merkit pushataan ja popataan vain kerran, jokainen merkki myös tulostetaan vain kerran. Operaatioiden määrä per merkki on siten melko vakio. Tämän perusteella algoritmin aikavaativuus on luokkaa O(n). 

## Harjoitustyön ydin

Harjoitustyön ydin on yllä kuvatun shunting yard algoritmin toteutus. Niin että algoritmi ottaa syötteenä infix muotoisen matemaattisen lausekkeen ja muuttaa sen RPN muotoon. Algoritmin pitää pysty lukemaan lukuarvoja, sulkeita, peruslaskutoimituksia sekä erilaisia yhden ja kahden parametrin funktioita, kuten esimerkiksi potenssi, neliöjuuri, sin, min, max. Algoritmi täytyy kehittää niin, että se havaitsee virheelliset infix muotoiset lausekkeet. Lisäksi täytyy tehdä erillinen pinototeutus, että RPN muotoisesta lausekkeesta saadaan arvo laskettua. Tämä arvo on mahdollista sitten tallentaa muuttujaan ja syöttää muuttuja uuden lausekkeen yhteydessä. 

## Viitteet

https://en.wikipedia.org/wiki/Shunting_yard_algorithm

https://en.wikipedia.org/wiki/Reverse_Polish_notation
