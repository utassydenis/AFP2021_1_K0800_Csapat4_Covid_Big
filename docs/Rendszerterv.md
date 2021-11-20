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
Felhasznált technológiák:
 1. MySQL:
    A MySQL kezeli az adatbázisunkat, itt tároljuk el az adatokat.
    A program "query"-n keresztül kommunikál az adatbázissal, lekérdezéseket, müveleket végez el benne.
    XAMPP-al vezérelt, localhost-on elérhető.
2.  Python:   
    PyCharm fejlesztői környezetben folyik a programozás.
    A python program kezelői felülete Kivy használatával hoztuk létre, ennek segítségével rendezzük el a gombokat, képeket, feliratokat, megejelenő ablak méretét.
    A program letöltött adatok alapján dolgozik.
    Ezekből az adatokból kiválasztja a számunkra szükséges adatokat, amiket feltölt az adatbázisba.
    Az adatbázishoz a connector package használatával tud kapcsolódni, mysql connect használatával.
    Miután a kapcsolat létrejött a cursor használatával hajt végre utasításokat.



## 8. Telepítési terv
--
A program lokálisan működik.
A futtatáshoz szükség van MySQL elérésre, illetve internetkapcsolatra.
A felhasználónak le kell töltenie az alkalmazást a saját gépére, biztosítania kell a localhost elérését XAMPP-on keresztül.

## 9. Karbantartási terv
--
A rendszer karbantartása időszakos lesz. Hibákat a felhasználó egy hibabejelentő gomb segítségével tudja majd jelezni a fejlesztők felé.
A hibabejelentésnél a felhasználó leírhatja mi a hiba és opcionálisan megadhatja a folyamatot amivel a hiba történt (opcionálisan képernyőkép feltöltése). Az üzenetet csak a fejlesztők látják.

## 10. Adatbázis terv
--
![Image](https://github.com/utassydenis/AFP2021_1_K0800_Csapat4_Covid_Big/blob/main/pictures/adatb%C3%A1zis%20terv.png)

Az program leellenőrzi , hogy az adatbázis létezik e, ha nem létrehozza.
Ezután a program leellenőrzi , hogy létezik e a tábla, ha nem létrehozza.
A program ezután feltölti az adatokat.
Ezt a program a "frissítés" gombbal automatikusan elvégzi.

## 11. Implementációs terv
---
Python: A GUI felület python nyelven fog készülni. Ezeket a technológiákat amennyire csak lehet külön fájlokba írva készítjük, és úgy fogjuk egymáshoz csatolni a jobb
átláthatóság, könnyebb változtathatóság, és könnyebb bővítés érdekében. A programban megjelenítjük és alkalmazzuk az adatbázis kezelést emellett alkalmazzuk a Python
grafikus interfészét. 