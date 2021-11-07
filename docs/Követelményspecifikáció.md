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

## 2. Jelenlegi helyzet
---
A megrendelő szeretne jobban belátást nyerni a COVID-19 által keletkezett megbetegedések számában. A program ezt szeretné lehetővé tenni, könnyű kezelése, hatékonysága és gyorsasága révén, ami által könnyedén szinte nulla szakértelem nélkül megjeleníthető a program
által jósolt megbetegedések adatai. A program egyfajta számolásnak köszönhetően képes ezt megjeleníteni a felhasználója számára. A
rendszer a pontos adatok (ezalatt most a dátumokat értem) felvitele után lesz képes a számolásra, azaz a jóslásra. A számok nem lesznek teljesen pontosak, egyfajta megközelítő értékkel szolgál, amiből ki lehet indulni és következtetéseket levonni az eredmény felhasználása során. 

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

## Követelmény lista

| ID | Név | Kifejtés |
| ------------- | ------------- | ------------- |
| 1 | Időintervallum megadás | A felhasználó az időintervallum megadásával tudja szűrni, mely idő közötti adatokat lássa. |
| 2 | Listázás | Ezen opció segítségével tudja a bevitt adatokat megjeleníteni az adatbázisból. |
| 3 | Predict | Ezen funkció segítsével tudja a felhasználó megindítani a jóslási folyamatot. |
| 4 | Adatbázis | Ezen opció segítsével tudja a felhasználó megadni a kívánt adatbázist. |
| 5 | Grafikus felület | A felhasználó itt tudja megtekinteni a megjósolt adatokat grafikus felületen. |

## 4. Jelenlegi üzleti folyamatok

Jelenleg a megrendelő a különböző webes felületeken tud tájékozódni a statisztikákról (Google statisztikák, https://koronavirus.gov.hu/, stb.), ahol a jelenlegi statisztikákat tudja elérni. Az előrejelzések webhelyenként eltérőek.

## 5. Igényelt üzleti folyamatok

1. Online megjelenés
2. Adatbázis
    1. Online adatbázisokból lekérdezés
    2. Adattárolás
3. Adatok listázása egy megadott időintervallumon belül
4. Megbetegedés, halálozások, gyógyulások előrejelzése