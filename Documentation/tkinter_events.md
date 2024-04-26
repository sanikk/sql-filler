tkinterin eventin hallintakoodi kiinnostaa. miten siellä erotellaan noita eventtejä aiheuttavia objekteja koodissa?
näköjään siihen eventin aiheuttaneeseen namiskaan päästään suoraan kuitenkin käsiksi eventin kautta niin eiks siinä vois
tehdä jotain identiteetti checkkejä?

toi on varmaan vaan mietitty meillä väärin. siellä on välillä bindattu väärään objektiin tuo eventin vahtaaja. jos
widget itse seuraa omia tapahtumiaan ja sillä on vaan joku rajapinta mistä toteuttaa muutokset niin luulis toimivan.

Koko jutussa on kyse tosta yksi listbox meemistä, vai mikä widget olikaan.

Jos toi on tehty paskasti niin vois katsoa jos sais vähän valikoitua noita eventtejä niin
että tuo seuraisi ensijaisesti omiaan. 

Vaikuttaisi vain järkevältä. Objekti seuraa vain omia eventtejään