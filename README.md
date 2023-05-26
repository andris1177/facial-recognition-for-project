# facial-recognition-for-project

## lfw letöltési link: http://vis-www.cs.umass.edu/lfw/#download

## windows
``` powershell
git clone https://github.com/andris1177/facial-recognition-for-project.git
cd facial-recognition-for-project/local/tensorflow-al
pip install -r requirements.txt
python train_data.py
python facere.py
```

<br>

## Linux
``` bash
git clone https://github.com/andris1177/facial-recognition-for-project.git
cd facial-recognition-for-project/local/tesorflow-al
pip3 install -r requirements.txt
python3 train_data.py
python3 facere.py
```

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