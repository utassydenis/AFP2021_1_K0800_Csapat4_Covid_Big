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
A kliens és a szerver HTTP/HTTPS protokolon keresztül kommunikál egymással.

### Backend:
-Az adatok tárolásához szükség lesz egy adatbázisra amihez MySql-t használunk.
-A program különféle megadott oldalakról lekéri az eddigi és aktuális adatokat amit hozzáad az adatbázishoz és rendszerezi időrend, illetve régió alapján.
-A program egy Python scriptet használ ami legenerálja az előrejelzést.

## 8. Telepítési terv
--
A program webes felületen lesz elérhető.
PhpMyadmin konfigurálása.
Adatbázis tesztelése:
    Adatok lekérése a weboldalaktól.
    Adatok tárolása.

