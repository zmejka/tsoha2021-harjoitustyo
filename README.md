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

- Sovellukseen voi kirjautua, joko luomalla oman tunnuksen tai käyttämällä käyttäjätunnuksia Käyttäjä (salasana: testaus) tai Admin (salasana: admin). Tässä vaiheessa käyttäjäroolien toiminnassa ei ole vielä eroja.
- Käyttäjä voi luoda aiheita ja lisätä aiheisiin kysymyksiä.
- Tässä vaiheessa voi luoda ainoastaan Tosi/Epätosi tyyppisiä kysymyksiä.
- Käyttäjä voi valita aiheen ja aloittaa kysymyksiin vastamista, mutta tämä toiminto on toteutettu vain osittain. Tällä hetkellä kysymys ei vaihdu.

Puutteet:

- Sovelluksen ulkoasua ei vielä toteutettu
- Sovelluksen toiminnot on hyvin keskeneräisiä
- Käyttäjätunnuksen ja salasanan merkkimäärät ei ole rajoitettu
- Rekisteröitymisestä, aiheiden ja kysymysten luomisen onnistumisestä/epäonnistumisestä ei tule mitään ilmoitusta.
- Käyttäjätasojen toimintaerot puuttuvat
- Tietoturva vaatimuksia ei vielä otettu kunnolla huomioon
- Ohjelman rakennetta ei vielä jäsennetty kunnolla