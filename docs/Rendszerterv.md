# Rendszerterv

## 1. A rendszer célja
---

A rendszer célja, hogy a felhasznló egyszerűen és átláthatóan tudja használni az előtte lévő programot. Az adatbázisok megtekintésének lehetőségével
tisztában legyen azzal mely adatokból várhatja a jóslást. A számítás előtt, listázás segítsévégel láthatja mely adatok kerültek be az adatbázisból.
A jóslás funkció segítségével tudja véglegesíteni a számítás folyamat végbemenését. Amint ez megtörtént lehetőség nyílik a számára, hogy
grafikus felületen is megtekintse a számszerűsített adatokat.

## 2. Projektterv
---

## 3. Üzleti folyamatok modellje
---
![Image](https://github.com/utassydenis/AFP2021_1_K0800_Csapat4_Covid_Big/blob/main/pictures/ÜzletiFolyamatok.png)

## 4. Követelmények
---
### Funkcionális követelmények:
    - Létező adatbázis
    - Időintervallum megadása
    - COVID adatok jóslása intervallum alapján
    - Eredmény közlése számszerűsített adatokkal
    - Eredmény közlése grafikon segítségével

### Nem funkcionális követelmény:
    - A programnak átláthatónak kell lennie
    - Pontosnak kell lennie
    - Gyorsnak kell lennie

## 5. Funkcionális terv
---
### Rendszerszereplők:
    - Felhasználó

### Rendszerhasználati esetek és lefutásaik:

* Felhasználó:
    - Meg tudja adni az időintervallumot
    - Megtekintheti az eredményt számszerűsített adattal
    - Megtekintheti az eredményt grafikonon

### Menü-hierarchiák:

* Main menu:
    - Időintervallum megadása
    - Számszerűsített adat
    - Grafikon

## 6. Fizikai környezet
---
### Fejlesztői környezet:
    - Visual Studio Code
    - Pycharm
    - Google Colab
    - Git

### Futtatási környezet:
    A program futtatásához elsősorban egy számítógép szükséges, amire telepítve van a Python. A folyamatot megkönnyíti, ha telepítjük a Pycharm-ot, mivel
    azt egyszerű kezelni.
    Google Colab esetén elég egy Google account, így belépés után már futtatható is a program.

### Specifikáció:
    - Számítógép egy stabil operációs rendszerrel
    - Internetkapcsolat
    - Python
    - Pycharm

![Image](https://github.com/utassydenis/AFP2021_1_K0800_Csapat4_Covid_Big/blob/main/pictures/Rendszerterv%20-%20fizikai%20k%C3%B6rnyezet.jpg)

## 7. Architekturális terv
--
A program Python alapon, MySQL adatbázissal működik, így a működéshez szükség van XAMPP-ra.
A program képes frissíteni az adatbázist:
    1.: A program a frissítés gombbal letölti az internetről a legfrissebb adatokat.
    2.: A letöltött adatokból a program működéséhez szükséges adatoka átmásolja egy másik fájlba.
    3.: A program belép a MySQL-be:
        3.1.: A program leellenőrzi , hogy a használt adatbázis létezik e.
            3.1.1: Ha nem létezik az adatbázis , akkor a program létrehozza az adatbázist.
        3.2.: A program leellenőrzi , hogy létezik e a használt tábla.
            3.2.1.: Ha nem létezik a tábla , akkor a program létrehozza a táblát.
        3.3.: A program feltölti az adatokat a táblába.
A program képes egy megadott időintervallumból lekérdezni a megbetegedési , illetve halálozási adatokat, régiókra bontva.
    1.: Az program leellenőrzi , hogy a megadott időszak a megfelelő módon volt e megadva.
    2.: A program lekérdezi, hogy a megadott időszak az adatbázis adatain bell esik e.
    3.: A program a megadott régiónak és időintervallumnak megfelelően kijelzi az adatokat a felhasználó számára.


## 8. Telepítési terv
--
A program webes felületen lesz elérhető.
PhpMyadmin konfigurálása.
Adatbázis tesztelése:
    Adatok lekérése a weboldalaktól.
    Adatok tárolása.


## 9. Karbantartási terv
--
A rendszer karbantartása időszakos lesz. Hibákat a felhasználó egy hibabejelentő gomb segítségével tudja majd jelezni a fejlesztők felé.
A hibabejelentésnél a felhasználó leírhatja mi a hiba és opcionálisan megadhatja a folyamatot amivel a hiba történt (opcionálisan képernyőkép feltöltése). Az üzenetet csak a fejlesztők látják.