# COVID-FORECAST
## 1. Áttekintés
---
A projekt célja, hogy egy Pythonban megírt program meg tudja jósolni a COVID adatokat (pl. megbetegedések száma, elhalálozások száma,
napi fertőzöttek) egy időintervallum alapján. A program egy adatbázisból szerzi az adatokat. Az adatbázisnak tartalmaznia kell: 
dátum (nap, hónap, nap), napi fertőzöttek, halálozás, ország, népesség, kontinens, összes eddigi fertőzött. A könnyű tesztelés és
átláthatóság érdekében szükség van egy egyszerű GUI felületre, amin könnyedén meg lehet adni az időintervallumot, hogy mettől meddig
dolgozza fel az adatokat. Az időintervallum tetszőleges, lehet több hónap, egy hónap, de akár egy hét is. Például ha 2021.10.04-től
2021.10.10-ig állítjuk ezt be, akkor az adatok feldolgozásával meg tudja jósolni a 2021.10.11-2021.10.17-re valószínűsíthető COVID
adatokat.

## 3. Vágyálom rendszer
A 2019 végén megjelenő új koronavírus, a SARS-CoV-2 a világ minden kormányát jelentős kihívások elé állította. Az egészségügyi
kapacitások tervezése, a járvány megállítását célzó korlátozó intézkedések bevezetése vagy megszüntetése döntéstámogató előrejelző
rendszerek működtetését teszi szükségessé. A monitorozó/előrejelző rendszerek egyik lehetséges eszköze lehet a COVID-FORECAST projekt.
A könnyebb információszerzés érdekében van szükségünk a projekt által nyújtott előrejelzésre. Az időintervallum megadásával könnyen fel
lehet készülni akár egy újabb hullámra is. Fontos, hogy megbízhatóak és hitelesek legyenek az adatok, amikből a program dolgozik, hiszen
csak így juthatunk minél pontosabb eredményhez. A program grafikus része legyen egyértelmű, egyszerű és könnyen kezelhető. Az adatbázis,
amiből a program dolgozik legyen módosítható, hiszen pontosítások gyakran történnek az adatokban. A legfontosabb, hogy hatalmas eltérésű,
valószínűtlen eredményt ne adjon vissza a program, mert akkor feltételezhető a helytelen működés. Az eredmény lehet hasonló, mint a
feldolgozott adatbázis, de ha eltérő, akkor legyen rendezett, átlátható és precíz. Akár lehet egy Excel táblázat is, de egy grafikon
még jobb, mivel jobban szemlélteti a javuló vagy esetleg romló járványügyi adatokat.