# tsoha2021-harjoitustyo
## Kyselysovellus

Sovellus on Helsingin Yliopiston Tietokantasovellus harjoitustyökurssin projekti.

Sovellusta voidaan käyttää opitun tiedon harjoittelemiseen kysymyssettien avulla.

Sovelluksessa on kolme käyttäjätasoa: Admin, Ohjaaja ja Harjoittelija. Admin voi hallinnoida sovellusta esimerkiksi poistamalla käyttäjiä, aiheita ja kommentteja. Ohjaaja voi luoda sovellukseen aiheita, kysymyksiä ja vastausvaihtoehtoja. Kaikki käyttäjäroolit voivat vastata kysymyksiin ja seurata kehitystään.

#### Sovelluksen ominaisuuksia ovat:

- Käyttäjä voi luoda tunnuksen ja kirjautua sovellukseen sisään.
    + Tämä toiminto on toteutettu kokonaisuudessa.
- Admin voi luoda toisen admin käyttäjän
    + Tämä toiminto on mahdollinen jatkokehityskohde
- Admin voi poistaa minkä tahansa aiheen, kysymyksen tai viestin.
    + Tällä hetkellä Admin voi poista käyttäjän, aiheen, kysymyksen ja kommentin. Lisäksi Admin voi muokata kysymysten sisältöä.
- Ohjaaja voi luoda uuden aiheen, kirjoittaa siitä lyhyen kuvauksen ja lisätä siihen kysymyksi vastausvaihtoehtoineen.
    + Tämä toiminto on toteutettu. Ohjaaja voi luoda vain Tosi/Epätosi tyyppisiä kysymyksiä. Ohjaaja voi lisätä kysymyksiä ainoastaan itseluominsa aiheisiin.
    + Monivalinta- sekä lukuarvovastaustyyppisiä kysymysten luominen on jatkokehityskohde.
- Ohjaaja voi poistaa luomansa aiheen tai vain yksittäisen kysymyksen siitä aiheesta.
    + Tämä toiminto on siirretty Admin käyttäjälle. Ohjaajan mahdollisuus poistaa aiheita tai kysymyksiä on jatkokehityskohde.
- Ohjaaja voi katsoa kysymyskohtaiset tilastot, kuinka usein mihinkin kysymykseen on vastattu oikein.
    + Tämä toiminto on mahdollinen jatkokehityskohde
- Harjoittelija voi valita aiheen ja tutustua aiheen kuvaukseen.
    + Harjoittelija näkee aiheen kuvauksen kyselysivulla.
- Harjoittelija voi valita kuinka moneen kysymykseen hän haluaa vastata (esim. 10 tai 20 kpl). Harjoittelija vastaa kysymyksiin ja saa heti palautteen siitä, kuinka moni vastaus meni oikein. Lopuksi Harjoittelija näkee tilaston omista vastauksista.
    +  Siirtyessä kyselysivulle Harjoittelija näkee aiheen kuvauksen ja pyydetyn määrän kysymyksiä, jotka on arvottu aiheen kaikista kysymyksistä.
    + Kyselyn suorittamisen jälkeen Harjoittelija näkee kuinka moneen kysymykseen hän on vastannut oikein ja mikä on oikeiden vastausten prosenttiosuus. Lisäksi kuinka monta kertaa Harjoittelija on vastannut tämän aiheen kysymyksiin, moneenko kysymykseen yhteensä sekä mikä on kaikkien vastausten oikeiden vastausten prosenttiosuus.
- Harjoittelija voi lähettää Ohjaajalle viestin, jos havaitsee virheen kysymyksessä tai haluaa antaa palautetta sisällöstä.
    + Harjoittelija pystyy lähettämään kommentin aiheesta/kysymyksestä. Ohjaaja näkee kaikki omien aiheiden kommentit ja voi kuitata ne luetuksi. Admin voi poista suljetut kysymykset. Ohjaajan mahdollisuus poistaa kommentti on jatkokehityskohde.

Sovellus on testattavissa ja löytyy osoitteesta: https://tsoha2021-quizapp.herokuapp.com/

Sovellukseen on luotu kolme testikäyttäjää:

- Käyttäjä - salasana: testaus (rooli Ohjaaja)
- Testaaja - salasana: testaus2 (rooli Harjoittelija)
- Admin - salasana: admin (rooli Admin)

#### Tietokannan rakenne:

Tietokantakaavio kuvattu schema.sql tiedostossa. Tietokannassa on 5 aktiivista taulua. Taulu Answer on luotu monivalinta- ja lukuarvo- kysymyksiä varten ja tässä vaiheessa ei ole käytössä.

#### Sovelluksen jatkokehityskohteet:

- Sovelluksen ulkoasu
- Kommentteihin vastaaminen
- Ohjaajan oikeuksien kehittäminen