| Folyamat száma  | Funkció | Tesztelési folyamat leírása | Végkifejlet | Komment | Várt eredmény| Időpont|
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 1  | Algoritmus kódolásának állapota | A kód teljes, sikeresen lefut. | Sikeres | - | Hibamentes futás. | 2021.12.13 |
| 2  | Adatok feldolgozása  | Az adatbázist beolvassa, sikeresen felosztja és jó alapja az algoritmusnak. | Sikeres | - | Adatbázis feldolgozás illetve szükségtelen adatok kiszűrése. | 2021.12.13
| 3  | Számítások  | Az algoritmus képes a számításra, viszont adatai még nem tökéletes. | Még javítható. | - | Tökéletes matematikai pontossággal való számítás. | 2021.12.13 |
| 4  | Adatok megjelenítése  | A kreált adatokat grafikon formában megkapjuk. | Sikeres | - | Vizuális reprezentálása az adatoknak. | 2021.12.13 |
| 5  | Predikció  | Nem ad még tökéletes adatokat vissza, javítani kell a pontosságot. | Még javítható. | Pontossággal való gondok. | A grafikonon ábrázolt görbébe tökéletesen beleillő adat visszaadása. | 2021.12.13 |
| 6  | Frontend gombjainak működése  | Gombok elhelyezkedése helyes, hibamentesen futnak | Sikeres | - | Hibaüzenet nélkül adja vissza a várt értéket. | 2021.12.20 |
| 7  | Frissítés gomb működése | Megnyomás esetén letölti a database.xlsx-et. | Sikeres | - | A letöltés megtörténik, az adatbázis használatra kész. | 2021.12.20 |
| 8  | Frissítés gomb rossz változók esetén. | Ha nem létezik az SQL adatbázis, akkor létre kell hoznia, majd feltöltenia helyes adatokkal. | Sikeres | - | Rossz változók esetén az elvárt adatok feltöltése. | 2021.12.20 |
| 9  | Dátum megadás az input mezőben. | A dátum szűrést 7 és 14 napra állítjuk és várjuk a különböző visszaadott értékeket. | Sikeres | - |Egyaránt helyes visszatérési érték megállapítása. | 2021.12.20 |
| 10 | Adatbázis cserével való tesztelés | Más xlsx illetve csv adatokat dolgoztatunk fel az algoritmussal. | Sikertelen | Az xlsx-et tökéletesen beolvassa, csv feldolgozást még javítani kell. |Kiterjesztéstől függetlenül helyes beolvasás az elvárható.| 2021.12.20 |
| 11 | A fő predictor algoritmus és a mellék input algoritmus összeillesztése. | A két kód lineáris együttműködésének vizsgálata azonos adatbázissal. | Sikertelen | Az input algoritmus hibás pontosággal dolgozik. | Második algoritmus fejlesztésre szorul. | Tökéletes pontossággal való együttműködés a két kód megírása között. | 2021.12.20 |
| 12 | A mellék algoritmus adatbázis használata| Sikeresen olvassa a fő algoritmus számára előkészített adatbázist | Sikeres | - | Hibamentes beolvasás a predikcióhoz | 2021.12.20|
| 13 | A mellék algoritmus adatfeldolgozása | A felosztás és fölösleges adatok kiszűrése sikeres.| Sikeres | - | Hibátlan szűrés, az algoritmusnak tökéletesesn kell olvasnia az adatokat csv-ből | 2021.12.20 |
| 14 | A mellék algoritmus tesztelése hibás adatbázissal| Hibaüzenet visszadobásnak sikeressége.| Sikertelen | Nem a megfelelő hibazüzenet jelenik meg. | Megfelelően informáló hibaüzenet visszaadása a user felé. | 2021.12.20 |


## Rados Kevin által készített report.