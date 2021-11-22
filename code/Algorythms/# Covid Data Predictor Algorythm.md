# Covid Data Predictor Algorythm
## Linear Regression + Input request

---

## Nehány tisztázni való alapfogalom.

- Machine Learning (ML): A Machine Learning vagy Gépi tanulás módszere egy képességet demonstrál
                         mely segítségével bizonyos rendszerek képesek automatikusan tanulni és fejleszteni önmagukat.

- Data Set: Egy egységes adatbázis amely válogatott adatokból áll össze. Az algoritmus az itt 
            megadott információ alapján dolgozik.

- Data Visualisation: Általában valamilyen (oszlop, vonal, kör stb.) diagram segítségével mutatja be a kapott adatok
                      viszonyát egymáshoz képest.

- Data Cleaning: Adat tisztítás. A nem megfelelő formátumban levő, nem pontos, fölösleges, többször megjelenő vagy
                 nem teljes adatok eltávolítása az adatbázisból.

![Image](https://github.com/utassydenis/AFP2021_1_K0800_Csapat4_Covid_Big/blob/main/pictures/linear_regression.gif)

A statisztika eszköztárában a lineáris regresszió egy olyan paraméteres 
regressziós modell, mely feltételezi a magyarázó- (X) és a magyarázott (y) változó 
közti (paramétereiben) lineáris kapcsolatot. Ez azt jelenti, 
hogy lineáris regresszió becslése során a mintavételi adatok 
pontfelhőjére igyekszünk egyenestilleszteni.

A lineáris regresszió egy "jósló" feladatot lát el, amely a függő változókat jósol
megadott függettlen változók alapján. Tehát ez a regressziós technológia jövőben mutató
kapcsolatot keres a bemenő és kimenő változók között.

Az algoritmus a matpotlib könyvtár alapján íródott.

### Az algoritmus felépítése

    1. Az adatbázis beimportálása.
    2. Az adatbázis letisztítása.
    3. Az algoritmus felépítése.
    4. Az algoritmus tesztelése.
    5. Jóslás az adatok alapján.
    6. Adatok leképezése diagram formátumban.

## Összefoglalás

    Az algoritmus feldolgozol egy adatbázist, ahol szükséges ott korrigálja az adatokat.
    A beolvasott adatok segítségével feltölti a képletet, majd kirajzolja a kapott információt.
    Végül kér egy esetszámot, amihez a korabbi adatok alapján jósol.

## Linear Regression

---

Az algoritmus a scikit-learn könyvtár alapján íródott.


### Az algoritmus felépítése:

    1. Beimportáljuk a kódolás alatt felhasznált könyvtárakat.
    2. Beolvassuk az adatbázist jellemzően egy xlsx vagy csv fileból.
    3. Szűkítjük az adatbázist a számunkra érdekes adatokra.
    4. Két részre szedjük az adatokat, melyek lesznek a függők és melyek a függetlenek.
    5. A függő adatok alapján készül a jóslás míg a függetlenek lesznek a viszonyszámok.
    6. Megkezdjük az adatok alapján "felkészíteni" az algoritmust a jóslásra.
    7. A helyes változók felépítése alapján megkezdjük a jóslást.
    8. Az algoritmus lefutása után megkapjuk táblázatos viszonylatban az eredeti adatokat és melletük a jósoltat is.
    9. Végül pedig grafikon kirajzolás segítségével szemléltetjül a kapott adatokat.

## Összefoglalás

Az algoritmus ezen szintjén képes beolvasott covid19 megbetegedési esetszám alapján halálozási számot jósolni
illetve képes összehasonlítani a meglevő adatokkal, mellyel reprezentálhatja a pontosságot. Emellett képes
kirajzolni az adatokat szemléltetve, az eredetiek elhelyezkedését illetve a lináris növekedést is.

---

 ## coronaPredictor.py

 Az algoritmus polinomiális regressziót alkalmaz.

 ### Polinomiális regresszió:

 A regressziót úgy kell meghatározni, hogy az eredmény kiszámításához a független és a függő változók közötti kapcsolatot
 megtalálja. Az első polinomiális regressziós modellt Gergonne 1815-ben alkalmazta. Arra szolgál, hogy megtalálják a
 legmegfelelőbb sort a regressziós vonal segítségével az eredmények előrejelzésére. A regressziós technikáknak sokféle
 típusa létezik, ezek közül a polinomiális regresszió egyike.

 Ez az egyik olyan regressziós technika, amelyet a szakemberek használnak az eredmény előrejelzésére. Ez a független és
 a függő változók közötti kapcsolat, ha a függő változó az n. fokozatú független változóhoz kapcsolódik. Nem követeli meg,
 hogy a függő és a független változók közötti kapcsolat legyen lineáris, tehát ha a vonal görbe, akkor lehet, hogy
 bármilyen polinom kifejezése van.

 A fő különbség a lineáris és a polinomiális regresszió között az, hogy a lineáris regresszió megköveteli a függő és
 független változók lineáris összekapcsolását, miközben ez jobban illeszkedik a vonalhoz, ha az egyenletben magasabb
 fokot foglalunk be a független változó kifejezésbe.

 Egyenlete: I = b0 + a1x + a2x ^ 2 + a3x ^ 3 +…. ANX ^ n

 Ha magasabb fokokat adunk hozzá, például kvadratikusan, akkor a vonal görbévé válik, amely jobban illeszkedik az adatokhoz.

 Az algoritmus a pandas, numpy, matplotlib, sklearn könyvtárak alapján íródott.

 ![Image](https://github.com/utassydenis/AFP2021_1_K0800_Csapat4_Covid_Big/blob/main/pictures/polynomial-regression.jpg)

 
