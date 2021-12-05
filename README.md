# tsoha2021-harjoitustyo

Sovelluksen voidaan käyttää opitun tiedon harjoittelemiseen kysymyssettien avulla. Kysymysten vastausvaihtoehtoja voivat olla tosi tai epätosi, valitse oikea vaihtoehto tai jokin lukuarvo tai sana.

Sovelluksessa on kolme käyttäjätasoa: Admin, Ohjaaja ja Harjoittelija. Admin voi hallinnoida sovellusta esimerkiksi poistamalla käyttäjiä, aiheita ja viestejä. Ohjaaja voi luoda sovellukseen aiheita, kysymyksiä ja vastausvaihtoehtoja. Harjoittelija voi vastata kysymyksiin ja seurata kehitystään.

Sovelluksen ominaisuuksia ovat:

- Käyttäjä voi luoda tunnuksen ja kirjautua sovellukseen sisään.
- Admin voi luoda toisen admin käyttäjän
- Admin voi poistaa minkä tahansa aiheen, kysymyksen tai viestin.
- Ohjaaja voi luoda uuden aiheen, kirjoittaa siitä lyhyen kuvauksen ja lisätä siihen kysymyksiä vastausvaihtoehtoineen.
- Ohjaaja voi poistaa luomansa aiheen tai vain yksittäisen kysymyksen siitä aiheesta.
- Ohjaaja voi katsoa kysymyskohtaiset tilastot, kuinka usein kukin kysymykseen on vastattu oikein.
- Harjoittelija voi valita aiheen ja tutustua aiheen kuvauksen.
- Harjoittelija voi valita kuinka monen kysymykseen hän halua vastata (esim. 10 tai 20 kpl). Harjoittelija vastaa kysymyksiin ja saa heti palautteen, menikö vastaus oikein. Lopuksi Harjoittelija näkee tilaston omista vastaauksista.
- Harjoittelija voi lähettää Ohjaajalle viestin, jos havaitsee virheen kysymyksessä tai haluaa antaa palautetta sisällöstä. Ohjaaja voi vastata saamaansa palautteeseen.

Sovellus on testattavissa. Sovellus löytyy osoitteesta: https://tsoha2021-quizapp.herokuapp.com/

Sovellukset testaaminen:

- Sovellukseen voi kirjautua, joko luomalla oman tunnuksen tai käyttämällä käyttäjätunnuksia:
  Käyttäjä (salasana: testaus, rooli Ohjaaja), Testaaja (salasana: testaus2, rooli Harjoittelija) tai Admin (salasana: admin). Admin tunnuksen toimintoja ei ole vielä toteutettu, joten sitä ei kannata tässä vaiheessa käyttää.
- Käyttäjä (rooli Ohjaaja) voi luoda aiheita ja lisätä aiheisiin kysymyksiä. Tällä hetkellä voidaan luoda ainoastaan Tosi/Epätosi tyyppisiä kysymyksiä.
- Testaaja (rooli Harjoittelija) ja Käyttäjä (rooli Ohjaaja) voivat valita aiheen ja kysymysten määrän sekä suorittaa kyselyn. Tämä toiminto on toteutettu vasta osittain. Tällä hetkellä kysymysten arvonta ei toimi.
- Käyttäjä näkee aiheen kuvauksen Quiz sivulla.
- Kyselyn perusteella käyttäjä näkee kuinka moneen kysymykseen on vastattu oikein. 
- Käyttäjä voi tallentaa aiheeseen liittyvät kommentit tai kysymykset tietokantaan, mutta ne ei vielä pysty sieltä tarkastelemaan.

Puutteet:

- Sovelluksen ulkoasu on puutteellinen
- Sovelluksen toiminnoista puuttuu vastausten tilastot sekä kommenttien hakeminen. 
- Tietoturva vaatimuksia on toteutettu vain osittain
- Admin toiminnot kuten aiheiden, kysymysten ja kommenttien poistot puuttuu.