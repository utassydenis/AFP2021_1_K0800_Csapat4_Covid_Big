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