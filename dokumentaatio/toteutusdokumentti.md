# Toteutusdokumentti

## Ohjelman yleisrakenne

Tieteellinen laskin ottaa syötteekseen matemaattisen lausekkeen merkkijono muodossa ja antaa käyttäjälle lausekkeen arvon. Arvoja on mahdollista tallentaa muuttujiin ja käyttää muuttujia uusissa lausekkeissa. Lauseke voi sisältää lukuarvoja, muuttujia, sulkeita, peruslaskutoimituksia sekä joitakin yhden että kahden parametrin saavia funktioita. Mikäli käyttäjä yrittää syöttää virheellisen muotoisen lausekkeen, niin tästä annetaan virheilmoitus. Unix/Linux terminaali toimii käyttöliittymänä. 

Ohjelma käyttää kolmea eri algoritmia, jotka tarkistavat ja muokkaavat käyttäjän syöttämään infix muotoista lauseketta. Ensimmäinen validator-algoritmi tarkistaa infix muotoisen lausekkeen oikeellisuuden ja lisää lausekkeen eri tokenit Deque:n alkioiksi. Deque tietorakenne syötetään sitten shunting yard -algoritmille. Tämä algoritmi hyödyntää muun muassa pinoa ja muuttaa infix muotoisen lausekkeen postfix tai RPN (Reverse Polish Notation) muotoon. Shunting yard myös huomioi joitain virheitä lausekkeessa, kuten jos sulkuja on liikaa tai ne ovat epäjärjestyksessä. Algoritmi edelleen lisää tokenit Deque-tietorakenteeseen, mutta nyt RPN muodossa. RPN muotoinen lauseke voidaan sitten käyttää pinon kautta, niin että aina kahdelle pinon päälimmäiselle luvulle suoritetaan seuraavaksi tuleva laskuoperaatio. Näin saadaan tulokseksi annettun lausekkeen arvo. 

Ohjelma pystyy tarkistamaan erilaisia virheitä lausekkeista. Alla joitakin esimerkkejä:
- Sulkeiden väärä määrä tai järjestys
- Sellaiset merkit jotka eivät ole sallittuja
- Virheelliset funktiot
- Jos funktioille annetaan väärä määrä argumentteja
- Nollalla jakaminen

## Aika- ja tilavaativuudet

Shunting yard algoritmi lukee jokaisen merkin yhden kerran, pinoon menevät merkit pushataan ja popataan vain kerran, jokainen merkki myös tulostetaan vain kerran. Operaatioiden määrä per merkki on siten melko vakio. Tämän perusteella algoritmin aikavaativuus on luokkaa O(n). 

## Työn mahdolliset puutteet ja parannusehdotukset

Käyttäjä ei pysty vielä tallentamaan vastauksia muuttujiin. Negatiivinen luku täytyy antaa nollan avulla (esimerkiksi -5 täytyy syöttää muodossa 0-5).

## Laajojen kielimallien käyttö

Ohjelman kehityksessä ei ole käytetty laajoja kielimalleja.


## Viitteet

https://en.wikipedia.org/wiki/Shunting_yard_algorithm

https://en.wikipedia.org/wiki/Reverse_Polish_notation
