# Viikkoraportti 3

Tällä viikolla perehdyin testien luomiseen. Pelkkään perehtymiseen kului itsessään jonkin verran aikaa, koska edellisten testien luonnista on taas hieman aikaa. Loin testejä pääosin Validator-luokan algoritmille sekä joitain alustavia testejä ShuntingYard-luokalle. Sain testit hyvin ajan tasalle ja tästä eteenpäin tavoitteena on luoda testejä aina sitä mukaan, kun uutta koodia syntyy. Alustava testausdokumentti on myös luotu.

Tein myös rakenteeseen muutoksia. Alun perin lähes kaikki toiminnallisuus, käyttöliittymää lukuun ottamatta, sijaitsi Calulator-luokan sisällä. Luokka alkoi kasvaa liian suureksi, joten loin omat Validator ja ShuntingYard -luokat, jotka vastaavat lausekkeiden käsittelystä. Koodi on näin selkeämpää ja helpompilukuista. Jouduin rakennemuutoksen takia myös korjaamaan jo tehdyt testit, mutta tästä eteenpäin testaaminen on helpompaa, kun toiminnallisuudet on eritelty omiin luokkiin. 

Muuten aika kului periaatteessa Validator-luokan metodien kehittämiseen. Näistä suurin osa on nyt tehty, joitain pieniä viilauksia ja lisäyksiä luokkaan varmaan vielä tulee, mutta ne on järkevämpi toteuttaa myöhemmin. Luokka tarkistaa nyt riittävällä tasolla string-muotoisen lausekkeen, erittelee lausekkeesta tokenit deque-tietorakenteeseen,joka voidaan sitten syöttää shunting yard algoritmille. 

Aloitin myös ShuntingYard-luokan kehittämisen, joka vastaa infix lausekkeen muuttamisesta postfix muotoon. Loin alustavia metodeja ja testejä. Seuraavaksi on tarkoitus jatkaa kehitystä tämän parissa. 

Aikaa kului työskentelyyn noin 12 tuntia.