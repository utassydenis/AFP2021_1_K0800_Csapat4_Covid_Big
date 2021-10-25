# COVID-FORECAST
## Áttekintés
---
A projekt célja, hogy egy Pythonban megírt program meg tudja jósolni a COVID adatokat (pl. megbetegedések száma, elhalálozások száma,
napi fertőzöttek) egy időintervallum alapján. A program egy adatbázisból szerzi az adatokat. Az adatbázisnak tartalmaznia kell: 
dátum (nap, hónap, nap), napi fertőzöttek, halálozás, ország, népesség, kontinens, összes eddigi fertőzött. A könnyű tesztelés és
átláthatóság érdekében szükség van egy egyszerű GUI felületre, amin könnyedén meg lehet adni az időintervallumot, hogy mettől meddig
dolgozza fel az adatokat. Az időintervallum tetszőleges, lehet több hónap, egy hónap, de akár egy hét is. Például ha 2021.10.04-től
2021.10.10-ig állítjuk ezt be, akkor az adatok feldolgozásával meg tudja jósolni a 2021.10.11-2021.10.17-re valószínűsíthető COVID
adatokat.