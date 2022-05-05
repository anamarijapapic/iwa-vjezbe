
# Vježba 4 – Session

Izmijeniti Vjezbu 3 na sljedeci nacin. Napraviti Python skriptu za odabir predmeta. Primjer rada skripte je ilustriran na idućim slikama.

![image](https://user-images.githubusercontent.com/92815435/159834986-ad49b518-9a14-498c-8373-06adb29e9a50.png)
![image](https://user-images.githubusercontent.com/92815435/159835036-6bf9de12-42dc-49a7-a796-f6ff27ab02f2.png)
![image](https://user-images.githubusercontent.com/92815435/159835080-26713b92-b33a-4097-a98b-61153f12627e.png)

![image](https://user-images.githubusercontent.com/92815435/159835115-b01a6c2f-2c73-4bd0-bb89-59b64b3c600b.png)
![image](https://user-images.githubusercontent.com/92815435/159835151-e9f5e5e5-3fc4-405e-a91e-edb095e4a5d3.png)
![image](https://user-images.githubusercontent.com/92815435/159835190-5aadefb4-c0d8-4b05-9a12-4bab89b8cb2e.png)

Svaka od stranica (godina) zadržava status predmeta (radio button ostaje označen prema zadnjem odabiru). Da bi se to omogućilo, pri promijeni stranice, **podatke o predmetima spremiti iz post parametara u sesiju u bazi podataka i čitati iz sesije u bazi podataka varijable pri generiranju HTML-a**. Skripta predmeti.py sadrži popis predmeta po godinama i druge potrebne podatke i potrebno ju je uključiti sa import. Sve funkcionalnosti moraju raditi i nakon dodavanja/uklanjanja predmeta iz popisa. 

Kôd podijeliti u funkcije za:
-	Ispis jednog predmeta sa odabirom
-	Ispis predmeta godine
-	Ispis upisnog lista
-	Spremanje odabira iz post parametere u sesiju u bazi podataka