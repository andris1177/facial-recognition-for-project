# facial-recognition-for-project
## windows
``` powershell

```

<br>

## linux
``` bash

```
<br>
## Web szerver
### Bármilyen webszerver jó én apache-t használtzam xampon belül, mert van beépített mysql adatbázisa.

<br>

## adatbázis létrehozása
``` sql
CREATE DATABASE projekt_feladat;

CREATE TABLE felhasználó_adatok (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50) NOT NULL,
  password VARCHAR(255) NOT NULL
);

CREATE TABLE képek (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  image MEDIUMTEXT
);
```