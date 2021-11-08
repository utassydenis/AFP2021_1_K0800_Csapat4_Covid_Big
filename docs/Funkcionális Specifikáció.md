# COVID-FORECAST
## 1. Áttekintés
---
A projekt elsődleges célja az, hogy a program egy adott adatbázisból jósoljon COVID adatokat. Éppen ezért a program GUI felületének egyszerűnek és könnyen
kezelhetőnek kell lennie, hogy mindenki tudja használni (azok is, akik egyáltalán nem értenek a programozáshoz). A program legfőbb (és talán egyetlen)
funkciója, hogy egy adott időintervallum megadásával COVID adatokat jósoljon az adott intervallumtől későbbi időpontra. Az időintervallum tetszőleges,
lehet több hónap, egy hónap, de akár egy hét is. Például ha 2021.10.04-től 2021.10.10-ig állítjuk ezt be, akkor az adatok feldolgozásával meg tudja jósolni
a 2021.10.11-2021.10.17-re valószínűsíthető COVID adatokat.
Az adatbázis tartalmazza: 
dátum (nap, hónap, nap), napi fertőzöttek, halálozás, ország, népesség, kontinens, összes eddigi fertőzött.
Az bemenő adatbázis módosítható, hiszen pontosabb adatok bármikor előfordulhatnak, így a kimenet reálisabb lesz.
A program a kimenetet számszerűsített adatokkal, vagy grafikon segítségével adja vissza.

## 2. Jelenlegi helyzet
---
A megrendelő egy olyan programot szeretne, ami szemlélteti számszerűsített adatokkal vagy grafikonnal a COVID-19 járvány terjedését. Ezt egy Python program
segítségével képzeli el, hiszen így egy számítógépre lesz csak szüksége, amin megadja az időintervallumot és meg is kapja a várható adatokat. A bemeneti
adatokat egy adatbázissal akarja megadni, mivel az könnyen módosítható (pontosabb adatok érdekében, hiszen bármikor változhatnak az adatok, így pontosabb
adatokkal reálisabb eredményt kaphatunk), illetve akár teljesen cserélhető is. Jelenleg sok forrásból dolgozik a megrendelő, ami sok nehézséget eredményez,
illetve nagy odafigyelést igényel. Fontos számára, hogy a program ne adjon vissza olyan adatot, ami már első ránézésre sem jó, hiszen akkor a projekt nem
teljesíti célját. Emelett leszögezte, hogy a GUI felületnek egyszerűnek és felhasználóbarátnak kell lennie, hogy mindenki tudja használni (azok is, akik
egyáltalán nem értenek a programozáshoz). Ezen okokból kifolyólag megkértek minket, hogy csináljuk meg nekik a vágyott programot, ami megkönnyíti mindennapi
munkájukat a járvány elleni védekezésben.

## 3. Jelenlegi üzleti folyamatok modellje
---
![Image](https://github.com/utassydenis/AFP2021_1_K0800_Csapat4_Covid_Big/blob/main/pictures/jelenlegiuzeltifolyamatokmodellje.jpg)

## 4. Igényelt üzleti folyamatok modellje
---
![Image](https://github.com/utassydenis/AFP2021_1_K0800_Csapat4_Covid_Big/blob/main/pictures/funkspec-igényeltüzletifolyamatokmodellje.jpg)

## 5. Használati eset
---

### LEÍRÁS

A használati diagram alapvetően 4 aktorral operál melyek nem mások mint:
    - Felhasználó
    - Adatbázis
    - Fejlesztő
    - A számítást végző matematikai képlet

**Felhasználó**: Képes megtekinteni a felhasznált adatbázist, el tudja érni a grafikus megjelenést, be tudja állítani az időintervallumot, illetve elérhető a jóslás funkció a számára.
**Fejlesztő**: Képes módosítani az adatbázist és a jóslás funkcióban használt képletet.

Egy specifikus használati eset leírása:

Egy felhasználó megvásárolja a programunkat mely segítségével hiteles jóslást képes végezni a Covid megbetegedések esetében.
Amint beállította a számára érdekes idő intervallumot, kezdheti is a jóslást. Ha ez megvan megkapja a kívánt adatokat amelyek nem csak
számszerűsítve, de rajzolt grafikus felületen is elérhető lesz számára.

![Image](https://github.com/utassydenis/AFP2021_1_K0800_Csapat4_Covid_Big/blob/main/pictures/CovidUseCaseDatabase.png)

## 9. Fogalomtár
---
**Python**: A Python jelenleg talán a legjelentősebb szkriptnyelv (TIOBE index 4. hely Java, C és C++ után). Szkritpnyelvként a Python
lehetővé teszi, hogy magasabb szintű, absztraktabb, elegánsabb kódot írjunk, azon az áron, hogy a program lassabban fog futni. Ahogyan
egyre gyorsabbak a gépek, egyre több és több olyan feladat van, ahol egyszerűen nincs igény a nyers vas sebességére.

**COVID**: A Covid19 (koronavírus-betegség 2019, coronavirus disease 2019) vírusos légúti, illetve légzőszervi megbetegedés, amelyet a
SARS-CoV-2 nevű koronavírus okoz.  A COVID-19 fertőzés a tüdők mellett más szerveket is károsíthat, ezzel növelve a hosszú távú 
egészségi problémák kockázatát. Okozhat szívizomgyulladást, amelynek szövődményeként akár szívelégtelenség is felléphet.

**GUI**: A grafikus felhasználói felület vagy grafikus felhasználói interfész (angolul graphical user interface, röviden GUI) a
számítástechnikában olyan, a számítógép és ember közti kapcsolatot megvalósító elemek összessége, melyek a monitor képernyőjén szöveges
és rajzos elemek együtteseként jelennek meg. A grafikus felhasználói felületeken alapvető szerepe van a mutatóeszközök, például az egér
használatának, amelyekkel a grafikus felület elemei intuitív módon, a fizikai világ egyfajta modelljeként kezelhetők. A leggyakoribb
grafikus felhasználói elemek az ablakok, menük, választógombok, jelölőnégyzetek és ikonok, valamint a mutatóeszközhöz kapcsolódó
egérkurzor.

**Forecast**:  Egyfajta előrejelzés vagy prognózis.

**Adatbázis**: Az adatbázis azonos minőségű, többnyire strukturált adatok összessége, amelyet egy azok tárolására, lekérdezésére és
szerkesztésére alkalmas szoftvereszköz kezel. Célja: adatok megbízható, hosszú távon tartós tárolása és viszonylag gyors
visszakereshetőségének biztosítása.